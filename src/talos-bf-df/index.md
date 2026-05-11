# Talos bright-field and dark-field imaging

> [!CAUTION]
> **VERY ROUGH DRAFT.** Notes from a **Stanford MATSCI 322 TEM Lab** session taught by **Andrew Barnum**, **Pinaki Mukherjee**, and **Ash**. This guide is being expanded and refined as @bobleesj uses the Talos in future sessions. Steps and screenshots still need verification against the live instrument.
>
> **TODO:** Add stage navigation, eucentric height alignment, selected-area aperture insertion, condenser aperture changes, dose-on-sample calibration, and end-of-session shutdown.

This guide covers the operational steps for bright-field (BF) and dark-field (DF) imaging on the Talos TEM, captured during a class session in April 2026. It also includes a reference example of how under- and over-focused images appear on the FluCam, which is useful when interpreting defocus during alignment.

**Acronyms:**

- `BF` : bright field
- `DF` : dark field
- `TEM` : transmission electron microscope
- `STEM` : scanning transmission electron microscope
- `FFT` : fast Fourier transform
- `Velox` : Thermo Fisher acquisition software for the Talos
- `FluCam` / `SmartCam` : fluorescent screen camera (used for alignment)
- `Ceta` : high-resolution CMOS camera mounted below the phosphor screen
- `mulXY` : multi-function X/Y knobs on the hand panel

## Overview

| Phase | What it covers | Time |
| ----- | ---------- | ---- |
| [Part 1: Startup and orientation](#part-1-startup-and-orientation) | System settle, identify legacy hardware, vacuum check | 5 min |
| [Part 2: Open Velox and select a camera](#part-2-open-velox-and-select-a-camera) | Launch Velox, choose FluCam or Ceta | 2 min |
| [Part 3: Configure acquisition parameters](#part-3-configure-acquisition-parameters) | Frame size, frame combining, shutter, recording mode | 3 min |
| [Part 4: Bright-field imaging](#part-4-bright-field-imaging) | Open valves, navigate, set illumination, annotate | varies |
| [Part 5: Dark-field imaging](#part-5-dark-field-imaging) | Beam tilt, dark-field toggle, BF/DF comparison | 10 min |

## Part 1: Startup and orientation

### 1.1 Allow the system to settle

- [ ] **Wait for the column to reach steady state**

  1. Wait 2 to 3 minutes after powering up the Talos console before interacting with the column.
  2. Confirm the vacuum and high-tension subsystems have stabilized.

### 1.2 Locate the legacy hardware buttons

- [ ] **Identify the legacy controls on the console**

  1. Identify the legacy hardware buttons on the console. These exist because, before live FFT was available, focus had to be judged on the phosphor screen using the "Wobbler" feature, which modulates the beam to highlight the focused condition.
  2. Use the live FFT in `Velox` for routine focusing. The legacy controls remain functional as a backup.

     <img src="img/p1_setup_01.jpg" alt="Close-up of the diffraction button and surrounding hardware controls on the Talos console" width="800">

### 1.3 Check the vacuum overview

- [ ] **Confirm vacuum status**

  1. Open the Talos UI vacuum overview panel.
  2. Confirm the column vacuum reads green before opening the column valves.

     <img src="img/p1_setup_02.jpg" alt="Talos UI showing the vacuum overview panel" width="800">

     > **CRITICAL:** Do not proceed if any vacuum gauge is yellow or red. Contact staff.

## Part 2: Open Velox and select a camera

### 2.1 Launch Velox

- [ ] **Open the Velox acquisition software**

  1. Launch `Velox` from the desktop.

     <img src="img/p1_setup_03.jpg" alt="Velox software window after launch, showing the camera selection options" width="800">

### 2.2 Select the FluCam for initial setup

- [ ] **Use the FluCam during alignment**

  1. Select the `FluCam` (also labeled `SmartCam` in some menus) for initial setup and alignment. The FluCam points at the phosphor screen rather than receiving the direct beam.
  2. Use this camera for any operations that risk a high beam dose, since it protects the more expensive `Ceta` CMOS camera underneath.

### 2.3 Switch to the Ceta camera for final acquisition

- [ ] **Switch to Ceta when alignment is satisfactory**

  1. Switch to the `Ceta` camera once the alignment is complete and a high-resolution image is required.

     <img src="img/p1_setup_04.jpg" alt="Velox camera selection menu with the Ceta TEM camera highlighted" width="800">

## Part 3: Configure acquisition parameters

### 3.1 Open the acquisition presets

- [ ] **Open both acquisition presets**

  1. Open the two acquisition presets in `Velox`.
  2. Update the parameters in each preset as needed during the session.

     <img src="img/p1_setup_05.jpg" alt="Velox dual acquisition preset panel" width="800">

### 3.2 Set frame size and frame combining

- [ ] **Set 1024 by 1024 frames with 200 ms combining**

  1. Set the frame size to 1024 by 1024 pixels.
  2. Set the frame combining to 200 ms. Frame combining averages multiple short exposures into a single output frame, which improves signal-to-noise without committing to one long exposure.

     <img src="img/p1_setup_06.jpg" alt="Velox acquisition parameters set to 1024 by 1024 pixels and 200 ms frame combining" width="800">

### 3.3 Choose the shutter

- [ ] **Pick pre-specimen or post-specimen shutter**

  1. Choose the **pre-specimen** shutter to block the beam before it reaches the sample. This protects beam-sensitive samples between exposures.
  2. Choose the **post-specimen** shutter (a projection blanker) to block the beam after the sample. This controls exposure on the camera without changing illumination on the sample.

     <img src="img/p1_setup_07.jpg" alt="Velox shutter selection panel with pre-specimen and post-specimen options" width="800">

### 3.4 Choose the recording mode

- [ ] **Pick the recording mode that matches the experiment**

  1. Choose **Auto Stop** to record a fixed number of frames and then halt. This is the default for still imaging.
  2. Choose **Circular** to keep the most recent N frames in a rolling memory buffer; pressing stop preserves whatever is in the buffer. This is useful for in-situ experiments where the moment of interest is unpredictable.
  3. Choose **Continuous** to save every frame for the full duration of the recording.

     <img src="img/p1_setup_08.jpg" alt="Velox recording mode selector showing Auto Stop, Circular, and Continuous options" width="800">

### 3.5 Open the column status bar

- [ ] **Show the column status bar during acquisition**

  1. Open the column status bar so the beam state, vacuum, and stage coordinates remain visible during acquisition.

     <img src="img/p1_setup_09.jpg" alt="Talos column status bar showing live beam state, vacuum, and stage coordinates" width="800">

## Part 4: Bright-field imaging

### 4.1 Open the column valves

- [ ] **Open the column valves once vacuum is green**

  1. Open the column valves from the Talos UI.

     <img src="img/p4_bf_10.jpg" alt="Velox view immediately after opening the column valves, with beam reaching the sample" width="800">

### 4.2 Drop to low magnification to find the feature of interest

- [ ] **Navigate at ~25x magnification**

  1. Drop the magnification to roughly 25x using the magnification knob.
  2. Move the stage to a feature of interest using the trackball.

     <img src="img/p4_bf_11.jpg" alt="Low-magnification view at approximately 25 times used for stage navigation" width="800">

### 4.3 Set the illumination

- [ ] **Use the intensity knob to spread or condense the beam**

  1. Turn the intensity knob until the illumination on the sample is uniform and the histogram fills the dynamic range without saturating.

### 4.4 Acquire and annotate

- [ ] **Acquire and annotate a bright-field image**

  1. Acquire an image with the chosen camera.
  2. Use the `Velox` annotation tool to label features, mark positions, or add scale annotations.

     <img src="img/p4_bf_12.jpg" alt="Velox annotation toolbar in use on a bright-field image" width="800">

     <img src="img/p4_bf_13.jpg" alt="Bright-field image with annotation overlay" width="800">

     <img src="img/p4_bf_14.jpg" alt="Bright-field image at intermediate magnification" width="800">

     <img src="img/p4_bf_15.jpg" alt="Bright-field image after annotation, ready to save" width="800">

## Part 5: Dark-field imaging

### 5.1 Switch the multi-function knob to beam tilt

- [ ] **Set mulXY to beam tilt mode**

  1. Switch the multi-function knob (`mulXY`) so that it controls beam tilt rather than stage motion. Beam tilt is the mechanism used to align a chosen diffraction spot onto the optical axis for dark-field imaging.

     <img src="img/p5_df_16.jpg" alt="Talos hand panel showing the multi-function knob set to beam tilt mode" width="800">

### 5.2 Enter dark-field mode

- [ ] **Press the dark-field button**

  1. Press the dark-field button on the hardware panel to enter dark-field mode.

     <img src="img/p5_df_17.jpg" alt="Talos console with the dark-field mode indicator illuminated" width="800">

### 5.3 Tilt the beam to align a diffraction spot

- [ ] **Align the chosen Bragg reflection onto the optical axis**

  1. Tilt the beam with the multi-function knob until the chosen diffraction spot sits on the optical axis. In diffraction mode, the central beam and the selected Bragg reflection swap positions when dark-field mode is toggled on.

     <img src="img/p5_df_18.jpg" alt="Diffraction pattern with the selected Bragg spot tilted onto the optical axis for dark-field imaging" width="800">

### 5.4 Compare bright-field and dark-field images

- [ ] **Acquire matched BF and DF images of the same area**

  1. Acquire a bright-field reference image first.

     <img src="img/p5_df_19.jpg" alt="Bright-field image of the sample area before switching to dark field" width="800">

  2. Switch back into dark-field mode, leave diffraction mode, and retract the selected-area aperture.
  3. Acquire the dark-field image.

     <img src="img/p5_df_20.jpg" alt="Dark-field image of the same sample area showing inverted contrast" width="800">

     > **NOTE:** Contrast is inverted between BF and DF: grains that diffracted strongly into the selected reflection now appear bright against a dark background.

## Changelog

- May 11, 2026 : Moved the underfocus/overfocus reference into [Session notes](../notes.md) since it is session-specific rather than part of the general BF/DF procedure.
- May 11, 2026 : Initial draft compiled from the April 2026 Talos sessions by @bobleesj. BF and DF procedure structure adapted from the existing Phenom Pharos SOP layout.
