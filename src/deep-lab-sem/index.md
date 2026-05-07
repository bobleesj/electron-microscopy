****# Phenom Pharos G2 SEM/STEM (Deep Lab)

<img src="img/p0_phenom_pharos_overview.jpg" alt="Phenom Pharos monitor showing the settings panel overlaid on live SEM images of Sn ball samples" width="800">

> [!CAUTION]
> **VERY ROUGH DRAFT** - Notes and photos recorded by @bobleesj during TA session with Ash on Apr 16, 2026. Based on the Theme 1C "Imaging Basics on the Phenom" lab walkthrough. The goal of this guide is to help you operate the Phenom Pharos in the future, not to reproduce the lab exercise. Steps and screenshots still need verification.
>
> **TODO:** Further verify every step against the actual instrument. Add screenshots for tuning buttons (autofocus, autoCB, autostigmate) and the accelerating voltage / detector / vacuum selectors.

This guide covers operating the Phenom Pharos G2 desktop SEM/STEM in the Deep Lab at Stanford. The Phenom Pharos is a desktop-sized field-emission SEM that also supports STEM imaging through a swappable holder. It is fast to start up (no pump-down wait like the Spectra), and the UI is simple enough that a new user can be imaging within a few minutes.

**Links:**

- [Thermo Fisher Phenom Pharos product page](https://www.thermofisher.com/us/en/home/electron-microscopy/products/desktop-scanning-electron-microscopes/phenom-pharos.html)
- [SNSF Phenom Pharos reservation page](https://snsf.stanford.edu/opportunities/phenom-pharos)

**System specifications:**

<img src="img/p0_settings_menu_options.jpg" alt="Phenom top menu options panel showing System (Acc Voltage, Beam Intensity, Detector, Vacuum), Live and Acquisition settings" width="800">

The acquisition settings panel shows what is available: accelerating voltage (5/10/15/20 kV or custom), beam intensity (Low/Image/Point/Map/Custom), detector (BSD Full, BSD Top, SED, or 4A+BSD+SED), and vacuum (High 0.1 Pa, Medium 10 Pa, Low 60 Pa).

| | |
|---|---|
| Model | Phenom Pharos G2 Desktop FEG-SEM |
| Source | Schottky field emission |
| Sample size | 25 mm max diameter |
| Resolution | SED: 2 nm, STEM: <1 nm |
| Detectors | SED, BSD (BSE), BSD-TOPO, EDS, STEM (BF, DF, HAADF) |
| Acceleration voltage | 1 to 20 kV |
| Vacuum | 0.1 Pa, 1 Pa, 60 Pa (low/medium/high) |
| Footprint | 925 × 305.6 × 343.5 mm, 83.8 kg |

**Acronyms:**

- `SEM` - Scanning Electron Microscopy (surface imaging)
- `STEM` - Scanning Transmission Electron Microscopy (thin-sample imaging)
- `SED` - Secondary Electron Detector (surface topography)
- `BSD` / `BSE` - Backscattered Electron Detector (atomic number contrast)
- `BF` / `DF` / `HAADF` - Bright Field / Dark Field / High-Angle Annular Dark Field (STEM modes)
- `autoCB` - Auto Contrast-Brightness
- `WD` - Working Distance
- `FW` - Field Width

**Example images produced by the Phenom Pharos:**

- *Secondary electron image of tin on carbon standard* (SED mode)
- *STEM bright field image of rubber sample* (BF STEM mode)

## Overview

| Phase | What it covers | Time |
| ----- | ---------- | ---- |
| [Part 1: Loading a sample](#part-1-loading-a-sample) | Prepare sample on stub puck, insert into drawer | 5 min |
| [Part 2: Transfer to SEM](#part-2-transfer-to-sem) | Optical overview, set accelerating voltage, move to SEM | 2-3 min |
| [Part 3: Imaging and tuning](#part-3-imaging-and-tuning) | Pick magnification, autofocus/autoCB/autostigmate, acquire images | varies |
| [Part 4: Maps software for large-area tiles](#part-4-maps-software-for-large-area-tiles) | Switch to Maps software, set up a tile series | 5-15 min |
| [Part 5: STEM mode](#part-5-stem-mode) | Swap to STEM holder, load a TEM grid, image in BF/DF/HAADF | 15-30 min |
| [Part 6: End session](#part-6-end-session) | Save images, unload sample, hand off | 5 min |


## Part 1: Loading sample

### 1.1 Unload sample

- [ ] **Eject and open the drawer**

  1. Put on nitrile gloves before handling any sample or holder.
  2. In the software, click the eject icon (triangle in the left sidebar) to vent the chamber. Wait for the vent cycle to finish.
  3. Pull the bottom drawer on the front of the Phenom Pharos G2 open.

     <img src="img/p1_s1_drawer_open_01.jpg" alt="Opening the sample loading drawer on the Phenom Pharos G2" width="800">

- [ ] **Remove the existing stub**

  1. The previous user's stub puck is seated in the drawer. Lift it out by the black handle.

     <img src="img/p1_s1_drawer_stub_holder_02.jpg" alt="Previous sample stub holder seated inside the open drawer" width="800">

  2. Gently pull it out

     <img src="img/p1_s1_stub_holder_removed_03.jpg" alt="Previous sample stub puck holder removed from the Phenom" width="800">

- [ ] **Remove the old sample**

  1. Use a tweezer to pick the previous sample off the stub.

     <img src="img/p1_s2_remove_old_01.jpg" alt="Tweezers lifting the previous sample off the stub puck" width="800">

  2. Lift the sample clear of the stub. The stub center is now empty.

     <img src="img/p1_s2_remove_old_02.jpg" alt="Previous sample removed, stub center now empty" width="800">

  3. Place the old sample aside on the bench. You can return it to its storage tube at the end of the session.

     <img src="img/p1_s2_open_new_tube.jpg" alt="Tweezers reaching into the orange-capped storage tube to retrieve the new sample" width="800">

### 1.2 Load your sample

- [ ] **Get your new sample from its orange tube**

  1. Locate the orange-capped storage tube labeled with your sample name (for example, `Cu braid`).
  2. Uncap the tube and use the tweezer to reach for your new sample inside.

  3. Lift the new sample out of the tube by its edge.

     <img src="img/p1_s2_lift_new_sample.jpg" alt="Lifting the new copper sample out of the orange-capped storage tube with tweezers" width="800">

- [ ] **Bring the sample to the stub**

  1. With the stub empty in hand, position the new sample above the stub center.

     <img src="img/p1_s2_new_sample_on_bench.jpg" alt="Empty stub puck held in hand with new copper sample ready to be placed" width="800">

- [ ] **Place and secure the sample**

  1. Lower the sample onto the center of the stub.
  2. If needed, press down firmly with your thumb to secure the sample against the stub.

     <img src="img/p1_s2_press_down_thumb.jpg" alt="Pressing the copper wire sample down onto the stub with the thumb to secure it" width="800">

- [ ] **Verify the mounted sample**

  1. Hold the stub up and inspect from the side. The sample must sit **below** the metal rim and be centered.

     <img src="img/p1_s2_cu_wire_seated_02.jpg" alt="Inspecting the mounted copper wire sample on the stub, held up for verification" width="800">

     > **CRITICAL:** If the sample sticks above the rim, it will hit the pole piece when the stage raises. Flatten or reseat before inserting.

### 1.3 Insert and close the drawer

  1. Lift up the drawer and insert the stub. The Phenom begins pumping down automatically. The front display shows a loading animation while pumping. Wait for pumping to complete before proceeding.

     <img src="img/p1_s3_drawer_closed_03.jpg" alt="Phenom Pharos with drawer closed showing loading animation on front display" width="800">

## Part 2: Transfer to SEM

### 2.1 View the optical overview

When the drawer closes and pumping completes, the Phenom starts in **optical mode**. You see the sample through the loading camera, not the electron beam yet.

> **NOTE:** The mouse scroll wheel behaves differently in each mode:
> - **Optical mode (first load):** scroll adjusts optical **focus**.
> - **SEM mode (after "Move to SEM"):** scroll adjusts **magnification**.
>
> Don't expect to zoom with the wheel until you move to SEM.

- [ ] **See the optical camera view**

  1. The software shows the optical view of your sample from the loading camera. Use this to get a rough idea of where your features are on the stub.

     <img src="img/p2_s1_optical_view_01.jpg" alt="Optical camera view of Cu braid sample on the monitor" width="800">

  2. Scroll the mouse wheel to focus the optical camera. The optical view is useful for orientation but cannot resolve fine features.

     <img src="img/p2_s1_optical_view_focused_02.jpg" alt="Focused optical view of the sample" width="800">

### 2.2 Set the save path and file naming

- [ ] **Configure acquisition settings**

  1. Click the gear icon in the left sidebar to open `Settings`.
  2. Go to `Customize` → `Acquisition`. Set the `Label` (for example, `Cu_sample`) and the `Location` path (typically `C:\Users\Phenom\Pictures\...\session N`).
  3. The filename format will automatically include label, kV, magnification, detector, pressure, and date.

     <img src="img/p2_s2_settings_customize.jpg" alt="Acquisition settings dialog showing label, location, and filename format" width="800">

### 2.3 Move to SEM

- [ ] **Transfer sample to the electron beam**

  1. In the left sidebar, hover to reveal the `Move to SEM` button. Click it to transfer the sample from the optical camera to the SEM beam.

     <img src="img/p2_s3_press_sem_mode.jpg" alt="Move to SEM button in the left sidebar of the Phenom software" width="800">

  2. A progress indicator appears showing `Moving to SEM`. This takes about 15 seconds.

     <img src="img/p2_s3_moving_to_sem.jpg" alt="Moving to SEM progress indicator at 35%" width="800">

  3. Set the accelerating voltage to a starting value (5 kV is a safe default for most samples).

     > **NOTE:** Higher kV (20 kV) gives better signal from BSE but more beam penetration. Lower kV (5 kV) is better for surface imaging and beam-sensitive samples.

## Part 3: Imaging and tuning

### 3.1 Find an intermediate magnification

- [ ] **Navigate the sample**

  1. Scroll the mouse wheel to zoom in and out. Find a magnification that feels "intermediate" for your features (usually 1,000x to 10,000x to start).
  2. Drag on the image to translate the stage. Features come into view as the stage moves.

     <img src="img/p3_s1_sem_image_with_controls.jpg" alt="SEM image with imaging controls panel showing Magnification, Focus, Contrast, Brightness, Rotation, Gamma" width="800">

     > The right panel shows `Imaging controls`: magnification slider, focus, contrast, brightness, rotation, gamma, and an invert toggle. Most of these you adjust by the auto buttons, not manually.

### 3.2 Tune the beam (the three auto buttons)

The Phenom has three auto-tuning buttons in the lower left corner. Use them in order every time you change kV, change detector, or move to a new region.

> **TODO for me to investigate: when to use auto vs. manual?** The auto buttons handle most cases, but there are specific situations where you need to override them manually. Figure out:
> - When does `Autofocus` fail and require manual focus? (e.g., low-contrast regions, very flat samples)
> - When is manual stigmator adjustment better than `Autostigmate`? (e.g., atomic-resolution tuning, asymmetric features)
> - When do you turn off `autoCB` and set contrast/brightness manually? (e.g., comparing images across pressures, where the PDF says "leave autoCB alone" during the pressure series)
> - How does automatic scanning (tile series auto-positioning, auto-focus per tile) behave and when does it need manual correction? This is a known weak area to investigate in future sessions.

- [ ] **Run autofocus, autoCB, autostigmate**

  1. Click `Autofocus` first. The system wobbles focus and settles on the sharpest value.
  2. Click `Auto contrast-brightness` (`autoCB`). This normalizes the detector signal to fill the histogram.
  3. Click `Autostigmate`. This corrects beam astigmatism (round beam shape).

     > **NOTE:** Every time you change kV, rerun all three. When you only change detectors, autoCB is usually enough.

### 3.3 Acquire an image

- [ ] **Save an image**

  1. Set the `Scan size` and `Dwell time` in the acquisition panel. `1920x1080` at `Medium` scan is a good default for quick imaging.
  2. Click the camera icon on the left sidebar to acquire. The system does a high-quality scan and saves the image to your path.

     > **NOTE:** Files are saved as `.tiff` with metadata (kV, magnification, detector, pressure, WD, date) embedded.

- [ ] **Review in the image viewer**

  1. Double-click a saved `.tiff` in Windows Explorer to open it in the Phenom Image Viewer. The right panel shows all acquisition properties.

     <img src="img/p3_s2_image_viewer_properties.jpg" alt="Phenom Image Viewer showing BSE image with properties panel" width="800">

### 3.4 Detectors and modes

Once the sample is loaded and you are in SEM mode, open the top menu options panel to pick your accelerating voltage, beam intensity, detector, vacuum, averaging, scan size, and dwell time. These are all the settings you will touch during a session.

<img src="img/p0_settings_menu_options.jpg" alt="Phenom top menu options panel with System (kV, beam intensity, detector, vacuum), Live, and Acquisition sections" width="800">

The Phenom Pharos supports multiple imaging modes. Switch between them from the `Detector` row in the settings panel.

| Mode | What it shows | When to use |
|---|---|---|
| `BSD Full` | Backscattered electrons, all angles | Atomic number contrast (Z-contrast), compositional differences |
| `BSD Top` | Backscattered, only top segment | Surface topography with Z-contrast |
| `SED` | Secondary electrons | Fine surface topography. Not available at high pressure. |
| `4A+BSD+SED` | Combined | Composite image |

Pressure affects which detectors are usable:

| Pressure | Use case |
|---|---|
| Low (0.1 Pa) | Best resolution. SED available. Default for most samples. |
| Medium (10 Pa) | Reduces charging on insulating samples. |
| High (60 Pa) | Use for heavily charging samples. SED not usable at this pressure. |

## Part 4: Maps software for large-area tiles (Optional)

> [!WARNING]
> **Part 4 is a placeholder.** The Maps software is powerful but deserves its own dedicated tutorial: project templates, tile stitching, auto-focus per tile, rotation alignment, stitched navigation, high-resolution drill-in, and handling of sparse samples. The notes below are a sketch from a single session.
>
> **TODO:** Write a full Maps walkthrough after more hands-on practice. Cover: template setup, optical → SEM transfer for tile planning, auto-focus behavior across tiles, rotation to match feature direction, nested high-resolution tile series, file organization of large datasets.

For mapping large areas (for example, a whole copper braid or the full width of a grid), switch to the `Maps` software for tile acquisition and stitching.

### 4.1 Open Maps and set up a tile series

- [ ] **Switch to Maps**

  1. Press the Windows key on the keyboard to minimize the Phenom software.
  2. Launch `Maps` (Thermo Scientific).
  3. Create a new project. Set a template (Factory Template is fine for a first pass).

- [ ] **Configure the tile series**

  1. In `Maps`, set the number of tiles (for example, 3x3 or 4x4 to start).
  2. Set the tile HFW (horizontal field width), resolution (for example, 1920x1080), averaging, contrast, and brightness.
  3. Position and rotate the tile grid over the region of interest on your optical overview.

     <img src="img/p4_s1_maps_tile_setup.jpg" alt="Maps software with tile series grid positioned over sample" width="800">

### 4.2 Run the tile series

- [ ] **Acquire tiles**

  1. Click `RUN` at the bottom. `Maps` takes over the microscope and acquires each tile.
  2. A progress bar shows remaining time (for example, "4 of 16 images acquired, 1.43 GB").

     <img src="img/p4_s2_maps_running_tiles.jpg" alt="Maps software acquiring tile series of Cu braid with progress indicator" width="800">

  3. After all tiles are acquired, `Maps` automatically stitches them into a single stitched layer.

- [ ] **Drill into a region**

  1. Use the stitched map to navigate to an area of interest.
  2. Set a smaller, higher-resolution tile series on top of the first to map that area at finer detail. Keep the second series small to avoid a long acquisition (aim for 3-5 min).

## Part 5: STEM mode (Optional)

STEM imaging requires swapping to the STEM holder, which has a segmented transmission detector built into the stub. The holder takes a standard 3 mm TEM grid on top.

### 5.1 Swap to the STEM holder 

- [ ] **Retrieve the STEM holder**

  1. Unload the current sample (see [Part 6](#part-6-end-session)).
  2. Take the STEM holder out of its storage case. The STEM holder has a circular transmission detector window in the center of the stub.

     <img src="img/p5_s1_stem_holder_bench.jpg" alt="STEM holder on the bench showing segmented transmission detector" width="800">

     > **NOTE:** The STEM holder itself contains the BF/DF/HAADF segmented detectors. The grid sits on top of the detector, and transmitted electrons pass through the grid and hit the segmented detector below.

### 5.2 Load a TEM grid

- [ ] **Place the grid, blue side down**

  1. Use fine-tip tweezers to pick up the TEM grid by the edge.
  2. Lower the grid into the holder slot with the **blue side facing down**. The sample side faces up toward the beam.

     <img src="img/p5_s2_load_grid_tweezers_01.jpg" alt="Loading TEM grid into STEM holder with tweezers, blue side down" width="800">

  3. Seat the grid flat so it does not shift during pumping.

     <img src="img/p5_s2_load_grid_place_02.jpg" alt="TEM grid seated flat in the STEM holder" width="800">

- [ ] **Add the washer and close**

  1. Place the washer on top of the grid to secure it in the holder.
  2. Close the retaining cap.

     <img src="img/p5_s2_stem_holder_assembled.jpg" alt="STEM holder assembled with grid and washer in place" width="800">

### 5.3 Insert the STEM holder

- [ ] **Load into the Phenom**

  1. Place the STEM holder into the drawer the same way as a regular stub.
  2. Close the drawer. The green LED on the inside confirms the holder is seated correctly.

     <img src="img/p5_s3_stem_holder_loaded_green.jpg" alt="STEM holder inserted with green LED indicator lit" width="800">

### 5.4 Switch to STEM imaging

- [ ] **Enter BF STEM mode**

  1. Once pumping completes and the sample moves to the SEM, the system defaults to BSE Full. Switch to 5 kV.
  2. Zoom into one of the dark grid squares until the Cu grid bars are no longer visible.
  3. In the detector selector, switch to `BF STEM` mode.
  4. Run autoCB, autofocus, and autostigmate in that order.

- [ ] **Compare detectors**

  1. Cycle through `BF STEM`, `DF STEM`, and `HAADF STEM` to compare contrast mechanisms on the same region. Run autoCB each time you switch detector.

     > **When to use each STEM mode:**
     > - `BF STEM`: absorption contrast, shows thickness variations. Good for polymers, biological samples.
     > - `DF STEM`: diffraction contrast, shows crystalline grains.
     > - `HAADF STEM`: Z-contrast, heavier atoms appear brighter. Good for nanoparticles.

## Part 6: End session

- [ ] **Save and back up images**

  1. Verify all images are saved to your session folder. Check the filename format includes sample label, kV, magnification, detector, pressure, and date so you can identify them later.

     <img src="img/p6_file_organization.jpg" alt="Windows file explorer showing saved Phenom images organized by session" width="800">

  2. Copy the folder to external storage or a network drive before leaving.

- [ ] **Unload the sample**

  1. In the software, click the eject icon (triangle in the left sidebar) to vent the chamber. Wait for the vent cycle to complete.
  2. Open the drawer and remove the stub or STEM holder.pressure.

- [ ] **Return to storage**

  1. Return the stub puck holder and STEM holder to their storage locations.
  2. Close the drawer empty to protect the chamber.

- [ ] **Hand off**

  1. Log the session in the booking/logbook as required by lab rules.
  2. Wipe down the bench and return gloves/tweezers to their locations.

## Acknowledgments

Thank you to TA Ash for running the Phenom Pharos lab walkthrough on Apr 16, 2026. Photos captured during the session by @bobleesj.

## Changelog

- Apr 16, 2026 - Initial rough draft from Ash TA session and Theme 1C lab PDF by @bobleesj
