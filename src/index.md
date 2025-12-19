# Electron Microscopy (WIP)

Step-by-step tutorials for electron microscopy at the [Stanford Nano Shared Facilities (SNSF)](https://snsf.stanford.edu/). Focused on practice sitting in front of the microscope with visual elements.

> **New to SNSF?** If you are affiliated with Stanford, follow the [internal access guide](https://nanolabs.stanford.edu/access/internal) to get started.

WIP:

- [ ] Use real screenshots instead of pictures
- [ ] Better pictures: proportion, focus, FOV
- [ ] More visuals added to each session when needed

> **Disclaimer:** Always follow [https://barnum.su.domains/](https://barnum.su.domains/) for correctness. Only use this documentation if you are working with the authors and need quick visual references.

## Available guides

| Guide                           | Instrument | Description                          | Readiness | Status         |
| ------------------------------- | ---------- | ------------------------------------ | --------- | -------------- |
| [STEM](STEM.md)                 | Spectra    | STEM alignment and imaging           | 5/10      | Available      |
| [4D-STEM](4D-STEM.md)           | Spectra    | 4D-STEM with Dectris detector        | 2/10      | Available      |
| [EELS](EELS.md)                 | Spectra    | Electron Energy Loss Spectroscopy    | 2/10      | Available      |
| [EDS](EDS.md)                   | Spectra    | Energy Dispersive X-ray Spectroscopy | 2/10      | Available      |
| [TEM](TEM.md)                   | Titan      | TEM alignment and imaging            | -         | 🚧 Coming soon |
| [Tomography](tomography.md)     | Spectra    | Electron tomography                  | -         | 🚧 Coming soon |
| [Ptychography](ptychography.md) | Spectra    | Ptychography imaging                 | -         | 🚧 Coming soon |
| [PED](PED.md)                   | Spectra    | Precession Electron Diffraction      | -         | 🚧 Coming soon |


**SNSF instruments:**

- [FEI Titan at SNSF](https://snsf.stanford.edu/facilities/eim/titan)
- [Spectra 300 at SNSF](https://snsf.stanford.edu/facilities/eim/spectra)

**Other resources:**

- Simulate ronchigram: https://bobleesj.github.io/electron-microscopy-website/ronchigram
- (S)TEM alignment diagrams: https://www.rodenburg.org/RODENBURg_STEM.pdf

## 🙋 Looking for volunteers!

We appreciate feedback, corrections, and contributions from the community!

- **Found an error?** Open an issue or submit a PR
- **Want to add your institution's SOP?** Reach out to [@bobleesj](https://github.com/bobleesj) - we can help with writing and formatting as long as you have notes, Word docs, or rough drafts
- **Have suggestions?** See the [GitHub repo](https://github.com/bobleesj/electron-microscopy) for contribution guidelines

## Acknowledgments

Authors thank Dr. Pinaki Mukherjee for training @bobleesj and Guoliang Hu at Stanford SNSF.

## Changelog

- Dec 18, 2025 - Add drafts of EELS nad EDS
- Dec 17, 2025 - Use mdBook to render static pages and host on GitHub
- Dec 16, 2025 - Add Python script, detect new images from `.git`, convert to `.jpg` and compress.
- Dec 14, 2025 - Begin Electron Microscopy training documentation, led by @bobleesj.

Separate changelog is provided for each tutorial page.
