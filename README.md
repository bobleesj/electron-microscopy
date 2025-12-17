# Electron Microscopy Training (WIP)

WIP:

- [ ] Use real screenshots instead of pictures
- [ ] Better pictures: proportion, focus, FOV
- [ ] More visuals added to each session when needed

Disclaimer: Always follow [https://barnum.su.domains/](https://barnum.su.domains/) for correctness. Only use this documentation if you are working with the authors of the document and you are looking for quick visual references.

The content is meant to be used as a step-by-step tutorial focused on practice sitting in front of the microscope with a focus on visual elements.

## Available guides

| Guide                           | Description                               | Status         |
| ------------------------------- | ----------------------------------------- | -------------- |
| [STEM](STEM.md)                 | Basic STEM alignment procedures           | Available      |
| [4D-STEM](4D-STEM.md)           | 4D-STEM acquisition with Dectris detector | Available      |
| [EELS](EELS.md)                 | Electron Energy Loss Spectroscopy         | 🚧 Coming soon |
| [EDS](EDS.md)                   | Energy Dispersive X-ray Spectroscopy      | 🚧 Coming soon |
| [Tomography](tomography.md)     | Electron tomography                       | 🚧 Coming soon |
| [Ptychography](ptychography.md) | Ptychography imaging                      | 🚧 Coming soon |
| [PED](ped.md)                   | -                                         | 🚧 Coming soon |

## Immediate TODO

- [ ] `README.md` - how to open/close TITAN holder box
- [ ] `STEM.md` - better probe correction process
- [ ] `4D-STEM.md` - use API to turn on/off 4D-STEM camera

## How to load sample

> Disclaimer: This guide is written for those who have already used single-tilt and double-tilt holders before. If you are using this documentation for the first time, you should work with a supervisor.

### Single-tilt holder

**Load sample:**

> FIXME: use technical terms for these objects... "pin" or "clip"?

1. Push the pin inside the tiny hole shown below:

   <img src="img/sample-loading/single-tilt/01-holder-overview.jpg" alt="Single-tilt holder overview" width="500">

2. Lift the clip gently:

   <img src="img/sample-loading/single-tilt/02-sample-placement.jpg" alt="Sample placement" width="500">

3. If using a copper grid, pinch the tip of the copper grid

   <img src="img/sample-loading/single-tilt/03-holder-ready.jpg" alt="Holder ready" width="500">

4. Place the sample, shiny side up for the standard sample

   <img src="img/sample-loading/single-tilt/04-holder-inserted.jpg" alt="Holder inserted" width="500">

### Double-tilt holder

**Load sample:**

1. Load the sample and washer (gold donut):

   <img src="img/sample-loading/double-tilt/01-holder-preparation.jpg" alt="Holder preparation" width="500">

2. Add the cap and rotate the holder about the long axis to ensure the sample is secure:

   <img src="img/sample-loading/double-tilt/02-holder-insertion.jpg" alt="Holder insertion" width="500">

**Unload sample:**

1. Press down the very small hole gently as shown below:

   <img src="img/sample-loading/double-tilt/03-holder-locked.jpg" alt="Holder locked" width="500">

2. The three parts should all be disassembled and placed on the bottom:

   <img src="img/sample-loading/double-tilt/05-holder-removal.jpg" alt="Holder removal" width="500">

## How to remove and insert holder

**Insert holder**

- Push the holder in, feel resistance. This will start the turbo pump immediately.

  <img src="img/sample-loading/holder-insert/01-holder-insertion.jpg" alt="Holder insertion to microscope" width="500">

- Wait 2 minutes, turn counter-clockwise until you feel gently stuck
- Guide the holder to push in. Expect the holder to move in.
- On TEMUI, turn off turbo pump

**Remove holder**

- Press `Reset holder` in TEMUI.
- Close column valves in TEMUI.
- Pull the holder straight out up to the point shown above, turn clockwise, pull the rest out continuously.

## For maintainers and authors

### Checklist

- [ ] Is our writing the clearest yet most concise for decision-making for complete beginners and those who haven't used the instrument in months or years?
- [ ] Have we added a concise changelog for each document? Example: `Dec 13, 2025 - add 4D-STEM tutorial draft by @bobleesj`
- [ ] Did you run `python scripts/process_new_images.py --max-width 1200 --delete-originals` for new images?

### Writing conventions and principles

Writing guides for humans and quality control:

- We want to make correct decisions with the least cognitive overload for the reader.
- We want to serve "IKEA manual" of microscopes.
- The adage "A picture is worth a thousand words" should be judiciously applied. Balance richness vs. cognitive overload.

Formatting consistency designed for LLM:

- Use sub-bullets (`-`) for details under each step
- No periods for action commands (e.g., `Click Col Valves Open on TEMUI`)
- Use periods for observations/explanations (e.g., `Notice the image is pulsing in and out.`)
- Lowercase for general text, uppercase only for acronyms:
  - Uppercase: TEM, STEM, 4D-STEM, EELS, EDS, HAADF, ABF, BF, FFT, FOV, LLM
  - Uppercase: TEMUI, Velox (software names)
  - Uppercase: A1, A2, B2, C1, C2, C3, S3 (aberration parameters)
  - Lowercase: beam, aperture, intensity, magnification, etc.
- Place images after relevant steps with `alt` text and `width="500"`
- Use `<img src="..." alt="..." width="500">` for all images
- Use `.jpg` format for images (not `.png`)
- Do not use horizontal lines (`---`)
- Keep TODO items at the top of each document (e.g., `> TODO: ...`)
- Keep a `## Changelog` section at the bottom with dated entries
- Use `STEM.md` as the main reference document for formatting.

### Scripts

Process new images (HEIC/PNG → JPG, compress, normalize extensions):

```bash
pip install Pillow pillow-heif
python scripts/process_new_images.py --max-width 1200 --delete-originals
```

## Acknowledgments

Authors thank Dr. Pinaki Mukherjee for training @bobleesj and Guoliang Hu at Stanford SNSF.

## Changelog

- Dec 17, 2025 - Add Python script, detect new images from `.git`, convert to `.jpg` and compress.
- Dec 14, 2025 - Begin Electron Microscopy training documentation, led by @bobleesj.

Separate changelog is provided for each tutorial page.
