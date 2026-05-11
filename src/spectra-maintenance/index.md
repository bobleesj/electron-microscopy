# Spectra 300 maintenance (DRAFT)

This page collects recovery and maintenance procedures specific to the Spectra 300 at Stanford SNSF. These are not part of normal acquisition but may be needed mid-session. Drafted by Sangjoon Bob Lee from staff-provided notes and images.

> [!CAUTION]
> This is a rough draft. Confirm each procedure with staff before relying on it.

## Overview

| Procedure | When to use | Time |
| --------- | ----------- | ---- |
| [Liquid nitrogen fill](#liquid-nitrogen-fill) | LN dewar reads low during session | 10-15 min |
| [Octagon recovery](#octagon-recovery) | `TEMUI` shows an Octagon vacuum error | 2-5 min |

## Liquid nitrogen fill

Refill the LN dewar from the portable nitrogen tank in the back room when the level drops. Wear cryo gloves — liquid nitrogen can cause severe cold burns.

> TODO: Confirm at what nitrogen level (%) staff want users to start a refill.

- [ ] **Check the nitrogen level**

  1. On the Spectra touch panel, check the `Nitrogen Level` readout. Refill when the level reads low.

     <img src="img/LN2-low-level-readout.jpg" alt="Spectra touch panel showing 14% nitrogen level" width="500">

- [ ] **Bring the portable tank into the Spectra room**

  1. The portable nitrogen tank is stored in the back room.

     <img src="img/LN2-portable-tank-back-room.jpg" alt="Portable nitrogen tank in the back room" width="500">

  2. Roll the tank to the sample-loading area inside the Spectra room.

     <img src="img/LN2-tank-positioned-spectra.jpg" alt="CRYO-CYL portable tank positioned next to the Spectra" width="500">

- [ ] **Put on cryo gloves**

  1. Cryo gloves and the transfer hose are stored near the sample-loading zone.

     <img src="img/LN2-cryo-gloves.jpg" alt="Cryo gloves and transfer hose at sample-loading area" width="500">

- [ ] **Connect the transfer hose**

  1. On the portable tank, identify the valve labeled `LIQUID`. The other valve is for gas — do **not** use it.

     <img src="img/LN2-liquid-valve.jpg" alt="LIQUID-labeled valve on the portable tank" width="500">

  2. Attach one end of the transfer hose to the `LIQUID` valve.

     <img src="img/LN2-connect-hose-tank.jpg" alt="Connecting transfer hose to LIQUID valve" width="500">

  3. Insert the other end of the hose into the fill port on the Spectra.

     <img src="img/LN2-connect-hose-spectra.jpg" alt="Inserting hose into the Spectra fill port" width="500">

- [ ] **Open the valve and fill**

  1. Open the `LIQUID` valve by turning the knob **counter-clockwise** (toward `OPEN`).

     <img src="img/LN2-valve-open-close.jpg" alt="REGO valve showing OPEN and CLOSE directions" width="500">

  2. Watch the Spectra touch panel `Nitrogen Level`. Stop at 80-85% to leave headroom for thermal expansion.

     <img src="img/LN2-filled-86percent.jpg" alt="Nitrogen level reading 86% after refill" width="500">

- [ ] **Close the valve and disconnect**

  1. Close the `LIQUID` valve by turning **clockwise** (toward `CLOSE`). Use the wrench stored on the dewar handle if the knob is iced over.

     <img src="img/LN2-disconnect-wrench.jpg" alt="Using wrench to close the LIQUID valve" width="500">

  2. Disconnect the hose from the Spectra fill port.

     <img src="img/LN2-disconnect-spectra.jpg" alt="Disconnecting hose from the Spectra fill port" width="500">

- [ ] **Return the tank**

  1. Roll the tank back to the back room. Lock it in place with the safety chain as shown.

     <img src="img/LN2-tank-returned-locked.jpg" alt="Portable tank returned to back room and chained" width="500">

## Octagon recovery

The Octagon vacuum gauge measures the sample-area pressure. If it goes out of range, `TEMUI` reports an error and the Octagon gauge may show `Disabled`. Run `Evaluate Column` and toggle the column ion getter pump (`IGPcl`) to bring it back.

- [ ] **Confirm the Octagon error**

  1. In `TEMUI`, open the `Vacuum (Supervisor)` panel. The Octagon row reads `Disabled` (or a high log value) when the gauge has tripped.

     <img src="img/OCT-octagon-disabled.jpg" alt="Vacuum Supervisor with Octagon Disabled" width="500">

  2. Open the error log to read the underlying message. Typical entries include `Vacuum Error: Octagon pressure is too high` or `Watchdog IGPco High`.

     <img src="img/OCT-error-log.jpg" alt="TEMUI error log with Octagon vacuum errors" width="500">

- [ ] **Run Evaluate Column**

  1. In `TEMUI`, open the vacuum overview and click `Evaluate Column`. The status changes to `Busy` and the action banner reads `Action started: Evaluate Column / Waiting for IGP to start`.

     <img src="img/OCT-evaluate-column.jpg" alt="Vacuum overview running Evaluate Column" width="500">

- [ ] **Toggle the column ion getter pump**

  1. In the same vacuum overview, click the `IGPcl` button (ion getter pump - column). The `IGPcl` indicator highlights while the pump cycles.

     <img src="img/OCT-igpcl-button.jpg" alt="IGPcl button highlighted in vacuum schematic" width="500">

- [ ] **Wait for recovery**

  1. Watch the `Vacuum (Supervisor)` panel. Status reads `Busy` while the system recovers and the Octagon log value drops.

     <img src="img/OCT-vacuum-busy.jpg" alt="Vacuum Supervisor Busy during Octagon recovery" width="500">

  2. Wait for the Octagon row to return to green. If it does not recover within a few minutes, escalate to staff.

  3. Once recovered, return to imaging and verify the beam is visible on the fluorescent screen.

     <img src="img/OCT-beam-restored.jpg" alt="Beam visible on fluorescent screen after Octagon recovery" width="500">


## Changelog

- May 11, 2026 - Initial draft of Octagon recovery and LN2 fill from staff notes by @bobleesj
