# EELS

> [!CAUTION]
> **VERY ROUGH DRAFT** - Steps 8-11 in Part 3 are incomplete and need better images/instructions.

> TODO:
> - [ ] Add image for "EELS Scan" button (Step 2, Part 3)
> - [ ] Better photo for STEM SI button
> - [ ] Show what auto gain looks like
> - [ ] Clarify zero loss extraction steps
> - [ ] Add comparison images for beam not centered

This guide covers Electron Energy Loss Spectroscopy (EELS) on the Spectra 300. The process has two parts: calibration in TEM mode and STEM EELS spectrum imaging.

> **Prerequisite:** Complete the [STEM alignment](STEM.md) procedure before starting.

**Acronyms:**

- `GIF` - Gatan Imaging Filter
- `EFTEM` - Energy Filtered Transmission Electron Microscopy
- `ZLP` - Zero Loss Peak
- `SI` - Spectrum Imaging
- `mulXY` - Multifunction X/Y knobs on hand panel

## Part 1: Calibration

Use a vacuum or thin amorphous carbon area for calibration.

1. **Find a calibration area**

   - Locate a vacuum region or thin amorphous carbon area on the standard sample

2. **Open DigitalMicrograph**

   - Open `DigitalMicrograph` on the left monitor
   - If you see any dialog box, click `OK` to dismiss

     <img src="img/EELS/EELS-digitalmicrograph-open.jpg" alt="DigitalMicrograph software opened" width="500">

   - Click `EFTEM` (Energy Filtered Transmission Electron Microscopy)

3. **Open FilterControl**

   - Go to `Help` → `User Mode` → `Power User`
   - Go to `Window` → `Floating Window` → `Filter Control`

     <img src="img/EELS/EELS-filter-control.jpg" alt="Filter Control window" width="500">

   - Notice the green circle in `TEMUI` showing EELS detector is active

     <img src="img/EELS/EELS-temui-eels-open.jpg" alt="TEMUI showing EELS detector active" width="500">

4. **Set beam intensity**

   - Converge the beam by adjusting the intensity knob

     <img src="img/EELS/EELS-beam-converged.jpg" alt="Beam converged to optimal intensity" width="500">

   - Lift the fluorescent screen by pressing `R1`
   - Click `View` in DigitalMicrograph
   - Go to `Filter Control` → `Aperture` → `Mask` to verify beam position

     Correct intensity:

     <img src="img/EELS/EELS-filter-mask-good.jpg" alt="Correct beam intensity in filter mask" width="500">

     Too high intensity (oversaturated):

     <img src="img/EELS/EELS-intensity-too-high.jpg" alt="Beam intensity too high - oversaturated" width="500">

5. **Center and tune the GIF**

   - Click `Center ZLP` in Filter Control
   - Click `Tune GIF`. Notice the message appears:

     <img src="img/EELS/EELS-tune-gif-message.jpg" alt="Tune GIF confirmation message" width="500">

   - Click `OK` to confirm

## Part 2: TEM EELS acquisition

1. **View the sample**

   - Set magnification to ~17,000x
   - Click `View` in DigitalMicrograph
   - Select `EF-CCD Camera` → `View` to see image real-time

     <img src="img/EELS/EELS-ef-ccd-camera-view.jpg" alt="EF-CCD camera view selection" width="500">

     <img src="img/EELS/EELS-sample-live-view.jpg" alt="Sample live view" width="500">

2. **Acquire zero loss image**

   - Go to `SingleMap` → click `Zero Loss Image`

     <img src="img/EELS/EELS-single-map-zero-loss.jpg" alt="Single map zero loss image option" width="500">

3. **Switch to EELS mode**

   - Click `EELS` button to switch modes

     <img src="img/EELS/EELS-mode-switch.jpg" alt="EELS mode button" width="500">

     > FIXME: use image where EELS is clicked

   - Notice the 2D EELS spectrum. Observe the plasma peak near the zero loss peak.

     <img src="img/EELS/EELS-2d-spectrum-plasma-peak.jpg" alt="2D EELS spectrum showing plasma peak" width="500">

   > FIXME: what's plasma peak?

4. **Align the zero loss peak**

   - Set exposure to 2e-4 in View mode
   - Click `Align ZLP`

     <img src="img/EELS/EELS-align-zlp.jpg" alt="Align zero loss peak interface" width="500">

     > FIXME: where is ZLP click?

## Part 3: STEM EELS spectrum imaging

1. **Set camera length**

   - In `Velox`, change camera length to 29 mm or 37 mm
   - Notice the beam size decreases

     <img src="img/EELS/EELS-velox-camera-length.jpg" alt="Velox camera length setting" width="500">

2. **Enable EELS scanning**

   - Press `EELS Scan` in the software

   > FIXME: attach image

3. **Find a vacuum area**

   - Navigate to a vacuum region for initial alignment

4. **Center the beam**

   - In EFTEM mode, use `mulXY` knobs to center the beam

     Before centering:

     <img src="img/EELS/EELS-multifunction-xy-beam-center.jpg" alt="Beam before centering" width="500">

     After centering:

     <img src="img/EELS/EELS-beam-shifted-correct.jpg" alt="Beam centered correctly" width="500">

5. **Switch to STEM SI mode**

   - Click `STEM SI` to switch to Spectrum Imaging mode

     <img src="img/EELS/EELS-stem-si-button.jpg" alt="STEM SI button" width="500">

6. **Find sample area**

   - Navigate to an area of interest on your sample

7. **Start scanning**

   - Click `Scan` → `View` to see the image

     <img src="img/EELS/EELS-scan-view.jpg" alt="Scan view interface" width="500">

8. **Adjust gain**

   - Right-click on ADF image → click `Auto Gain`

   > FIXME: add image showing auto gain result

9. **Stop viewing**

   - Click `View` again to stop live scanning

10. **Capture line scan (1D EELS)**

    - Click `Capture` and draw a line across the region of interest

      <img src="img/EELS/EELS-capture-line.jpg" alt="Draw line for 1D EELS capture" width="500">

    - Go to `EELS` → `User Mode`

      <img src="img/EELS/EELS-user-mode-menu.jpg" alt="EELS user mode menu" width="500">

    - Go to `EELS` → `Zero Loss` → `Extract Zero Loss`

      <img src="img/EELS/EELS-extract-zero-loss.jpg" alt="Extract zero loss option" width="500">

      > FIXME: clarify what "extract zero loss" does and expected result

11. **Capture area scan (2D EELS)**

    - Click `Capture` and select a rectangular area for 2D spectrum imaging

      <img src="img/EELS/EELS-capture-area-2d.jpg" alt="Select area for 2D EELS capture" width="500">

      > FIXME: add steps for analyzing 2D EELS data, expected output

## Part 4: End session

Follow the steps in [End session](sample-loading.md#end-session).

## Changelog

- Dec 18, 2024 - initial rough draft by Guoliang Hu and @bobleesj
