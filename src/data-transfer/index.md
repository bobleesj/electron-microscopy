# Data transfer: Arina and Velox

This page covers how to save your data to a USB drive at Stanford SNSF: Arina 4DSTEM datasets (reached through the lab Mallard network share) and Velox HAADF `.emd` images (saved locally on the control workstation). Drafted by Sangjoon Bob Lee from staff notes and images.

## Overview

| Data | How to reach it |
| ---- | --------------- |
| [Arina 4DSTEM datasets](#save-arina-4dstem-data-to-usb) | Mallard network share → USB |
| [HAADF images (`.emd`)](#save-haadf-images-to-usb) | Velox `CaptureData` folder → USB |

## Save Arina 4DSTEM data to USB

The Arina detector writes 4DSTEM data to the lab Mallard server. Map it as a network drive, then copy your dataset to your USB drive.

- [ ] **Plug your USB into the Arina PC**

  1. Plug your USB drive into the computer below (the TVIPS scan generator PC). The USB port is circled.

     <img src="img/IO-arina-pc-usb-port.jpg" alt="Arina TVIPS PC with USB port circled" width="400">

- [ ] **Open Map network drive**

  1. In Windows File Explorer, right-click `This PC` and select `Map network drive...`.

     <img src="img/IO-map-network-drive-menu.jpg" alt="Right-click This PC showing Map network drive option" width="500">

- [ ] **Enter the share path**

  1. Set `Drive` to `Z:` and `Folder` to `\\mallard.stanford.edu\mallard_arina`.
  2. Check `Reconnect at sign-in`, then click `Finish`.
  3. Enter the Mallard password when prompted. The password is in the pinned channel of the Colin Ophus group internal Slack.

     <img src="img/IO-map-network-drive-dialog.jpg" alt="Map Network Drive dialog with mallard_arina path and drive Z" width="500">

- [ ] **Copy your dataset to USB**

  1. Open the mapped `Z:` drive, find your session's 4DSTEM dataset, and copy it to your USB drive.

## Save HAADF images to USB

Velox saves HAADF images and other `.emd` files locally on the control workstation. Copy them straight to a USB drive.

- [ ] **Plug in the USB drive**

  1. Insert your USB drive into the PC. It appears as a new drive in File Explorer.

     <img src="img/IO-usb-plug-in.jpg" alt="USB drive plugged into the control workstation" width="500">

- [ ] **Find the CaptureData folder and copy**

  1. Open the `CaptureData (X:)` folder. Velox saves your session's `.emd` files here, organized by date.
  2. Copy your dated folder to the USB drive.

     <img src="img/IO-capturedata-folder.jpg" alt="CaptureData folder with Velox emd files" width="500">
