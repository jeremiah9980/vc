# Google Drive Ingestion Workflow

## Easiest option: Google Drive for Desktop

1. Create a Drive folder named `DriveClipPipeline/incoming_clips`.
2. Mirror it locally with Google Drive for Desktop.
3. Symlink or point the local mirrored folder to this repo's `incoming/` directory.
4. Run the processing script on a schedule or manually.

## Better automation: rclone

Example concept:

```bash
rclone copy gdrive:DriveClipPipeline/incoming_clips ./incoming
python3 src/process_clips.py --input incoming --output output --preset softball_daylight
rclone copy ./output gdrive:DriveClipPipeline/cleaned_clips
```

## n8n approach

Suggested nodes:

- Google Drive Trigger
- Download File
- Execute Command on processing host
- Upload cleaned output to Google Drive
- Optional Slack or email notification

## Best practices

- Use separate folders for raw, processing, cleaned, and archived clips.
- Use consistent naming conventions:
  - `2026-03-15_game1_clip001.mp4`
  - `2026-03-15_game1_clip002.mp4`
- Keep raw files untouched.
- Export cleaned clips with `.cleaned.mp4` suffix.
- Archive completed raw footage after review.
