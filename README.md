MUSICA Extractor — Quick Guide
=============================

What it does
---
- Reads video URLs from `links.txt` (one per line).
- Downloads the best audio with `yt-dlp`, converts to MP3 (192 kbps), and saves in `downloads/`.

Requirements
---
- Python 3
- `yt-dlp` (install with `python3 -m pip install yt-dlp`)
- `ffmpeg` installed and on your PATH

Quick use
---
1. Put one URL per line in `links.txt` next to `main.py`.
2. Run:

```bash
python3 main.py
```

Output
---
- MP3 files are saved to the `downloads/` directory using the video title as filename.

Notes
---
- If `links.txt` is missing or empty the script will notify you.
- To change format, bitrate, or output location, edit the `ydl_opts` dictionary in `main.py`.

