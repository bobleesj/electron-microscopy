"""
Ronchigram simulation for electron microscopy.

This module provides functions for simulating Ronchigrams, which are shadow images
formed in the back focal plane of an electron microscope. Ronchigrams are used for
aberration measurement and correction in STEM.

The simulation follows the standard approach:

1. Calculate the aberration function χ₀(α, φ) from aberration coefficients
2. Form the probe wavefunction ψ = exp(-iχ₀)
3. Propagate through a sample (transmission function)
4. Calculate intensity in the diffraction plane

Functions
---------
calculate_lambda
    Relativistic electron wavelength
polar_mesh_and_aperture
    Create coordinate mesh and aperture mask
calculate_chi0
    Aberration function χ₀(α, φ)
calculate_chi
    Complex probe wavefunction from aberration function
generate_sample
    Random amorphous sample pattern
generate_transmission_fn
    Transmission function from sample potential
calculate_ronchigram
    Full Ronchigram intensity calculation
"""

import torch


# Physical constants
ANG2M = 1e-10     # Angstrom to meters
MRAD2RAD = 1e-3   # milliradian to radian

# Standard aberration indices (n, m) for 14 aberrations up to 5th order
N_IDX = torch.tensor([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5], dtype=torch.float32)
M_IDX = torch.tensor([0, 2, 1, 3, 0, 2, 4, 1, 3, 5, 0, 2, 4, 6], dtype=torch.float32)

# Aberration names for reference
ABERRATION_NAMES = [
    "C10 (defocus)",
    "C12 (2-fold astig)",
    "C21 (coma)",
    "C23 (3-fold astig)",
    "C30 (spherical)",
    "C32",
    "C34",
    "C41",
    "C43",
    "C45",
    "C50",
    "C52",
    "C54",
    "C56",
]

# Default aberration ranges in meters (for normalization)
DEFAULT_ABERRATION_RANGES = torch.tensor([
    100e-9,   # C10 defocus: ±100 nm
    50e-9,    # C12 2-fold astigmatism: ±50 nm
    100e-9,   # C21 coma: ±100 nm
    50e-9,    # C23 3-fold astigmatism: ±50 nm
    1e-6,     # C30 spherical: ±1 μm
    100e-9,   # C32: ±100 nm
    50e-9,    # C34: ±50 nm
    500e-9,   # C41: ±500 nm
    200e-9,   # C43: ±200 nm
    100e-9,   # C45: ±100 nm
    10e-6,    # C50: ±10 μm
    1e-6,     # C52: ±1 μm
    500e-9,   # C54: ±500 nm
    200e-9,   # C56: ±200 nm
])


def calculate_lambda(keV: float) -> torch.Tensor:
    """
    Calculate relativistic electron wavelength.

    Uses the relativistic formula:

    .. math::

        \\lambda = \\frac{12.3986}{\\sqrt{(2 \\times 511 + E) \\times E}}

    where E is in keV and λ is in Angstroms.

    Parameters
    ----------
    keV : float
        Accelerating voltage in keV

    Returns
    -------
    torch.Tensor
        Electron wavelength in meters
    """
    lambda_ang = 12.3986 / torch.sqrt(torch.tensor((2 * 511 + keV) * keV))
    return lambda_ang * ANG2M


def polar_mesh_and_aperture(
    r_max: float,
    obj_ap_r: float,
    num_px: int,
    device: torch.device,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Create polar coordinate meshgrid and objective aperture mask.

    Parameters
    ----------
    r_max : float
        Maximum radius (angle) in mrad
    obj_ap_r : float
        Objective aperture radius in mrad
    num_px : int
        Number of pixels
    device : torch.device
        Torch device for tensor allocation

    Returns
    -------
    tuple of (rr, pp, oapp)
        rr : torch.Tensor
            Radial coordinates α in mrad, shape (num_px, num_px)
        pp : torch.Tensor
            Angular coordinates φ in radians, shape (num_px, num_px)
        oapp : torch.Tensor
            Objective aperture mask (1 inside, 0 outside), shape (num_px, num_px)
    """
    center = num_px / 2

    i = torch.arange(num_px, device=device, dtype=torch.float32)
    ii, jj = torch.meshgrid(i, i, indexing="ij")

    x_val = (ii - center) / center * r_max
    y_val = (jj - center) / center * r_max

    rr = torch.sqrt(x_val**2 + y_val**2)
    pp = torch.atan2(y_val, x_val)
    oapp = (rr <= obj_ap_r).float()

    return rr, pp, oapp


def calculate_chi0(
    mags: torch.Tensor,
    rr: torch.Tensor,
    pp: torch.Tensor,
    wavelength: float,
    angles: torch.Tensor | None = None,
) -> torch.Tensor:
    """
    Calculate the aberration function χ₀(α, φ).

    The aberration function is defined as:

    .. math::

        \\chi_0 = \\frac{2\\pi}{\\lambda} \\sum_{n,m} 
        \\frac{C_{n,m} \\alpha^{n+1}}{n+1} \\cos(m(\\phi - \\phi_{n,m}))

    Uses the standard 14 aberrations up to 5th order:
    (1,0), (1,2), (2,1), (2,3), (3,0), (3,2), (3,4),
    (4,1), (4,3), (4,5), (5,0), (5,2), (5,4), (5,6)

    Parameters
    ----------
    mags : torch.Tensor
        Aberration magnitudes in meters, shape (14,) or (batch, 14)
    rr : torch.Tensor
        Radial coordinates α in mrad, shape (H, W)
    pp : torch.Tensor
        Angular coordinates φ in radians, shape (H, W)
    wavelength : float
        Electron wavelength in meters
    angles : torch.Tensor, optional
        Aberration orientation angles in radians, shape (14,).
        If None, all angles are set to 0 (rotationally symmetric).

    Returns
    -------
    torch.Tensor
        Aberration function χ₀ in radians, shape (H, W) or (batch, H, W)
    """
    n_idx = N_IDX.to(rr.device)
    m_idx = M_IDX.to(rr.device)

    if angles is None:
        angles = torch.zeros(14, device=rr.device)

    alpha_rad = rr * MRAD2RAD

    # Handle batched input
    if mags.dim() == 1:
        mags = mags.unsqueeze(0)
        squeeze_output = True
    else:
        squeeze_output = False

    batch_size = mags.shape[0]

    # Reshape for broadcasting: (14, 1, 1) for element-wise ops
    n_3d = n_idx.view(1, -1, 1, 1)
    m_3d = m_idx.view(1, -1, 1, 1)
    angles_3d = angles.view(1, -1, 1, 1)
    mags_4d = mags.view(batch_size, 14, 1, 1)

    # Expand spatial dimensions
    alpha_4d = alpha_rad.unsqueeze(0).unsqueeze(0)  # (1, 1, H, W)
    pp_4d = pp.unsqueeze(0).unsqueeze(0)  # (1, 1, H, W)

    # Compute all terms at once
    prefactor = 2 * torch.pi / wavelength
    terms = (
        prefactor
        * mags_4d
        * (alpha_4d ** (n_3d + 1))
        / (n_3d + 1)
        * torch.cos(m_3d * (pp_4d - angles_3d))
    )

    chi0 = terms.sum(dim=1)  # Sum over 14 aberrations

    if squeeze_output:
        chi0 = chi0.squeeze(0)

    return chi0


def calculate_chi(chi0: torch.Tensor) -> torch.Tensor:
    """
    Calculate the complex probe wavefunction from aberration function.

    .. math::

        \\psi = \\exp(-i \\chi_0)

    Parameters
    ----------
    chi0 : torch.Tensor
        Aberration function in radians

    Returns
    -------
    torch.Tensor
        Complex probe wavefunction
    """
    return torch.exp(-1j * chi0)


def mask_chi0(
    chi0: torch.Tensor,
    rr: torch.Tensor,
    threshold: float = torch.pi / 4,
) -> tuple[torch.Tensor, float]:
    """
    Create flat region mask and find minimum radius where |χ₀| exceeds threshold.

    This is useful for identifying the "sweet spot" in a Ronchigram where
    aberrations are small enough for high-resolution imaging.

    Parameters
    ----------
    chi0 : torch.Tensor
        Aberration function in radians
    rr : torch.Tensor
        Radial coordinates in mrad
    threshold : float, optional
        Phase threshold in radians (default: π/4)

    Returns
    -------
    tuple of (chi0_mask, r_max_mrad)
        chi0_mask : torch.Tensor
            Binary mask (255 inside flat region, 0 outside)
        r_max_mrad : float
            Flat region radius in mrad
    """
    flat_mask = (torch.abs(chi0) < threshold).float()
    chi0_mask = flat_mask * 255

    outside_mask = 1 - flat_mask
    radii_outside = outside_mask * rr
    radii_outside = torch.where(
        radii_outside > 0, radii_outside, torch.tensor(1e5, device=rr.device)
    )
    r_max_mrad = radii_outside.min().item()

    return chi0_mask, r_max_mrad


def generate_sample(
    num_px: int,
    device: torch.device,
    scale_factor: int = 8,
    seed: int | None = None,
) -> torch.Tensor:
    """
    Generate a random amorphous sample pattern.

    Creates random noise at lower resolution, then upscales using
    nearest-neighbor interpolation to create coarser features that
    resemble an amorphous sample.

    Parameters
    ----------
    num_px : int
        Output size (num_px × num_px)
    device : torch.device
        Torch device for tensor allocation
    scale_factor : int, optional
        Feature size scaling (larger = coarser features), default 8
    seed : int, optional
        Random seed for reproducibility

    Returns
    -------
    torch.Tensor
        Random sample pattern with values in [0, 1], shape (num_px, num_px)
    """
    if seed is not None:
        torch.manual_seed(seed)

    small_size = num_px // scale_factor
    subsample = torch.rand(small_size, small_size, device=device)

    sample = torch.nn.functional.interpolate(
        subsample.unsqueeze(0).unsqueeze(0),
        size=(num_px, num_px),
        mode="nearest",
    ).squeeze()

    return sample


def generate_transmission_fn(
    sample: torch.Tensor,
    interaction_param: float = 1.0,
) -> torch.Tensor:
    """
    Generate the transmission function from sample potential.

    .. math::

        T(r) = \\exp\\left(-i \\frac{\\pi}{4} \\sigma V(r)\\right)

    The π/4 factor produces reasonable phase contrast without requiring actual
    sample potentials and thicknesses. With sample values in [0, 1] and
    interaction_param=1, the maximum phase shift is π/4 ≈ 0.79 rad.

    Parameters
    ----------
    sample : torch.Tensor
        Sample potential pattern with values in [0, 1]
    interaction_param : float, optional
        Scaling factor for phase strength (default: 1.0)

    Returns
    -------
    torch.Tensor
        Complex transmission function
    """
    phase = torch.pi / 4 * sample * interaction_param
    return torch.exp(-1j * phase)


def calculate_ronchigram(
    chi: torch.Tensor,
    trans: torch.Tensor,
    oapp: torch.Tensor,
    normalize: bool = True,
) -> torch.Tensor:
    """
    Calculate the Ronchigram intensity pattern.

    The Ronchigram is calculated as:

    .. math::

        I = |\\mathcal{F}\\{T \\cdot \\mathcal{F}\\{\\psi\\}\\}|^2 \\cdot A_{obj}

    Parameters
    ----------
    chi : torch.Tensor
        Complex probe wavefunction, shape (H, W) or (batch, H, W)
    trans : torch.Tensor
        Complex transmission function, shape (H, W)
    oapp : torch.Tensor
        Objective aperture mask, shape (H, W)
    normalize : bool, optional
        If True, normalize intensity to [0, 1] range (default: True)

    Returns
    -------
    torch.Tensor
        Ronchigram intensity, shape (H, W) or (batch, H, W)
    """
    # Handle batched input
    if chi.dim() == 2:
        chi = chi.unsqueeze(0)
        squeeze_output = True
    else:
        squeeze_output = False

    # FFT of probe wavefunction (to real space)
    chi_fft = torch.fft.fft2(chi)

    # Multiply by transmission function
    exit_wave = chi_fft * trans.unsqueeze(0)

    # FFT back to diffraction plane
    diffraction = torch.fft.fft2(exit_wave)

    # Intensity
    intensity = torch.abs(diffraction) ** 2

    # Apply objective aperture
    intensity = intensity * oapp.unsqueeze(0)

    if normalize:
        # Normalize each image independently
        batch_min = intensity.view(intensity.shape[0], -1).min(dim=1).values
        batch_max = intensity.view(intensity.shape[0], -1).max(dim=1).values
        batch_min = batch_min.view(-1, 1, 1)
        batch_max = batch_max.view(-1, 1, 1)
        intensity = (intensity - batch_min) / (batch_max - batch_min + 1e-8)

    if squeeze_output:
        intensity = intensity.squeeze(0)

    return intensity


def forward_model(
    mags: torch.Tensor,
    rr: torch.Tensor,
    pp: torch.Tensor,
    oapp: torch.Tensor,
    wavelength: float,
    trans: torch.Tensor,
    angles: torch.Tensor | None = None,
) -> torch.Tensor:
    """
    Complete forward model: aberrations → Ronchigram intensity.

    This is the main function for simulating a Ronchigram from aberration
    coefficients. It combines all steps: aberration function calculation,
    probe formation, and Ronchigram intensity.

    Parameters
    ----------
    mags : torch.Tensor
        Aberration magnitudes in meters, shape (14,) or (batch, 14)
    rr : torch.Tensor
        Radial coordinates α in mrad, shape (H, W)
    pp : torch.Tensor
        Angular coordinates φ in radians, shape (H, W)
    oapp : torch.Tensor
        Objective aperture mask, shape (H, W)
    wavelength : float
        Electron wavelength in meters
    trans : torch.Tensor
        Complex transmission function, shape (H, W)
    angles : torch.Tensor, optional
        Aberration orientation angles in radians, shape (14,)

    Returns
    -------
    torch.Tensor
        Normalized Ronchigram intensity in [0, 1], shape (H, W) or (batch, H, W)
    """
    chi0 = calculate_chi0(mags, rr, pp, wavelength, angles)
    chi = calculate_chi(chi0)
    intensity = calculate_ronchigram(chi, trans, oapp, normalize=True)
    return intensity


class RonchigramSimulator:
    """
    Ronchigram simulator with fixed microscope parameters.

    This class encapsulates the simulation setup (wavelength, aperture, sample)
    so that multiple Ronchigrams can be generated efficiently by only varying
    the aberration coefficients.

    Parameters
    ----------
    keV : float, optional
        Accelerating voltage in keV (default: 200)
    num_px : int, optional
        Image size in pixels (default: 128)
    r_max : float, optional
        Maximum angle in mrad (default: 50)
    obj_ap_r : float, optional
        Objective aperture radius in mrad (default: 40)
    device : torch.device, optional
        Torch device (default: CPU)
    sample_seed : int, optional
        Random seed for sample generation (default: 42)

    Examples
    --------
    >>> sim = RonchigramSimulator(keV=200, num_px=128)
    >>> mags = torch.randn(14) * 1e-8  # Random aberrations
    >>> ronch = sim.simulate(mags)
    >>> ronch.shape
    torch.Size([128, 128])
    """

    def __init__(
        self,
        keV: float = 200.0,
        num_px: int = 128,
        r_max: float = 50.0,
        obj_ap_r: float = 40.0,
        device: torch.device | None = None,
        sample_seed: int = 42,
    ):
        if device is None:
            device = torch.device("cpu")

        self.keV = keV
        self.num_px = num_px
        self.r_max = r_max
        self.obj_ap_r = obj_ap_r
        self.device = device

        # Calculate wavelength
        self.wavelength = calculate_lambda(keV).item()

        # Create coordinate grids
        self.rr, self.pp, self.oapp = polar_mesh_and_aperture(
            r_max, obj_ap_r, num_px, device
        )

        # Generate fixed sample
        sample = generate_sample(num_px, device, seed=sample_seed)
        self.trans = generate_transmission_fn(sample)

        # Store aberration indices on device
        self.n_idx = N_IDX.to(device)
        self.m_idx = M_IDX.to(device)
        self.aberration_ranges = DEFAULT_ABERRATION_RANGES.to(device)

    def simulate(
        self,
        mags: torch.Tensor,
        angles: torch.Tensor | None = None,
    ) -> torch.Tensor:
        """
        Simulate Ronchigram from aberration coefficients.

        Parameters
        ----------
        mags : torch.Tensor
            Aberration magnitudes in meters, shape (14,) or (batch, 14)
        angles : torch.Tensor, optional
            Aberration orientation angles in radians

        Returns
        -------
        torch.Tensor
            Ronchigram intensity, shape (H, W) or (batch, H, W)
        """
        return forward_model(
            mags,
            self.rr,
            self.pp,
            self.oapp,
            self.wavelength,
            self.trans,
            angles,
        )

    def sample_aberrations(self, batch_size: int = 1) -> torch.Tensor:
        """
        Sample random aberration magnitudes within default ranges.

        Parameters
        ----------
        batch_size : int, optional
            Number of samples to generate (default: 1)

        Returns
        -------
        torch.Tensor
            Aberration magnitudes in meters, shape (batch_size, 14)
        """
        random_vals = torch.rand(batch_size, 14, device=self.device) * 2 - 1
        mags = random_vals * self.aberration_ranges.unsqueeze(0)
        return mags

    def normalize_aberrations(self, mags: torch.Tensor) -> torch.Tensor:
        """
        Normalize aberrations to [-1, 1] range.

        Parameters
        ----------
        mags : torch.Tensor
            Aberration magnitudes in meters

        Returns
        -------
        torch.Tensor
            Normalized aberrations in [-1, 1]
        """
        if mags.dim() == 1:
            return mags / self.aberration_ranges
        return mags / self.aberration_ranges.unsqueeze(0)

    def denormalize_aberrations(self, mags_norm: torch.Tensor) -> torch.Tensor:
        """
        Convert normalized [-1, 1] aberrations back to physical units.

        Parameters
        ----------
        mags_norm : torch.Tensor
            Normalized aberrations in [-1, 1]

        Returns
        -------
        torch.Tensor
            Aberration magnitudes in meters
        """
        if mags_norm.dim() == 1:
            return mags_norm * self.aberration_ranges
        return mags_norm * self.aberration_ranges.unsqueeze(0)
