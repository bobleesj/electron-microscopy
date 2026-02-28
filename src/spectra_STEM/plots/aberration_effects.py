"""
Generate aberration effects visualization for STEM guide.

Shows how individual aberrations affect the ronchigram appearance.

Usage:
    python aberration_effects.py
"""

import torch
import matplotlib.pyplot as plt
from ronchigram import (
    calculate_lambda,
    polar_mesh_and_aperture,
    calculate_chi0,
    calculate_chi,
    calculate_ronchigram,
    generate_sample,
    generate_transmission_fn,
)

# Simulation parameters
NUM_PX = 512
KEV = 300.0
ANGLE_MAX_MRAD = 100
APERTURE_MRAD = ANGLE_MAX_MRAD * 0.95
DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# Aberration configurations to visualize
# Note: "Well corrected" uses small defocus to show sample structure realistically
# Note: A1 needs small defocus to show elliptical/2-fold pattern
ABERRATION_CONFIGS = [
    {"name": "Well corrected\n(~0 aberrations)", "mags": {0: 0.2e-9}},
    {"name": "C1 (Defocus)\n50 nm", "mags": {0: 50e-9}},
    {"name": "A1 (2-fold astig)\n50 nm", "mags": {0: 5e-9, 1: 50e-9, 4: 5e-6}},
    {"name": "B2 (Coma)\n100 nm", "mags": {2: 100e-9}},
    {"name": "A2 (3-fold astig)\n50 nm", "mags": {3: 50e-9}},
    {"name": "Cs (Spherical)\n10 μm", "mags": {4: 10e-6}},
]


def plot_ronchigram_grid(rr, pp, wavelength, obj_aperture, trans, output_path):
    """Generate grid showing ronchigram appearance for each aberration."""
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.flatten()
    for i, config in enumerate(ABERRATION_CONFIGS):
        mags = torch.zeros(14, dtype=torch.float32, device=DEVICE)
        for idx, val in config["mags"].items():
            mags[idx] = val
        chi0 = calculate_chi0(mags, rr, pp, wavelength)
        chi = calculate_chi(chi0)
        ronch = calculate_ronchigram(chi, trans, obj_aperture)
        axes[i].imshow(ronch.cpu().numpy(), cmap='gray')
        axes[i].set_title(config["name"], fontsize=14, fontweight='bold')
        axes[i].axis('off')
    plt.suptitle('Effect of Individual Aberrations on Ronchigram', fontsize=18, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_path}")


def main():
    print(f"Using device: {DEVICE}")
    torch.manual_seed(42)
    wavelength = calculate_lambda(KEV)
    rr, pp, obj_aperture = polar_mesh_and_aperture(ANGLE_MAX_MRAD, APERTURE_MRAD, NUM_PX, DEVICE)
    sample = generate_sample(NUM_PX, DEVICE)
    trans = generate_transmission_fn(sample)
    plot_ronchigram_grid(rr, pp, wavelength, obj_aperture, trans, 'aberration_ronchigram_grid.png')
    print("Done!")


if __name__ == "__main__":
    main()
