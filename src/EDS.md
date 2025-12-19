# EDS

> [!CAUTION]
> **VERY ROUGH DRAFT** - These notes were recorded during training. This document will be updated with more detailed steps and images.

> TODO:
> - [ ] Add step-by-step images for TEM mode
> - [ ] Clarify STEM mode beam settings
> - [ ] Add screenshots for drift correction setup

This guide covers Energy Dispersive X-ray Spectroscopy (EDS) on the Spectra 300.

> **Prerequisite:** Complete the [STEM alignment](STEM.md) procedure before starting.

**Acronyms:**

- `EDS` - Energy Dispersive X-ray Spectroscopy
- `SI` - Spectrum Imaging

## Part 1: TEM mode EDS

1. **Select area**

   - Select the area of interest on your sample

2. **Open EDS**

   - Click on the EDS icon in Velox

     <img src="img/EDS/EDS-velox-eds-spectrum.jpg" alt="Velox EDS spectrum view" width="500">

3. **Check experiment log**

   - Review the experiment log for acquisition parameters

## Part 2: STEM mode EDS

1. **Set beam parameters**

   - Go to `Beam Setting` → `Probe` → click on `MF-Y`
   - Change convergence angle to 10 mrad (larger area to focus)
   - Increase screen current to 0.4 nA

2. **Start spectrum imaging**

   - Go to `SI` (Spectrum Imaging)
   - Click on the rectangle selection tool
   - Select an area on the sample

     <img src="img/EDS/EDS-stem-area-scan.jpg" alt="STEM EDS area scan" width="500">

   - For nanoscale resolution, choose 20 microsecond dwell time

3. **Set drift correction**

   - Click on `Drift Area` to enable drift correction

   > FIXME: add image for drift area selection

4. **Adjust parameters**

   - Use `Object Properties` to change acquisition parameters

5. **Acquire data**

   - Wait until pixel count stabilizes (watch for 8 pixel indicator)

     <img src="img/EDS/EDS-pixel-wait.jpg" alt="Pixel count indicator" width="500">

   - Stop recording when complete

## Part 3: Data processing

1. **Draw line profile**

   - Go to `Processing` to draw a line profile across features

     <img src="img/EDS/EDS-processing-line.jpg" alt="EDS processing line profile" width="500">

2. **Select arbitrary area**

   - You can also select an arbitrary area for analysis

3. **Atomic mapping**

   - For atomic resolution mapping, use Average or Gaussian filtering

     <img src="img/EDS/EDS-atomic-mapping.jpg" alt="EDS atomic mapping" width="500">

   - Use highest frequency and edge smoothing settings to obtain atomic resolution

## Changelog

- Dec 18, 2025 - Tutorial drafted by Guoliang Hu and @bobleesj
