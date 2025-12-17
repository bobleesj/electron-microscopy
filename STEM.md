# STEM

This guide covers STEM alignment on the Spectra 300. The process has three parts: TEM alignment (column optics), STEM alignment (focused probe), and imaging your sample.

> **Prerequisite:** Complete the [Sample loading](README.md#sample-loading) procedure before starting.

Acronyms

- `mulXY` - Multifunction X/Y knobs on hand panel

## Part 0: Safety check

- [ ] Standard sample is loaded
- [ ] Turbo pump is off, verified on TEMUI

## Part 1: Column optics alignment in TEM mode

1. **Find beam**

   - Click `Col Valves Open` on `TEMUI`
   - Set C1 to 2000, C2 to 70, C3 to 1,000 µm

     <img src="img/STEM/aperture-condenser.jpg" alt="aperture condenser" width="500">

   - At 700x, locate the gold (dark) and carbon boundary

     <img src="img/STEM/14-col-valves-open.jpg" alt="TEM view showing gold and carbon boundary region" width="500">

2. **Adjust eucentric height**

   - Increase magnification to ~7,500x
   - Press `Eucentric Focus` on hand panel

     <img src="img/STEM/TEM-alignment-eucentric-focus-handpanel.jpg" alt="Eucentric Focus on hand panel" width="500">

   - Notice diffraction pattern. Roll mouse scroller to see greater contrast.

     <img src="img/STEM/TEM-alignment-diffraction-pattern.jpg" alt="Diffraction pattern with greater contrast" width="500">

   - Converge the beam to a tiny dot with intensity knob

     <img src="img/STEM/TEM-alignment-beam-tiny-dot.jpg" alt="Beam converged to tiny dot" width="500">

   - Increase intensity. Image shows approximately minimal contrast.

     <img src="img/STEM/TEM-alignment-minimal-contrast.jpg" alt="Minimal contrast image" width="500">

   - Press `z-axis` on hand panel to reduce contrast even further

     <img src="img/STEM/TEM-alignment-reduced-contrast.jpg" alt="Reduced contrast" width="500">

3. **Align monochromator** 
   - Jagged area visible? Skip otherwise
   - `Mono` tab → click `Shift`, use `mulXY`

4. **Align C2 aperture**

   - `Tune` tab → click `Twolens`

     <img src="img/STEM/two-lens-mode.jpg" alt="two lens mode" width="500">

   - Notice beam shifted from center.
   - Make beam tiny by varying intensity knob
   - Center beam with hand panel ball
   - Increase beam to baseball size, vary intensity. Notice not concentric.
   - `Apertures` section → click `Adjust` next to `Condenser 2`, use `mulXY` to center beam

     <img src="img/STEM/TEM-alignment-c2-aperture-adjust.jpg" alt="C2 aperture adjustment" width="500">

   - `Beam Settings` tab → click `TEM` to return to three-lens mode
   - Ensure beam centered and concentric.

     <img src="img/STEM/TEM-alignment-beam-centered-concentric.jpg" alt="Beam centered and concentric" width="500">

5. **Fix condenser lens stigmation**

   - Go to ~200kx magnification using `Magnification` knob
   - Go to `Direct Alignment` → `Beam Shift`
   - Center beam with `mulXY`

     <img src="img/STEM/zoom-in.jpg" alt="zoom in" width="500">

   - Make beam baseball-size on fluorescent screen
   - Not concentric? `Stigmator` → `Condenser`, adjust with `mulXY`

6. **Fix beam tilt**

   - Go to `Direct Alignment` section
   - Click `Beam tilt pp X`, adjust `mulXY` to minimize jiggle
   - Repeat for `Beam tilt pp Y`
   - Notice beam center shifted again.
   - Click `Beam Shift`, use `mulXY` to center

7. **Fix rotation center**

   - Spread beam across entire fluorescent screen
   - Click `Rotation Center`
   - Notice the image is pulsing in and out.
   - Adjust `mulXY` to minimize pulsing until image moves symmetrically in/out

8. **Capture image**

   - Find a flat area with distribution of particle sizes, ensure no holes
   - Press `R1` to lift fluorescent screen. This enables beam to be detected by detector.
   - In `Velox`, click play to start seeing the image

     <img src="img/STEM/velox-under-focus-4-5rings.jpg" alt="velox under focus 4-5 rings" width="500">

   - (Optional) Press `z-axis` buttons to see how focus can change image:

     Under focus:

     <img src="img/STEM/TEM-alignment-under-focus.jpg" alt="Under focus" width="500">

     On focus:

     <img src="img/STEM/TEM-alignment-on-focus.jpg" alt="On focus" width="500">

     Over focus:

     <img src="img/STEM/TEM-alignment-over-focus.jpg" alt="Over focus" width="500">

9. **Run image corrector**

   - Press `Z-axis` down until you see 4-5 rings in FFT (slight underfocus)

     <img src="img/STEM/4-5-rings.jpg" alt="4-5 rings" width="500">

   - Stop recording. In `Velox`, click play button again
   - Reset `Objective`, `Image A1` in `TEMUI/Stigmator`. Right-click each button to reset

     <img src="img/STEM/TEM-alignment-stigmator-reset.jpg" alt="Stigmator reset" width="500">

   - Open `ImageCorrector` software
   - Click `C1A1` tab → `Start`
   - Aim for A1 < 5 nm. If `C1` shows orange, manually adjust Z-axis during iteration
   - Set intensity to 800-900 counts by adjusting Intensity knob
   - `C1` should be close to the suggested number. Below, software suggests C1 ~-599.3 nm.

     <img src="img/STEM/TEM-alignment-c1a1-result.jpg" alt="C1A1 result" width="500">

   - Go to `Tableau` tab → choose `Standard` under `Tableau type` → click `Start`

     <img src="img/STEM/TEM-alignment-tableau-standard.jpg" alt="Tableau standard" width="500">

   - Click `Accept` after the iteration
   - Go to `Tableau` → `Fast`
   - Click `Accept`
   - Press the A1, C1, etc. buttons in order
   - Check values meet the table below

   **Target values (TEM Image Corrector):**

   | Parameter | Resolution < 0.10 nm (20 mrad) | Resolution < 0.08 nm (24 mrad) |
   |-----------|-------------------------------|--------------------------------|
   | A1        | < 5 nm                        | < 5 nm                         |
   | A2        | < 100 nm                      | < 50 nm                        |
   | B2        | < 100 nm                      | < 50 nm                        |
   | C3        | ~ -8 μm                       | ~ -8 μm                        |
   | A3        | < 5 μm                        | < 1.5 μm                       |
   | S3        | < 5 μm                        | < 1 μm                         |

   - In `Velox`, click on the `Camera` button to take the picture

10. **Save optics settings**

    - `TEMUI` → `Files` → `SBL FEG Registers`
    - Add name `300KV-TEM-<NAME>` and click `Add`

      <img src="img/STEM/save-settings.jpg" alt="save settings" width="500">

    - Done! You are now ready for STEM probe alignment next.
    
## Part 2: Probe alignment in STEM mode

1. **Switch to STEM**

   - In `Velox`, click `STEM`, `HAADF`, set 1024×1024 / 250 ns dwell time
   - Drive around, set magnification to ~225 kx, find area with good distribution of feature sizes

     <img src="img/STEM/08-temui-settings.jpg" alt="TEMUI settings showing C1, C2, C3 values" width="500">

   - Adjust z-axis on hand panel until sharpest features
   - Verify convergence angle of 30 mrad, camera length 91 mm

     <img src="img/STEM/velox-FOV-length-probe-convergence-angle.jpg" alt="velox FOV length probe convergence angle" width="500">

   - Current should be ~0.100 nA. Too low? `Monochromator Tune (Expert)` → `Shift`, `Focus`, use `Intensity` knob to adjust

     <img src="img/STEM/STEM-alignment-monochromator-tune.jpg" alt="Modify intensity using Monochromator Tune" width="500">

   - Center beam on HAADF detector by clicking the HAADF button on TEMUI

2. **Reset aberrations**

> Why reset? The probe corrector software (Sherpa) measures the actual probe shape/ronchigram to calculate what corrections are needed. If manual stigmator corrections are already applied, the software can't distinguish between real aberrations from the optics and artificial corrections added.

   - `TEMUI` → `STEM Auto Tune` click `Reset`.

     <img src="img/STEM/STEM-alignment-stigmator-reset.jpg" alt="Reset stigmator in TEMUI" width="500">

   - `TEMUI` → `Stigmator` Reset `Probe A1` and `Condenser` to zero (right click)

     <img src="img/STEM/STEM-alignment-probe-a1-condenser-reset.jpg" alt="Reset Probe A1 and Condenser to zero" width="500">

3. **Fine-tune probe alignment**

   Ensure probe is aligned along the optical axis.

   - Press `Diffraction Mode` on hand panel
   - `Direct Alignment` → `Diffraction Shift and Focus Alignment`
   - Click `Center C2 aperture`, adjust with `mulXY`
   - Press `Diffraction Mode` again to exit

     <img src="img/STEM/probe-corrector-reset-aberration.jpg" alt="Probe corrector reset aberration" width="500">

4. **Run probe corrector** FIXME: which buttons to click?

   - In `Probe Corrector` software, set probe diameter 20 nm, semi-aperture 30 mrad

     <img src="img/STEM/probe-corrector-edit-probe-semi-aperture-to-30.jpg" alt="Probe corrector edit probe semi aperture to 30" width="500">

   - Run `C1A1`, try to make values close to zero

     <img src="img/STEM/STEM-alignment-c1a1-zero.jpg" alt="C1A1 values close to zero" width="500">

   - Click `0th-2nd`, set `Auto correct` to 50%

     <img src="img/STEM/STEM-alignment-0th-2nd-autocorrect.jpg" alt="0th-2nd autocorrect settings" width="500">

   - Go to `Tableau` → `Standard` → `Start`
   - Notice the aberration surface image. The aberration value in purple (e.g., C3) is the limiting aberration that needs correction.
   - Press the button with aberration C2, etc. sequentially until you see A4

     <img src="img/STEM/STEM-alignment-tableau-aberration-surface.jpg" alt="Tableau aberration surface" width="500">

   - Go to `C1A1` tab again
   - Adjust `C1` and `A1` again since adjusting higher-order aberrations may affect these
   - Run `C1A1` to ensure both values below 5 nm
   - Go back to `Tableau` tab
   - Select `A5` under Tableau options and click `Reevaluate`

     <img src="img/STEM/STEM-alignment-a5-reevaluate.jpg" alt="A5 reevaluate in Tableau" width="500">
   
   - Start `Tableau`, ensure to run `C1A1` again until you satisfy the target values below

      **Target values (STEM Probe Corrector):**

      > More or less identical as TEM

      | Parameter | Resolution < 0.10 nm (20 mrad) | Resolution < 0.08 nm (24 mrad) |
      |-----------|-------------------------------|--------------------------------|
      | A1        | < 5 nm                        | < 5 nm                         |
      | A2        | < 100 nm                      | < 50 nm                        |
      | B2        | < 100 nm                      | < 50 nm                        |
      | C3        | ~ -8 μm                       | ~ -8 μm                        |
      | A3        | < 5 μm                        | < 1.5 μm                       |
      | S3        | < 5 μm                        | < 1 μm                         |

   The Spectra microscope has reached about 48 pm. 49.9 pm is on the good side.

     <img src="img/STEM/STEM-alignment-final-resolution.jpg" alt="Final resolution result" width="500">

3. **Verify aberration corrected image**

   - In `Velox`, click the `Play` button
   - Done! You are now ready to image your sample

## Part 3: Image your sample

1. **Load your sample**

   - Follow load procedure in [README.md](README.md#how-to-remove-and-insert-holder)
   - Ensure Column is open
   - Ensure pressure values are correct on Spectra instrument and TEMUI:

     <img src="img/STEM/EXP-velox-tem-mode.jpg" alt="Velox TEM mode" width="500">

     <img src="img/STEM/EXP-velox-tem-view.jpg" alt="Velox TEM view" width="500">

   - Ensure you have the filename and folder setup in `Velox`

     <img src="img/STEM/EXP-velox-filename-setup.jpg" alt="Velox filename and folder setup" width="500">

2. **Find sample region of interest**

   - Enter `TEM` mode in `Velox
   - Go to lower magnification, below 1,000x to identify scan and region of interest

     <img src="img/STEM/EXP-low-mag-overview.jpg" alt="Low magnification overview" width="500">

   - Use diffraction pattern to find high contrast areas. Use HDR to see diffraction pattern.

     <img src="img/STEM/EXP-diffraction-pattern-hdr.jpg" alt="Diffraction pattern in HDR mode" width="500">

   - Go back to `STEM` and `HAADF` mode and click "play" button in Velox

     <img src="img/STEM/EXP-stem-haadf-view.jpg" alt="STEM HAADF view" width="500">

3. **Fine-tune focus with piezo**

   - Once you've found a good region of interest, `TEMUI` → `Sample Piezo`
   - Use `mulXY` to focus z-axis more precisely

     <img src="img/STEM/STEM-alignment-zone-axis.jpg" alt="Zone axis alignment" width="500">

4. **Run probe correction on sample**

   - Run `Sherpa` software, run `A1B1` then `B2/A2`
   - If you see the following error,

     <img src="img/STEM/EXP-sherpa-error.jpg" alt="Sherpa error" width="500">

     In `Velox`, click `Auto-tune` and ensure the signal touches the dotted `blue` and `red` lines

     <img src="img/STEM/EXP-velox-autotune.jpg" alt="Velox auto-tune signal adjustment" width="500">

   - Now it should work. Run `B2/A2`, this will take a few minutes.

     <img src="img/STEM/EXP-sherpa-b2a2-running.jpg" alt="Sherpa B2/A2 running" width="500">

1. **After probe correction**

   - If aberrations persist: `TEMUI` → `Stigmator` → `Probe A1`, adjust focus
   - Alternative: `Stigmator` tab → `Probe B2`, uncheck focus
   - Zoom in to verify correction

     <img src="img/STEM/EXP-zoomed-view.jpg" alt="Zoomed view after correction" width="500">

2. **Find zone-axis (optional)**

   - In `Velox`, drag the red dot to move probe position
   - `TEMUI` → `Quick` tab → `Smart Tilt` for automatic alpha/beta adjustment
   - After tilting, verify C1A1 is still good using the Sherpa software

## Part 4: End session

1. **Finish**

   - `TEMUI` → press `Column Valves Closed` → press `Turbo Pump On`
   - Follow unload procedure in [README.md](README.md#how-to-remove-and-insert-holder)

## Appendix

**Underfocus vs overfocus:**

- Underfocus: dark cores with bright Fresnel fringes on edges
- Overfocus: bright cores with dark edge fringes

Here is an example of underfocus image:

<img src="img/STEM/underfocus.jpg" alt="Underfocus example showing dark cores with bright Fresnel fringes" width="500">


**Gray colors during C1A1 probe correction:**

Grey colors shown below?

<img src="img/STEM/09-beam-setting-menu.jpg" alt="Beam Setting dropdown menu in TEMUI" width="500">

`Velox`, click `Auto-tune`. Increase signals touching the red and blue dotted lines:

<img src="img/STEM/velox-auto-tune.jpg" alt="Beam Setting dropdown menu in TEMUI" width="500">

Hand panel R1, R2, R3 values

<img src="img/STEM/TEMUI-hand-panel-keys.jpg" alt="TEMUI hand panel keys" width="500">

## FAQs

### Software

- **Convergence angle:** `Beam Setting` → `Probe`, use ``mulfYto`` adjust.

- **Tableau and C1A1:** Tableau shows aberrations visually. C1A1 corrects first-order aberrations (astigmatism and coma).

- **Underfocus direction:** Counterclockwise on hand panel, Z-axis down.

- **Eucentric height:** The z-position where tilting doesn't shift the sample. Defocus = 0. Probe size smallest relative to the sample.

- **Beam Shift vs hand panel ball:** Beam Shift stores the center position internally, so the beam stays centered when changing magnification.

- **Underfocus vs overfocus:** Underfocus: edges become white/bright Fresnel fringes. Overfocus: contrast inverts.

- **Monochromator:** Filters the electron beam to select a narrow energy range, improving energy resolution for EELS.

- **Scan often:** Tilt causes FOV to change, so rescan frequently.

- **Wobble at high mag:** Ensures no sample-induced aberration.

- **Verify zone axis:** Use CrystalMaker simulated diffraction and Kikuchi lines crossing in the center.

- **Major zone axis:** Thick bends tend to form.

- **Nanoparticle area for correction:** Focus on "size gradient" region between dark film and bulk. Better for aberration algorithms.


### Aberration correction

- TODO: **Image Correction vs. Probe Corrector:**
- TODO: 

> Simulate ronchigram for each aberration term: https://bobleesj.github.io/electron-microscopy-website/ronchigram.


### Lens system

- **Objective lens (TEM vs STEM):** In STEM, it sits above the sample and focuses the probe to ~1 Å. In TEM, it sits below and forms the first magnified image.

- **Back focal plane:** The objective lens focuses electrons scattered at the same angle to the same point here (forming the diffraction pattern).

- **Spherical aberration (Cs):** Electrons through outer lens focus at different points than center electrons. Blurs image, limits resolution. Cs correctors fix this.

- **Chromatic aberration (Cc):** Electrons with different energies focus at different points. Monochromator reduces this.

- **Cs corrector:** Uses multipole lenses to cancel spherical aberration, enabling sub-angstrom resolution.

- **Three condenser lenses (C1, C2, C3):** C1 controls brightness, C2 controls beam size/convergence, C3 provides additional probe formation flexibility.

- **Intensity knob:** Adjusts C2 lens to move crossover point. Clockwise = more focused, brighter. Counterclockwise = spread out, dimmer.

- **C2 aperture:** Limits beam angle and blocks stray electrons. Must be centered on optical axis.

- **Crossover symmetry:** If elliptical instead of round, there's condenser astigmatism degrading probe shape.

- **Two-lens vs three-lens mode:** Two-lens (C1+C2) for parallel illumination. Three-lens (C1+C2+C3) for STEM probe control. Align C2 in two-lens mode because it's simpler.

- **Objective aperture:** Sits at back focal plane, selects which diffracted beams contribute to image. Smaller = more contrast, less resolution.

- **Projector lenses:** Magnify and project image plane (imaging) or back focal plane (diffraction) onto screen/camera.

- **Focus changes with magnification:** Different mag uses different lens settings, slightly shifting focal plane.

- **Astigmatism correction:** Use stigmator coils (X and Y) to make elliptical beam circular.

- **Convergence angle and resolution:** Larger angle = higher resolution but more aberrations. There's an optimal angle.

### STEM detectors

- **HAADF:** High-Angle Annular Dark Field. Collects high-angle scattered electrons, gives Z-contrast.

- **ABF:** Annular Bright Field. Collects low-angle, good for light elements.

- **BF:** Bright Field. Collects direct beam.

- **Z-contrast:** Scattering scales with Z² (atomic number squared). Heavier atoms appear brighter.

- **Ronchigram:** Shadow image of probe on detector when focused on amorphous area. Flat, featureless = good alignment.

### Beam sensitive samples

- **Beam sensitive region:** Still scan, but on a small window only to avoid damaging other areas.

- **Beam intensity for sensitive materials:** ~50 pA can cause beam damage.

- **Alternative approach:** Use lower keV, but requires hours for beam to stabilize.

## References

- [Thermo Fisher Spectra 300 TEM](https://www.thermofisher.com/us/en/home/electron-microscopy/products/transmission-electron-microscopes/spectra-300-tem.html)

## Changelog

- Dec 15, 2025 - Add advanced pre-probe corrector with STEM Direct Alignment steps by @bobleesj
- Dec 12, 2025 - Add STEM training images by Guoliang Hu
- Dec 8, 2025 - First draft of SNSF Spectra training by @bobleesj

