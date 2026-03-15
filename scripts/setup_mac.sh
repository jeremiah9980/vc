#!/usr/bin/env bash
set -euo pipefail

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is required. Install it first: https://brew.sh"
  exit 1
fi

brew install ffmpeg python
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

mkdir -p incoming processing output logs

echo "Setup complete."
echo "Activate with: source .venv/bin/activate"
echo "Run with: python3 src/process_clips.py --input incoming --output output --preset softball_daylight"
