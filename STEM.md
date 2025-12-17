# STEM

This guide covers STEM alignment on the Spectra 300. The process has three parts: TEM alignment (column optics), STEM alignment (focused probe), and imaging your sample.

> **Prerequisite:** Complete the [Sample loading](README.md#sample-loading) procedure before starting.

Acronyms

- `mulXY` - Multifunction X/Y knobs on hand panel

<img src="img/STEM/TEMUI-hand-panel-keys.jpg" alt="TEMUI hand panel keys" width="500">

## Part 1: Column optics alignment in TEM mode

Turn the turbo pump off if working with a standard sample. Go to TEM mode in Velox.

1. **Find beam**
   - Click `Col Valves Open` on `TEMUI`
   - Set C1 to 2000, C2 to 70, C3 to 1,000 µm
     <img src="img/STEM/aperture-condenser.jpg" alt="aperture condenser" width="500">

   - At 700x, locate the gold (dark) and carbon boundary
     <img src="img/STEM/14-col-valves-open.jpg" alt="TEM view showing gold and carbon boundary region" width="500">

2. **Adjust eucentric height**
   - Increase magnification to ~7,500x
   - Press `Eucentric Focus` on hand panel
     <img src="img/STEM-new/IMG_6956.jpg" alt="IMG_6956" width="500">
   - Converge the beam to a tiny dot with intensity knob.
     <img src="img/STEM-new/IMG_6957.jpg" alt="IMG_6956" width="500">
   - Notice diffraction pattern. Roll mouse scoller to see greater sensitivty on TEMUI. 
     <img src="img/STEM-new/IMG_6958.jpg" alt="IMG_6958" width="500">  
   - Image shows approximately minimal contrast.
     <img src="img/STEM-new/IMG_6959.jpg" alt="IMG_6959" width="500">
   - Press z-axis to reduce constrast even further.
     <img src="img/STEM-new/IMG_6960.jpg" alt="IMG_6960" width="500">
   - Done!

3. **Align monochromator** 
   - Jagged area visible? Skip otherwise. (Visible in the image right above)
   - `Mono` tab, click `Shift`, use ``mulXY``.

4. **Align C2 aperture**
   - `Tune` tab, click `Twolens`
     <img src="img/STEM/two-lens-mode.jpg" alt="two lens mode" width="500">
   - Notice beam shifted from center.
   - Make beam tiny by varying intensity knob.
   - Center beam with with hand panel ball.
   - Increase beam about baseball size. Vary intensity. Notice not concentric.
   - `Apertures` section, click `Adjust` next to `Condenser 2`, use ``mulXY`` to center beam.
     <img src="img/STEM-new/IMG_6961.jpg" alt="IMG_6961" width="500">
   -  `Beam Settings` tab, click `TEM` to return to three-lens mode.
   -  Ensure beam centered, concentric.
      <img src="img/STEM-new/IMG_6962.jpg" alt="IMG_6962" width="500">
   -  Done!

5. **Fix condenser lens stigmation**
   - Go to ~200kx magnification using `Magnification` knob
   - Go to `Direct Alignment` → `Beam Shift`
   - Center beam with ``mulXY``

     <img src="img/STEM/zoom-in.jpg" alt="zoom in" width="500">

   - Make beam baseball-size on fluorescent screen
   - Not concentric? `Stigmator` → `Condenser`, adjust with ``mulXY``

6. **Fix beam tilt**
   - Click `Beam tilt pp X` under `Direct Alignment` section
   - Adjust ``mulXY`` to minimize jiggle
   - Repeat for `Beam tilt pp Y`.
   - Notice beam center shfited again.
   - Click `Beam shift`, `mulXY` to center.

7. **Fix rotation center**
   - Spread beam across entire fluorescent screen.
   - Click `Rotation center` under `Direct Alignment` section
     <img src="img/STEM/velox-under-focus-4-5rings.jpg" alt="velox under focus 4-5 rings" width="500">
   - Adjust ``mulXY`` until image pulses symmetrically in/out

8. **Check iamge**
   - Press `R1` to lift fluorescent screen
   - In Velox, click play to start imaging
   - Notice images are being shown on Velox
   - ATTACH IMAGE OF OVER, ON, UNDER-FOCUS

9. **Run image corrector**
   - Press Z-axis down until you see 4-5 rings in FFT (slight underfocus)

     <img src="img/STEM/4-5-rings.jpg" alt="4-5 rings" width="500">

   - Stop Velox recording
   - Open `ImageCorrector` software
   - Find a flat area with distribution of particle sizes
   - `Stigmator` tab Reset `Objective`, `Image A1` only.
   - (FIXME) Press `C1A1`, aim for A1 < 5 nm. Is C1 high? Z-axis to adjust slightly. Intensity abour 800-900 by adjusting Intensity knob. C1 should be close to to the suggested number Ex) here, case ~-600 nm. 
     - ATTACH IMAGE HERE
   - Go to `Tableau` → `Fast`
   - Click `Accept`, press the A1, C1, etc. buttons in order to (as shown in the image)

   **Target values (TEM Image Corrector):**

   | Parameter | Resolution < 0.10 nm (20 mrad) | Resolution < 0.08 nm (24 mrad) |
   |-----------|-------------------------------|--------------------------------|
   | A1        | < 5 nm                        | < 5 nm                         |
   | A2        | < 100 nm                      | < 50 nm                        |
   | B2        | < 100 nm                      | < 50 nm                        |
   | C3        | ~ -8 μm                       | ~ -8 μm                        |
   | A3        | < 5 μm                        | < 1.5 μm                       |
   | S3        | < 5 μm                        | < 1 μm                         |

> We do want to resolve to 5th order in TEM? Yes, in STEM but no in TEM.

1.  **Save optics settings**

  <img src="img/STEM/save-settings.jpg" alt="save settings" width="500">

   - `TEMUI` → `Files` → `SBL FEG Registers`
   - Add name `300KV-TEM-<NAME>` and click `Add`


## Part 2: Probe alignment in STEM mode

Go to `STEM` mode in Velox.

1. **Switch to STEM**
    - `Velox` → click `STEM`, `HAADF`, set 1024×1024 / 250 ns dwell time
    - Ensure convergence angle of 30 mrad, camera length 91 mm
    - Current ~100 pA. Too low? (ATTACH IMAGE MONO) `Monochromotaore Tune Expert` -> `Shift`, `Focus`, use `intensity` know to adjust Screen (it should be 0.100 nA)
      - ATTACH IMAGE
    - Center beam on HAADF detector. Click the button shown below to see. `Direct Alignment`, `Diffraction Shfit and Focus alignment` -> `mulXY` to cneter the beam 
      - ATTACH IMAGE
    - Drive around, good distribution of feature sizes.
    - Adjust z-axis on hand panel until sharpest features:

      <img src="img/STEM/08-temui-settings.jpg" alt="TEMUI settings showing C1, C2, C3 values" width="500">

2. **Reset aberrations**
   - 
   - Set magnification to ~225 kx, find area with particle size distribution
   - `TEMUI` → `STEM autotuning` → `Settings` → `Reset`
   `Sitgmator` -> 
      <img src="img/STEM/use-stem-auto-tuning-reset-click.jpg" alt="use stem auto tuning reset click" width="500">

3. **Fine-tune probe alignment**

Ensure probe is alignde along the optical axis.

   - Press `Diffraction Mode` on hand panel
   - `Direct Alignment` → `Diffraction Shift and Focus Alignment`
   - Click `Center C2 aperture`, adjust with ``mulXY``
   - Press `Diffraction Mode` again to exit
    camera length of 91 mm, probe convergence angle from `Velox` `Detector Layout`
   - FOV is dynamic and fixed.

      <img src="img/STEM/velox-FOV-length-probe-convergence-angle.jpg" alt="velox FOV length probe convergence angle" width="500">
   
   - `STEM Auto tune` in TEMUI so that Probe Corrector's aberration values are all removed.

      <img src="img/STEM/probe-corrector-reset-aberration.jpg" alt="probe corrector reset aberration" width="500">

1. **Run probe corrector**
   - In `Probe Corrector` software, set probe diameter 20 nm, semi-aperture 30 mrad

      <img src="img/STEM/probe-corrector-edit-probe-semi-aperture-to-30.jpg" alt="probe corrector edit probe semi aperture to 30" width="500">

    - Click `C1A1` → `Start`
    - Aim for A1 < 5 nm, A2/B2 < 100 nm, A3/C3/S6 < 5 µm
    - Go to `Tableau` → `Standard` → `Start`, adjust C2/S2 until you see A4

      <img src="img/STEM/probe-corrector-tableau.jpg" alt="probe corrector tableau" width="500">


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

2. **Verify aberration corrected image**
   - `Velox` - Click `Play button`

## Part 3: Image your sample

1. **Upload standard sample**
2. **Load your sample**
3. **After probe correction**
    - If aberrations persist: `TEMUI` → `Stigmator` → `Probe A1`, adjust focus
    - Alternative: `Stigmator` tab → `Probe B2`, uncheck focus
    - Target resolution: D < 60 pm (spec is 50 pm)

      <img src="img/STEM/stem-probe-corrector-final-result.jpg" alt="stem probe corrector final result" width="500">

4. **Find zone-axis**
   - `Quick` tab → `Sample Piezo`, fine-tune z-axis
    - Unblank beam on Velox
    - In `Velox`, drag the red dot to move probe position
    - `Quick` → `Smart Tilt` for automatic alpha/beta adjustment
    - After tilting, verify C1A1 is still good

## Part 4: End session

1. **Finish**
    - `TEMUI` -> press `Column volume closed` -> press `Turbo pump on`
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




     <img src="img/STEM/07-c1a1-result.jpg" alt="C1A1 correction result showing aberration values" width="500">
