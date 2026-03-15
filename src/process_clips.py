#!/usr/bin/env python3
"""Batch process sports clips with FFmpeg presets."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Any

SUPPORTED_EXTENSIONS = {".mp4", ".mov", ".mkv", ".m4v"}


def load_presets(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def ensure_ffmpeg() -> None:
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("FFmpeg is not installed or not available in PATH.")


def build_command(input_file: Path, output_file: Path, preset: Dict[str, Any]) -> list[str]:
    return [
        "ffmpeg",
        "-y",
        "-i",
        str(input_file),
        "-vf",
        preset["video_filters"],
        "-af",
        preset["audio_filters"],
        "-c:v",
        preset["video_codec"],
        "-preset",
        str(preset.get("preset", "medium")),
        "-crf",
        str(preset.get("crf", 21)),
        "-c:a",
        preset["audio_codec"],
        str(output_file),
    ]


def process_directory(input_dir: Path, output_dir: Path, preset_name: str, presets: Dict[str, Any]) -> None:
    if preset_name not in presets:
        raise ValueError(f"Unknown preset: {preset_name}")

    preset = presets[preset_name]
    output_dir.mkdir(parents=True, exist_ok=True)

    clips = [p for p in input_dir.iterdir() if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS]
    if not clips:
        print(f"No supported clips found in {input_dir}")
        return

    for clip in clips:
        output_file = output_dir / f"{clip.stem}.cleaned.mp4"
        cmd = build_command(clip, output_file, preset)
        print(f"Processing: {clip.name} -> {output_file.name}")
        subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch process sports video clips.")
    parser.add_argument("--input", required=True, help="Input directory with raw clips")
    parser.add_argument("--output", required=True, help="Output directory for cleaned clips")
    parser.add_argument("--preset", required=True, help="Preset name from config/presets.json")
    parser.add_argument(
        "--config",
        default="config/presets.json",
        help="Path to presets configuration JSON"
    )
    args = parser.parse_args()

    ensure_ffmpeg()

    input_dir = Path(args.input)
    output_dir = Path(args.output)
    config_path = Path(args.config)

    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    presets = load_presets(config_path)
    process_directory(input_dir, output_dir, args.preset, presets)
    print("Done.")


if __name__ == "__main__":
    main()
