# Session notes

*by Sangjoon Bob Lee*

This is a working scratchpad for raw notes taken during microscopy training visits and sessions. Notes here capture practical tips, questions, and observations from hands-on time at the instrument. Over time, useful content gets refined and incorporated into the proper guide sections.

---

## MAPED experience at NCEM, Mar 2, 2026

I had a chance to join TEAM MAPED session at NCEM with Stephanie Ribet and Henry Bell.

### General STEM notes for aberration

- **LM mode warning:** In TEAM, LM mode isn't used generally. It turns off the aberration corrector, a set of multipole electromagnetic lenses (hexapoles, octupoles) that correct for spherical aberration. When switched back on, the corrector needs hours to restabilize both thermally (coils heat up, causing alignment drift from thermal expansion) and electromagnetically (currents must settle to precise values).
- **aberration knobs:** in the probe corrector software, manually fix and it can be faster since software can take a while. For example, Correct A1 (twofold astigmatism) and B2 (axial coma) by hand. (@bobleesj, verifiy this)
- Use the **stigmator button** on the hand panel, it makes the beam round.
- **C2 adjust** is used to make the beam concentric, by alinigng C2 aperture.
- **Rotation center:** don't care about the edges. Use a magnified image to see whether the features are pulsing out of the page.

### Sample loading and vacumm

- After loading a sample, watch PPL. It should go down to low 10⁻³ or 10⁻⁴.
- Octagon must be below 10 after sample loading.

### Finding sample ROIs

- In Spectra, you can switch between TEM and STEM modes and it's stable. On TEAM, this is not the case, so it's better to use **STEM at 5k mag** to navigate and find samples.
- Use **stage double-click** to move around.

### Zone axis

- Use **alpha and beta on the hand panel** to get an approximation, then go to Stage, flap out, and use alpha and beta for fine adjustment.
- Feel free to use camera length to make it easier to see. Ensure the ronchigram is symmetric.

### Convergence angle

- Change the convergence angle by changing the aperture.
- C2 for 70 µm aperture gives ~9 mrad max. For higher convergence, use another aperture.
- If you change the C2 aperture, the software may still display the old value (e.g., "20") because it doesn't know how to get to the new position. Click **"Adjust"** to move to the new aperture where it has the intended aperature like 10 micrometer bull's eye aperture.
- Then move C2 to ~30 (instead of 1,000) to block out other apertures. 

### Arina at NCEM

- **HAADF must be out** before you insert Arina. Verify on Digital Micrograph.
- **Shutdown order:** voltage can be turned off from the software. No need to physically turn it off unlike at SNSF.

### Colume valve must be closed even during a quick break

- Always set **column valve off** for lunch. It does not affect aberrations.

### Modify current

- To gain more current, go to **Focus and Shift** under the `Mono` tab. This controls the monochromator lens excitation, which determines how tightly the beam is focused at the energy-selecting slit. Lowering focus means a less tight crossover at the slit, so more electrons pass through.

### Descan pivot point

- TODO: needs definition and procedure.

### TODOs

- [ ] Investigate the effect of descan when you integrate or sum across k-space
