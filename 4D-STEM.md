# 4D-STEM

This guide covers the setup and operation of 4D-STEM data acquisition using the
Arina detector.

Here is the Dectris Arina hardware within Spectra.

<img src="img/4D-STEM/spectra.jpg" alt="Spectra instrument main" width="500">

<img src="img/4D-STEM/arina-hardware.jpg" alt="Dectris hardware" width="500">

## Part 1: Detector setup

1. **Open the detector**
   - Open the column and go to the Arina detector
   - Press the button (with blue light) for 10 seconds, then it will open

2. **Remote computer connect**
   - Click the remote connection icon, then enter `192.168.12.73`

   <img src="img/4D-STEM/01-remote-connection.jpg" alt="Remote connection" width="500">

3. **Software in remote computer**
   - Open the Firefox browser → Initialize detector
   - CETA needs to be out. Click on the CETA icon to insert/remove CETA.

   <img src="img/4D-STEM/02-detector-initialization.jpg" alt="Detector initialization" width="500">

4. **How to save file**
   - Go to the detector software: click on "Save Images" and choose folder
   - Click on "Continuous" to check the image
   - When everything is good, click on "Single" to record and save
   - Note: `(name)_%00%` cannot be deleted, otherwise the file cannot be saved
     correctly

   <img src="img/4D-STEM/03-save-images-dialog.jpg" alt="Save images dialog" width="500">

## Part 2: Beam configuration

5. **Go to STEM**
   - Click on **Descan**

6. **Beam setting**
   - Go to "Beam Setting", click on "MF-Y Convergence Angle"
   - This is used for tuning the convergence angle of the beam

   <img src="img/4D-STEM/04-beam-settings.jpg" alt="Beam settings" width="500">

7. **Adjust aperture and convergence angle**
   - C2 aperture: Change from 70 → 50
   - Convergence angle: Use Multifunction Y to adjust to 10 mrad (1/5
     relationship with C2. If C2 is 70, convergence angle should be 14 mrad)
   - Click on "MF-Y Convergence Angle" to close

   <img src="img/4D-STEM/05-aperture-view.jpg" alt="Aperture view" width="500">
   - Remove other apertures
   - C3 aperture: Change from 1000 → 30 (you can use C2 at 50 to check if C3 is
     centered)
   - Adjust current: Go to Mono, click on "Focus", use the Intensity knob to
     adjust the current to ~0.032 nA

8. **Camera length**
   - Set camera length to **230 mm** or **285 mm**, depending on your needs

9. **Retract HAADF**
   - Click on "HAADF" to take the HAADF detector out

## Part 3: Acquisition

10. **Insert detector**
    - Press the "Insert" button to insert the detector

    <img src="img/4D-STEM/06-insert-detector.jpg" alt="Insert detector" width="500">
    - Press "EDS Scan" to see things (from "INT Scan")
    - Do not forget to press the "R1" button so the detector can work

    <img src="img/4D-STEM/07-eds-scan.jpg" alt="EDS scan" width="500">

11. **Acquisition**
    - Click on **Scan** → **Continuous** to check
    - Center the main spot
    - If it is OK, click on "Stop", then click on "Single Scan" to obtain data

12. **Analysis software (EIS)**
    - Click on "Rebin", "Reprocess" – you can use the software to do a simple
      analysis.

## Part 4: Finish

13. **Finish**
    - Retract the detector: Press "Retract"
    - Press "INT Scan"
    - Close the detector: Go to the Arina detector and press the button (with
      blue light) for 10 seconds. It will close and the light will turn off.

    <img src="img/4D-STEM/08-detector-close.jpg" alt="Detector close" width="500">

## FAQs

<details>
<summary>Why use 50 µm C2 aperture instead of 70 µm?</summary>

The smaller 50 µm aperture provides better coherence and a more defined probe,
which is important for 4D-STEM where you need clean diffraction patterns at each
probe position.

</details>

<details>
<summary>What does the 10 mrad convergence angle mean?</summary>

The convergence semi-angle determines how focused your probe is and affects the
size of the diffraction disks in your CBED pattern. 10 mrad is a common choice
that balances probe size with disk separation in the diffraction pattern.

</details>

<details>
<summary>Why 230 mm camera length?</summary>

This camera length positions the diffraction pattern appropriately on the
detector, ensuring the relevant diffraction information (Bragg disks) falls
within the detector area while maintaining good angular resolution.

</details>

## Changelog

- Dec 10, 2025 - First draft and images shared by Guoliang Hu
