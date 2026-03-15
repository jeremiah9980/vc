#!/usr/bin/env bash
set -euo pipefail

PRESET="${1:-softball_daylight}"

mkdir -p incoming output logs
python3 src/process_clips.py --input incoming --output output --preset "$PRESET" | tee logs/pipeline.log
