# EDS

> [!CAUTION]
> **VERY ROUGH DRAFT** - @bobleesj and Guoliang Hu took notes and pictures during training. This document will be updated with more detailed steps and images.

This guide covers Energy Dispersive X-ray Spectroscopy (EDS) on the Spectra 300. EDS identifies elements in a sample by detecting characteristic X-rays emitted when the electron beam knocks out inner-shell electrons. This guide uses the standard gold nanoparticle sample, so Au (gold) is the primary element expected in the elemental maps and spectra.

> **Prerequisite:** Complete the [STEM alignment](../spectra_STEM/index.md) procedure before starting.

**Acronyms:**

- `EDS` - Energy Dispersive X-ray Spectroscopy
- `SI` - Spectrum Imaging

## Overview

| Phase | Procedures | Time |
| ----- | ---------- | ---- |
| [Part 1: STEM mode EDS](#part-1-stem-mode-eds) | Set beam parameters, select imaging area, drift correction, acquire and process data | 15-30 min |

## Part 1: STEM mode EDS

### 1.1 Set beam parameters (optional)

- [ ] **Adjust convergence angle and beam current**

  1. In `TEMUI`, go to `Beam Settings`, select `Probe`, then click `MF-Y`
  2. Change convergence angle to approximately 21.5 mrad for EDS. A larger convergence angle focuses more current onto the sample, increasing the X-ray count rate.
  3. Increase screen current to ~0.4 nA. Higher beam current generates more X-rays but also increases sample damage. To adjust beam current, see [Monochromator tune](../spectra_STEM/index.md#16-monochromator-tune) in the STEM guide.

### 1.2 Select spectrum imaging area

- [ ] **Define acquisition area**

  1. In `Velox`, click `Spectrum Imaging Area` as shown below

     <img src="img/p2_s1_eds_toolbar_01.jpg" alt="Velox toolbar with Spectrum Imaging Area selected" width="800">

  2. Draw a rectangle on the HAADF image to define the area for EDS acquisition

     <img src="img/p2_s2_area_select_01.jpg" alt="Selecting spectrum imaging area on HAADF image" width="800">

- [ ] **Set drift correction**

  1. Click `Drift Area` in the toolbar. A tooltip appears: "Draw the drift measurement area."

     <img src="img/p2_s3_drift_area_01.jpg" alt="Drift Area tooltip in Velox" width="800">

  2. Draw a small rectangle near a high-contrast feature. The system uses this region to track and correct specimen drift during acquisition.

     <img src="img/p2_s3_drift_draw_02.jpg" alt="Drawing drift measurement area on sample" width="800">

  3. Verify both the spectrum image area (green rectangle) and drift area (white rectangle) are visible on the HAADF image.

     <img src="img/p2_s3_drift_complete_03.jpg" alt="Spectrum image area and drift area both selected" width="800">

### 1.3 Acquire and process data

- [ ] **Start acquisition**

  1. Click `Spectrum Imaging` to start acquisition. The tooltip shows the dwell time per pixel.

     <img src="img/p2_s4_acquire_01.jpg" alt="Spectrum Imaging start button with dwell time 2.00 µs" width="800">

  2. Let the acquisition run for several frames so the software accumulates enough signal. Then click `To Spectrum` and `Auto ID` in the `Periodic Table` panel to identify elements from the spectra collected so far. You may also select elements manually if auto detection does not work.

     > **TODO:** Verify whether you need both `To Spectrum` and `Auto ID`, or just one of them.

- [ ] **Review elemental maps**

  1. Select a rectangular area on the HAADF image for map processing

     <img src="img/p3_s1_map_processing_02.jpg" alt="Selecting area for map processing in Velox" width="800">

  2. The `Image Browser` panel displays elemental maps for each detected element. Use the `Display Settings` on the right to toggle between intensity (int), net counts (net), weight percent (wt%), and atomic percent (at%) views.

     <img src="img/p3_s3_elemental_maps_01.jpg" alt="Velox Image Browser with elemental maps and FFT display" width="800">

  3. The `Integrated Spectra` panel below shows the X-ray spectrum from the selected area. The `Periodic Table` panel identifies detected elements. Under `Object Properties`, verify the acquisition parameters (image size, pixel size, field of view, dwell time).

     <img src="img/p3_s2_spectrum_02.jpg" alt="Integrated spectrum with periodic table showing Au and Co elements" width="800">

  4. Elemental maps show spatial distribution of each element. In this example, N (green/yellow), O (red), and Au (purple) maps are displayed.

     <img src="img/p3_s3_elemental_maps_02.jpg" alt="Elemental maps showing N, O, and Au distributions" width="800">

## End session

Follow the steps in [End session](../spectra_STEM/index.md#end-session) from the Spectra STEM guide.

## Acknowledgments

Thank you to Cedric Lim for teaching @bobleesj the EDS workflow during his session. Images captured during his session.

## Changelog

- Apr 3, 2026 - Replace images with new photos captured by @bobleesj during EDS training by Cedric Lim
- Dec 18, 2025 - Initial rough draft by Guoliang Hu and @bobleesj
