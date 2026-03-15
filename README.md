# DriveClip Pipeline

A GitHub-ready starter repository for an automated sports video processing workflow:

- watches a Google Drive upload location
- downloads new clips into a local processing queue
- applies FFmpeg cleanup presets
- exports cleaned clips
- publishes a lightweight project website with setup docs

This starter is designed for creators building repeatable highlight workflows for softball, baseball, basketball, and recruiting content.

## What this repo includes

- **project website** in `docs/` for GitHub Pages
- **Python processing script** for clip cleanup
- **preset configuration** for common sports scenarios
- **Mac setup script** for FFmpeg + Python environment
- **sample automation ideas** for Google Drive ingestion
- **GitHub Actions workflow** for basic Pages deployment

## Recommended workflow

1. Upload clips to Google Drive.
2. Sync or export those files into the local `incoming/` folder.
3. Run the processing script.
4. Review cleaned clips in `output/`.
5. Use the cleaned files in CapCut, Final Cut Pro, Premiere, or an AI highlight workflow.

## Repository structure

```text
video-pipeline-repo/
├── .github/workflows/
├── automation/
├── config/
├── docs/
├── scripts/
├── src/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Quick start

### 1) Clone the repo

```bash
git clone https://github.com/YOUR-USERNAME/video-pipeline-repo.git
cd video-pipeline-repo
```

### 2) Run the Mac setup script

```bash
chmod +x scripts/setup_mac.sh
./scripts/setup_mac.sh
```

### 3) Drop source clips into `incoming/`

Supported examples:
- `.mp4`
- `.mov`
- `.mkv`

### 4) Process clips

```bash
python3 src/process_clips.py --input incoming --output output --preset softball_daylight
```

## Available presets

Preset names are defined in `config/presets.json`.

- `softball_daylight`
- `baseball_daylight`
- `basketball_indoor`
- `general_action`

## Google Drive ingestion options

This starter supports multiple approaches:

### Option A — Google Drive for Desktop
Use Google Drive for Desktop to mirror a Drive folder locally and point `incoming/` to that mirrored folder.

### Option B — rclone
Mount or sync a Drive folder to a local path, then schedule processing.

### Option C — n8n / Make / Zapier
Watch for new Drive files, move them into a processing folder, and trigger the processing host.

## Notes

- FFmpeg must be installed and available in your shell path.
- Video enhancement is intentionally conservative so that clips stay natural.
- This is a starter system, not a locked-down production platform.

## Publish the site

This repo includes a static site in `docs/`.

To use GitHub Pages:

1. Push the repo to GitHub.
2. In repository settings, enable **Pages**.
3. Set the source to **Deploy from branch** or use the included GitHub Actions workflow.
4. Your project site will publish from the `docs/` folder or workflow artifact.

## Next upgrades

- auto trim dead space
- speech/noise cleanup
- scorebug crop presets
- AI event tagging
- highlight reel assembly
- player-specific clip bucketing

