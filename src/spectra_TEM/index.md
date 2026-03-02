# TEM (Spectra)

This guide covers optional TEM alignment on the Spectra 300: column setup, eucentric height, aperture alignment, and image correction. TEM mode is useful for fast sample navigation and for users who need TEM-specific data (HRTEM, diffraction patterns). Most users will proceed directly to [STEM (Spectra)](../spectra_STEM/index.md).

<img src="img/APP-tmp-7056.jpg" alt="Spectra 300 workstation overview" width="800">

**Prerequisite:** The sample is already loaded and the holder is inserted into the Spectra 300. For sample loading and end session procedures, see [STEM (Spectra)](../spectra_STEM/index.md).

**Acronyms:**

- `mulXY` - Multifunction X/Y knobs on hand panel
- `TEMUI` - TEM User Interface (software)

**Workstation layout:**

| Monitor | Software | Purpose |
|---------|----------|---------|
| Bottom left | `TEMUI` | Microscope control, vacuum, alignments |
| Bottom right | `Velox` | Live imaging, acquisition |
| Top left | `ImageCorrector` | Aberration measurement & correction |
| Top right | Velox image gallery | Captured images from Velox |

## Overview

This guide covers two main phases:

| Phase | Procedures | Time |
| ----- | ---------- | ---- |
| [Part 1: Column alignment](#part-1-column-alignment) | Vacuum check, beam setup, eucentric height, monochromator, C2 aperture, condenser stigmatism, beam tilt, rotation center | 10-15 min |
| [Part 2: Image correction](#part-2-image-correction) | Capture image, C1A1 correction, Tableau measurement, save settings | 10-15 min |

## Part 0: Safety check

Do **not** skip this section. Verify every item before proceeding.

- [ ] Standard gold nanoparticle sample on a single-tilt holder is already loaded
- [ ] Latest updates from nemo.stanford.edu have been checked
- [ ] Arina detector is retracted
- [ ] Screen is inserted
- [ ] No errors across all software programs including `TEMUI`

## Part 1: Column alignment

### 1.1 Open column valves

Before imaging, verify that the vacuum system is ready and the column valves can be safely opened.

- [ ] **Verify vacuum pressure**

  1. In `TEMUI`, check the vacuum pressure values on the log scale (lower = better):

     | Gauge | Log Value | Why Important |
     |-------|-----------|---------------|
     | Gun | 1 | Highest vacuum needed for stable electron emission |
     | Liner | <10 | Prevents electron scattering along beam path |
     | Octagon | 1 | Protects sample from contamination and oxidation |
     | Projection | <30 | Maintains image quality in projection system |
     | Buffer tank | <50 | Ensures stable pumping performance |
     | Backing line | <80 | Turbo pump pushes compressed gas into the backing line |

- [ ] **Open column valves**

  1. In `TEMUI`, click `Col Valves Open`. The status changes to indicate the column valves are open and the turbo pump is off.

     <img src="img/TEM-col-valves-closed-turbo-on.jpg" alt="TEMUI showing column valves open, turbo pump off" width="400">

- [ ] **Set condenser apertures**

  1. In `TEMUI`, go to the `Tune` tab, then `Apertures`. Set Condenser 1, 2, 3 to 2000, 70, 1000.

     <img src="img/TEM-condenser-apertures-settings.jpg" alt="TEMUI aperture settings for C1, C2, C3" width="400">

### 1.2 Beam setup

Configure the beam parameters for initial navigation and sample finding.

- [ ] **Enter TEM mode**

  1. On the `Velox` software (bottom right monitor), verify TEM mode is active. If not, click the `TEM` button.

- [ ] **Set spot size**

  1. Set Spot Size 3 by pressing the `L3` or `R3` button on the hand panel. As spot size decreases, screen current increases and the image gets brighter.
  2. If the image is too bright, turn the intensity knob to decrease the screen current to around 2 nA and press `Linear` mode to see better contrast.

- [ ] **Find sample region**

  1. Set ~500x magnification by adjusting the magnification knob.
  2. Locate the gold (dark) and amorphous carbon boundary by driving the joystick on the hand panel. This contrast boundary serves as a visual marker to identify the region of interest across various magnifications.

     <img src="img/TEM-col-valves-open.jpg" alt="TEM view showing gold and carbon boundary at 500x" width="800">

### 1.3 Eucentric height

At eucentric height, the sample remains stationary when tilted. This is essential for accurate imaging and aberration correction. Complete eucentric height alignment after loading each sample. Do **not** skip this step.

- [ ] **Adjust z-axis**

  1. Set ~7,500x magnification by adjusting the magnification knob.

     <img src="img/TEM-alignment-eucentric-focus-handpanel.jpg" alt="Eucentric Focus button on hand panel" width="400">

  2. Press `z-axis` up or down on the hand panel. Watch the image contrast change as the sample moves through focus. At eucentric height, the contrast is minimized (the image appears most "washed out").

     <img src="img/TEM-alignment-reduced-contrast.jpg" alt="Reduced contrast at eucentric height" width="800">

### 1.4 Monochromator tune

The monochromator selects a narrow energy range from the electron beam. If the beam edge looks jagged, the monochromator needs alignment.

- [ ] **Check beam edge**

  1. Do you see a jagged area along the beam edge in the previous step? If not, skip this section. Otherwise, follow the steps below.

- [ ] **Adjust monochromator**

  1. In `TEMUI`, go to the `Mono` tab, then open `Monochromator Tune (Expert)` and click `Shift`.

     <img src="img/TEM-mono.jpg" alt="Monochromator Tune Expert panel" width="400">

  2. Adjust `mulXY` knobs until the jagged area disappears.

### 1.5 C2 aperture alignment

The C2 aperture controls convergence angle and beam size. It blocks off-axis electrons — only electrons within a certain angular range pass through. A user must center this aperture on the optical axis so that the beam expands and contracts symmetrically.

- [ ] **Enter two-lens mode**

  1. In `TEMUI`, go to the `Tune` tab, then `Beam Settings`, and click `Twolens`. In two-lens mode, C3 is turned off, so the beam behavior on screen is purely from C2. This makes it straightforward to detect and correct any C2 aperture misalignment. In three-lens mode, C3 reshapes the beam after C2, masking the misalignment.

     <img src="img/TEM-two-lens-mode.jpg" alt="Two lens mode in TEMUI" width="400">

- [ ] **Center and align C2 aperture**

  1. Center the beam by rolling the hand panel ball.
  2. Converge the beam by varying the intensity knob.
  3. Vary beam size by turning the intensity knob counterclockwise and clockwise. Notice the beam expansion is not concentric — this indicates the C2 aperture is off-center.
  4. Make the beam concentric: go to `Apertures`, click `Adjust` next to `Condenser 2`, then adjust the `mulXY` knobs until the beam expands and contracts concentrically.

     <img src="img/TEM-alignment-c2-aperture-adjust.jpg" alt="C2 aperture adjustment controls" width="400">

- [ ] **Return to three-lens mode**

  1. In `TEMUI`, go to `Beam Settings` and click `TEM` to return to three-lens mode.

     <img src="img/APP-beam-settings-tab.jpg" alt="Beam Settings tab showing TEM button" width="400">

  2. Verify the beam is centered and concentric.

     <img src="img/TEM-alignment-beam-centered-concentric.jpg" alt="Beam centered and concentric in three-lens mode" width="800">

### 1.6 Condenser stigmatism

Condenser astigmatism causes the beam to appear elliptical instead of round. Correcting this ensures a symmetric probe.

- [ ] **Increase magnification**

  1. Set ~200kx magnification by adjusting the magnification knob.
  2. If the beam has shifted from center, go to `Tune` tab, then `Direct Alignment`, click `Beam Shift`, and adjust the `mulXY` knobs to re-center.

- [ ] **Correct stigmatism**

  1. Enlarge the beam by adjusting the intensity knob.

     <img src="img/TEM-zoom-in.jpg" alt="Enlarged beam at 200kx" width="800">

  2. In `TEMUI`, click `Stigmator`, then `Condenser`. Adjust the `mulXY` knobs to make the beam as round as possible. The beam should remain circular as you vary the intensity knob. Press `None` when done.

### 1.7 Beam tilt

Beam tilt alignment minimizes lateral beam shift when the beam angle changes. Proper alignment ensures the beam tilts around a single point without drifting.

- [ ] **Align beam tilt**

  1. In `TEMUI`, go to `Direct Alignment` and click `Beam tilt pp X`. Adjust the `mulXY` knobs to minimize the lateral jiggle.
  2. Repeat for `Beam tilt pp Y`.
  3. If the beam center has shifted, click `Beam Shift` and adjust the `mulXY` knobs to re-center.

### 1.8 Rotation center

Rotation center alignment ensures the image rotates around the center of the field of view when focus changes.

- [ ] **Align rotation center**

  1. In `TEMUI`, go to `Direct Alignment` and click `Rotation Center`. The image pulses in and out of focus.
  2. Adjust the `mulXY` knobs to minimize lateral movement. The pulsing should appear concentric (expanding and contracting from the same point) with no side-to-side drift.

## Part 2: Image correction

### 2.1 Capture image

Before running the image corrector, a user must set up live imaging in `Velox` and find a suitable sample region.

- [ ] **Prepare for imaging**

  1. Find a flat area with a distribution of particle sizes and no holes.
  2. **Important:** Enlarge the beam to cover the entire fluorescent screen before lifting it. When the screen is raised, the camera and detectors below are exposed to the beam. A concentrated beam can permanently damage them.
  3. Press `R1` on the hand panel to lift the fluorescent screen.

- [ ] **Start live imaging**

  1. In `Velox` (right monitor), click the play button to start live imaging.

     <img src="img/APP-velox-play-button.jpg" alt="Play button in Velox" width="400">

  2. Do **not** change the intensity knob while the screen is lifted. The screen is lifted when `TEMUI` shows a black display with dose reading "Unavail".

  3. Gold nanoparticles should be visible on screen.

     <img src="img/TEM-underfocus-4-5-rings.jpg" alt="Gold nanoparticles slightly underfocused" width="800">

- [ ] **Explore focus (optional)**

  1. Press the `z-axis` buttons to observe how focus affects the image.

     Underfocus — edges appear bright with white Fresnel fringes:

     <img src="img/TEM-alignment-under-focus.jpg" alt="Underfocus: bright edge fringes" width="800">

     On focus — minimal fringe contrast:

     <img src="img/TEM-alignment-on-focus.jpg" alt="On focus: minimal fringes" width="800">

     Overfocus — contrast inverts, dark fringes at edges:

     <img src="img/TEM-alignment-over-focus.jpg" alt="Overfocus: inverted contrast" width="800">

### 2.2 C1A1 correction

C1A1 corrects first-order aberrations in the image-forming lenses: defocus (C1) and 2-fold astigmatism (A1).

- [ ] **Set underfocus**

  1. Press `Z-axis` down until you see 4-5 rings in the FFT (slight underfocus). The rings indicate Thon rings from the amorphous carbon, which the corrector software uses for aberration measurement.

     <img src="img/TEM-4-5-rings.jpg" alt="FFT showing 4-5 Thon rings at slight underfocus" width="800">

- [ ] **Reset stigmator values**

  1. Stop live scanning by clicking the play button in `Velox`.
  2. In `TEMUI`, go to the `Stigmator` quick tab. Reset `Objective` and `Image A1` to zero. If non-zero, right-click each button to reset, then click `Done`.

     <img src="img/TEM-stigmator-quick-tab.jpg" alt="Stigmator controls in TEMUI Quick tab" width="400">

- [ ] **Run C1A1**

  1. Open the `ImageCorrector` software (top left monitor).
  2. Set exposure time to 0.3s.
  3. Go to the `C1A1` tab and click `Start`. The microscope wobbles the focus up and down (changing objective lens current). The FFT is captured and its ring symmetry, angular distribution, and ring spacing are analyzed.
  4. During the iteration, carefully set intensity to **800–900 counts** by adjusting the intensity knob so the corrector has enough signal.

     <img src="img/TEM-alignment-c1a1-result.jpg" alt="C1A1 measurement results showing aberration values" width="800">

  5. Under `Auto correct`, set to `75%`, then press `Focus` and `A1` during the iteration to apply corrections.
  6. Aim for `A1` < 5 nm. If `C1` shows orange, manually adjust the Z-axis during the iteration. `C1` should be close to the suggested value (in the image above, the software suggests C1 of −599.3 nm).

### 2.3 Tableau measurement

Tableau measures higher-order aberrations by acquiring images at multiple beam tilts. This is necessary for sub-angstrom resolution.

- [ ] **Run Tableau**

  1. In `ImageCorrector`, go to the `Tableau` tab, select `Standard` next to `Tableau type`, then click `Start`.

     <img src="img/TEM-alignment-tableau-standard.jpg" alt="Tableau Standard measurement running" width="800">

- [ ] **Verify results**

  1. After the iteration completes, verify the aberration values match the targets below, then click `Accept`:

     | Parameter | Resolution < 0.10 nm (20 mrad) | Resolution < 0.08 nm (24 mrad) |
     |-----------|-------------------------------|--------------------------------|
     | A1        | < 5 nm                        | < 5 nm                         |
     | A2        | < 100 nm                      | < 50 nm                        |
     | B2        | < 100 nm                      | < 50 nm                        |
     | C3        | ~ −8 μm                       | ~ −8 μm                        |
     | A3        | < 5 μm                        | < 1.5 μm                       |
     | S3        | < 5 μm                        | < 1 μm                         |

  2. In `Velox`, click the camera button to capture an image and verify improvements.

### 2.4 Save optics settings

- [ ] **Save register**

  1. In `TEMUI`, go to `Files`, then `SBL FEG Registers`.
  2. Add name `300KV-TEM-<NAME>` and click `Add`.

     <img src="img/TEM-save-settings.jpg" alt="Save optics settings dialog" width="400">

- [ ] **Verify corrected image**

  1. In `Velox`, click the `Play` button to start live imaging and verify the aberration-corrected image quality.
  2. Done. You are now ready for [STEM probe alignment](../spectra_STEM/index.md).

## Appendix

### Save file to USB

Plug your USB into the following computer:

<img src="img/APP-usb-computer.jpg" alt="Computer for USB data transfer" width="400">

<details>
<summary><strong>Reference images (click to expand)</strong></summary>

**Gray colors during C1A1 probe correction:**

Seeing gray colors like below?

<img src="img/APP-beam-setting-menu.jpg" alt="Beam Setting dropdown menu in TEMUI" width="400">

In `Velox`, click `Auto-tune`. Increase the signal until it touches the red and blue dotted lines:

<img src="img/APP-auto-tune.jpg" alt="Auto-tune signal adjustment" width="400">

**Hand panel R1, R2, R3 values:**

<img src="img/APP-hand-panel-keys.jpg" alt="Hand panel button assignments" width="400">

**Stage position and coordinates:**

<img src="img/APP-stage-position.jpg" alt="TEMUI stage position showing X, Y, Z coordinates" width="400">

**Dose rate and TEM mode display:**

<img src="img/APP-dose-rate-TEM.jpg" alt="TEM interface showing dose rate and imaging mode" width="400">

**HAADF detector on TEMUI:**

<img src="img/APP-haadf-detector-temui.jpg" alt="HAADF detector settings in TEMUI interface" width="400">

**Samples with holes:**

<img src="img/APP-sample-with-holes.jpg" alt="Sample view showing holes in specimen" width="400">

**Wobbler to check eucentric height:**

At eucentric height, tilting the holder should induce minimal shift.

<img src="img/APP-wobbler-eucentric-height.jpg" alt="Wobbler function for eucentric height verification" width="400">

**Smart tilt:**

<img src="img/APP-smart-tilt.jpg" alt="Smart Tilt feature in TEMUI Quick tab" width="400">

**Beam setting in Quick tab:**

<img src="img/APP-beam-setting-quick-tab.jpg" alt="Beam Setting options in TEMUI Quick tab" width="400">

**Stage piezo in Quick tab:**

<img src="img/APP-stage-piezo-quick-tab.jpg" alt="Stage Piezo controls in TEMUI Quick tab" width="400">

**Stage tab:**

<img src="img/APP-stage-tab.jpg" alt="Stage tab showing position and tilt controls" width="400">

</details>

## Troubleshooting

Common problems encountered during TEM sessions.

| Problem | Cause | Solution |
| ------- | ----- | -------- |
| Beam is not round after C2 alignment | Condenser astigmatism | Go to `Stigmator`, then `Condenser`, adjust `mulXY` knobs |
| Beam shifts when changing magnification | Beam Shift not set | Use `Direct Alignment`, then `Beam Shift` to store center position |
| Image drifts when tilting | Eucentric height not set | Re-do eucentric height ([1.3](#13-eucentric-height)) |
| C1A1 shows orange for C1 | Focus too far from target | Manually adjust Z-axis during iteration |
| Tableau values outside specification | Higher-order aberrations uncorrected | Run additional Tableau iterations, reduce Auto correct to 75% |
| Gray image in Velox during C1A1 | Intensity too low for corrector | Adjust intensity knob to 800-900 counts during iteration |
| No beam visible after opening column valves | Beam is blanked or screen not inserted | Check beam blank status, verify screen position |

## FAQ

**Convergence angle:** In `TEMUI`, go to `Beam Setting`, then `Probe`, and use the `mulXY` knobs to adjust.

**Tableau and C1A1:** Tableau measures aberrations visually across multiple tilt angles. C1A1 corrects first-order aberrations (defocus and astigmatism). Run C1A1 first, then Tableau for higher-order corrections.

**Underfocus direction:** Counterclockwise on hand panel, Z-axis down.

**Eucentric height:** The z-position where tilting does not shift the sample. At eucentric height, defocus = 0 and probe size is smallest relative to the sample.

**Beam Shift vs hand panel ball:** Beam Shift stores the center position internally, so the beam stays centered when changing magnification. The hand panel ball moves the beam but does not save the position.

**Underfocus vs overfocus:** Underfocus produces bright white Fresnel fringes at edges. Overfocus inverts the contrast with dark fringes.

**Monochromator:** Filters the electron beam to select a narrow energy range, improving energy resolution for EELS and reducing chromatic aberration.

**Two-lens vs three-lens mode:** Two-lens mode (C1+C2) turns off C3, providing a simpler beam path for C2 aperture alignment. Three-lens mode (C1+C2+C3) is the standard operating mode for TEM imaging.

**Objective lens in TEM:** In TEM, the objective lens sits below the sample and forms the first magnified image. In STEM, it sits above the sample and focuses the probe.

**C2 aperture purpose:** The C2 aperture blocks off-axis electrons, controlling the convergence angle and beam current. It must be centered on the optical axis for symmetric beam expansion.

## References

- [Thermo Fisher Spectra 300 TEM](https://www.thermofisher.com/us/en/home/electron-microscopy/products/transmission-electron-microscopes/spectra-300-tem.html)

## Changelog

- Mar 1, 2026 - Restructure to match STEM guide format with subsections, checklists, and troubleshooting table
- Dec 15, 2025 - Add pre-probe corrector with STEM Direct Alignment steps by @bobleesj
- Dec 12, 2025 - Add STEM training images by Guoliang Hu
- Dec 8, 2025 - First draft of Spectra training by @bobleesj
