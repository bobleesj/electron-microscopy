# Electron Microscopy Training

📖 **[View the Documentation](https://bobleesj.github.io/electron-microscopy/)**

Step-by-step tutorials focused on practice sitting in front of the microscope with a focus on visual elements.

> Disclaimer: Always follow [https://barnum.su.domains/](https://barnum.su.domains/) for correctness. Only use this documentation if you are working with the authors of the document and you are looking for quick visual references.

## 🙋 Looking for volunteers!

We appreciate feedback, corrections, and contributions from the community!

- **Found an error?** Open an issue or submit a PR
- **Want to add your own SOP for your microscope?** Fork the repo and contribute your guide
- **Have suggestions?** We'd love to hear from you

👉 See [CONTRIBUTING.md](CONTRIBUTING.md) for step-by-step instructions on how to contribute.

## Other resources

- Simulate ronchigram: https://bobleesj.github.io/electron-microscopy-website/ronchigram
- (S)TEM alignment diagrams: https://www.rodenburg.org/RODENBURg_STEM.pdf

## For contributors

### Writing conventions and principles

Writing guides for humans and quality control:

- We want to make correct decisions with the least cognitive overload for the reader.
- We want to serve "IKEA manual" of microscopes.
- The adage "A picture is worth a thousand words" should be judiciously applied. Balance richness vs. cognitive overload.

Formatting consistency:

> You may check the following with your favorite AI tool:

- Use sub-bullets (`-`) for details under each step, with 3-space indent
- Use "in" for software references (e.g., `in TEMUI`, not `on TEMUI`)
- No periods for action commands (e.g., `Click Col Valves Open in TEMUI`)
- Use periods for observations/explanations (e.g., `Notice the image is pulsing in and out.`)
- Wrap software names in backticks: `TEMUI`, `Velox`, `ImageCorrector`, `Sherpa`
- Lowercase for general text, uppercase only for acronyms:
  - Uppercase: TEM, STEM, 4D-STEM, EELS, EDS, HAADF, ABF, BF, FFT, FOV
  - Uppercase: A1, A2, B2, C1, C2, C3, S3 (aberration parameters)
  - Lowercase: beam, aperture, intensity, magnification, etc.
- Spacing rules for bullets and images:
  - No blank line between consecutive sub-bullets
  - Blank line before `<img>` tags (required for proper rendering)
  - No extra blank lines after images before the next bullet
- Image naming: `PREFIX-description.jpg` with `-` separator
  - Use prefix to group images by document section (e.g., in STEM.md: `TEM-` for Part 1, `STEM-` for Part 2, `EXP-` for Part 3, `APP-` for Appendix)
  - Example: `TEM-alignment-beam.jpg`, `STEM-probe-corrector.jpg`, `EXP-sample-view.jpg`
- Place images after relevant steps with `alt` text and `width="500"`
- Use `<img src="..." alt="..." width="500">` for all images
- Use `.jpg` format for images (not `.png`)
- Use `> [!CAUTION]` for warnings at the top of rough drafts
- Keep TODO items at the top of each document (e.g., `> TODO: ...`)
- Keep a `## Changelog` section at the bottom: `- Dec 18, 2025 - description by @username`
- Link to shared sections instead of duplicating (e.g., `[End session](sample-loading.md#end-session)`)
- Use `STEM.md` as the main reference document for formatting

### Checklist before submitting

- [ ] Is our writing the clearest yet most concise for decision-making for complete beginners?
- [ ] Have we added a concise changelog entry?
- [ ] Did you run `python image_edit.py` for new images?

### Local development

**Install mdBook**

```bash
# macOS
brew install mdbook
# Windows/Linux/macOS
cargo install mdbook
```

<details>
<summary>No cargo or trouble install mdbook? (Expand)</summary>

  Download `cargo` from https://doc.rust-lang.org/cargo/getting-started/installation.html

  Did you encounter `note: link.exe returned an unexpected error` while installing mdbook?:
  
  1. Download `rustup-init.exe` from [here](https://rust-lang.github.io/rustup/installation/windows-msvc.html#walkthrough-installing-visual-studio-2022) and run `rustup-init.exe`.

  2. Install Visual Studio by following the tutorial provided [here](https://rust-lang.github.io/rustup/installation/windows-msvc.html#walkthrough-installing-visual-studio-2022). 

  3. On your computer, run `x64 Native Tools Command Prompt for VS 2022` file downloaded.

  4. Run `cargo install mdbook` and `mdbook serve --open`
</details>

**Run local dev server**

```bash
# Run local dev server
mdbook serve --open
```

### Process new images

Convert `.HEIC/.HEIF/.png` to `.jpg`.

```bash
pip install Pillow pillow-heif
python image_edit.py
```

### File structure

```
book.toml          # mdBook configuration
src/
├── SUMMARY.md     # Navigation/table of contents
├── index.md       # Home page
├── STEM.md        # Technique pages
├── 4D-STEM.md
├── ...
└── img/           # Images
```

### Deployment

Push to `main` branch → GitHub Actions auto-deploys to GitHub Pages. See `.github/deploy.yml`.

## Acknowledgments

Authors thank Dr. Pinaki Mukherjee for training @bobleesj and Guoliang Hu at Stanford SNSF.

## Changelog

Related to documentation, project settings, higher-level changes:

- Dec 18, 2025 - Add contribution guide
- Dec 17, 2025 - Migrate to mdBook, add GitHub Pages deployment
- Dec 17, 2025 - Add Python script for image processing
- Dec 14, 2025 - Begin Electron Microscopy training documentation
