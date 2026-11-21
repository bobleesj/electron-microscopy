# Electron Microscopy (WIP)

Step-by-step visual guides for learning TEM. Focused on practice sitting in front of the microscope with visual elements.

WIP:

- [ ] Use real screenshots instead of pictures
- [ ] Better pictures: proportion, focus, FOV
- [ ] More visuals added to each session when needed

> **Disclaimer:** Always follow [https://barnum.su.domains/](https://barnum.su.domains/) for correctness. Only use this documentation if you are working with the authors and need quick visual references.

## Available guides

| Guide | Instrument | Description | Readiness | Status |
| ----- | ---------- | ----------- | --------- | ------ |
| [STEM (Spectra)](spectra_STEM/index.md) | Spectra | STEM probe correction and imaging | 8/10 | Available |
| [TEM (Spectra)](spectra_TEM/index.md) | Spectra | Optional TEM alignment and image correction | 5/10 | Available |
| [TEM (Titan)](titan_TEM/index.md) | Titan | TEM alignment and imaging | - | Coming soon |
| [4DSTEM](4DSTEM/index.md) | Spectra | 4DSTEM with Dectris detector | 4/10 | Available |
| [EELS](EELS/index.md) | Spectra | Electron Energy Loss Spectroscopy | 2/10 | Available |
| [EDS](EDS/index.md) | Spectra | Energy Dispersive X-ray Spectroscopy | 2/10 | Available |
| [Aberration Correction (Advanced)](aberration-correction/index.md) | Spectra | Manual aberration correction without Sherpa | 1/10 | Available |

**Instrument links:**

- [FEI Titan at SNSF](https://snsf.stanford.edu/facilities/eim/titan)
- [Spectra 300 at SNSF](https://snsf.stanford.edu/facilities/eim/spectra)

**Other resources:**

- [Ronchigram simulator](https://bobleesj.github.io/electron-microscopy-website/ronchigram)
- [(S)TEM alignment diagrams](https://www.rodenburg.org/RODENBURg_STEM.pdf)

## Acknowledgments

Authors thank Dr. Pinaki Mukherjee and Andrew Barnum for training @bobleesj and Guoliang Hu at Stanford SNSF.

## Changelog

- Nov 15, 2026 - Add Spectra [beam finding](spectra_STEM/index.md#cant-find-the-beam), reorganize sample loading and end session, and clarify Arina shutdown
- Apr 22, 2026 - Reorganize sidebar into SNSF Spectra 300, Techniques, Class labs, Grid preparation, Sample loading sections
- Apr 22, 2026 - Add class lab guide on spot size and convergence angle (Talos)
- Apr 22, 2026 - Add drop casting grid preparation guide
- Mar 1, 2026 - Restructure STEM and TEM guides, add pre-session checklist and end session procedures
- Feb 28, 2026 - Reorganize guide structure, rename directories, add safety warnings
- Jan 31, 2026 - Add STEM probe correction guide with screenshots from Andrew Barnum training
- Jan 31, 2026 - Add draft Titan TEM guide
- Dec 18, 2025 - Add EELS and EDS guides
- Dec 17, 2025 - Use mdBook to render static pages and host on GitHub
- Dec 14, 2025 - Begin Electron Microscopy training documentation, led by @bobleesj
