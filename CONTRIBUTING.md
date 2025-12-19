# Contributing guide

Thank you for your interest in contributing to the electron microscopy training documentation!

This documentation is built by scientists from various backgrounds. No prior programming experience is required. Below, we provide step-by-step tutorials on how to make your first contribution.

## Method 1. Edit directly on GitHub (recommended)

The easiest way to contribute is directly from the GitHub website—no software installation needed:

<img src="src/img/CONTRIB-github-edit.png" alt="GitHub edit button" width="600">

1. Go to [https://github.com/bobleesj/electron-microscopy](https://github.com/bobleesj/electron-microscopy)
2. Navigate to the file you want to edit (e.g., `src/STEM.md`)
3. Click the pencil icon (✏️) to edit the file
4. Make your changes in the text editor
5. Click `Preview` to see how your changes will look
6. Scroll down and write a short description of your changes (e.g., "Add pictures for EELS calibration steps")
7. Click `Propose changes`
8. Click `Create pull request`
9. Tag @bobleesj in the description and wait for your changes to be reviewed and merged

Once merged, the website updates automatically within minutes!

## Method 2. Edit using Git on your computer

This method gives you more control and is useful for larger edits. If you're new to Git, see the beginner-friendly tutorials at https://scikit-package.github.io/scikit-package.

### First-time setup

These steps only need to be done once.

#### Step 1. Copy the repository to your GitHub account (fork)

1. Go to [https://github.com/bobleesj/electron-microscopy](https://github.com/bobleesj/electron-microscopy) and click the `Fork` button. This creates your own copy at `https://github.com/<your-username>/electron-microscopy`.

#### Step 2. Download the repository to your computer (clone)

1. Open a terminal application:
   - **macOS**: Open `Terminal` (found in Applications → Utilities)
   - **Windows**: We recommend [Git for Windows](https://git-scm.com/download/win), which provides a terminal that works with the commands below

2. Download your forked repository by typing:
   ```bash
   git clone https://github.com/<your-username>/electron-microscopy
   ```
   Replace `<your-username>` with your GitHub username.

3. Verify the connection by typing:
   ```bash
   git remote -v
   ```
   You should see `origin` pointing to your forked repository.

#### Step 3. Create a branch and make changes

The `main` branch is the official version. Always create a separate branch for your edits:

1. Create a new branch (replace `<branch-name>` with a descriptive name like `fix-stem-typos`):
   ```bash
   git checkout -b <branch-name>
   ```

2. Open the files in a text editor (e.g., VS Code, TextEdit, Notepad) and make your changes.

3. Check which files you modified:
   ```bash
   git status
   ```

4. Stage your changes (prepare them to be saved):
   ```bash
   git add <file-or-folder>
   ```

5. Save your changes with a description:
   ```bash
   git commit -m "Fix typo in STEM alignment section"
   ```

6. Upload your changes to GitHub:
   ```bash
   git push --set-upstream origin <branch-name>
   ```

#### Step 4. Submit your changes for review (pull request)

1. Go to [https://github.com/bobleesj/electron-microscopy](https://github.com/bobleesj/electron-microscopy)
2. You should see a green `Compare & pull request` button—click it
3. Write a short title describing your changes
4. Click `Create pull request`
5. Wait for review. Once approved and merged, the website updates automatically!

### Contributing again (after your first time)

Before making new edits, sync your copy with the latest version:

1. Add the original repository as `upstream` (only needed once):
   ```bash
   git remote add upstream https://github.com/bobleesj/electron-microscopy
   ```

2. Switch to your main branch and download the latest changes:
   ```bash
   git checkout main
   git pull upstream main
   ```

3. Create a new branch for your new edits:
   ```bash
   git checkout -b <new-branch-name>
   ```

4. Make changes, then stage, commit, and push:
   ```bash
   git add <files>
   git commit -m "<description of changes>"
   git push --set-upstream origin <new-branch-name>
   ```

5. Create a pull request as described in Step 4 above.

## Adding images

1. Add images to the appropriate folder under `src/img/`
2. Run the image processing script:
   ```bash
   # Convert png to jpg and compress images
   python image_edit.py
   ```
3. Use `<img>` tags in markdown:
   ```html
   <img src="img/STEM/TEM-example.jpg" alt="<Description>" width="500">
   ```

## Local preview

```bash
# Install mdBook (macOS)
brew install mdbook

# Run local server
mdbook serve --open
```

## Questions?

Open an issue at [https://github.com/bobleesj/electron-microscopy/issues](https://github.com/bobleesj/electron-microscopy/issues)
