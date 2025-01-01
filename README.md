# Lossless to mp3 converter

**Not fully tested! Use at your own risk**.

This simple Python script converts lossless files to lossy 320 kbps MP3.

To trigger, run the following line of code:
```
py main.py "path/to/files" [delete] [recursive]
```

* For `[delete]`, set to `true` if you want.
* For `[recursive]`, set to `true` if you want to convert files in sub-directories as well.

Requires `ffmpeg` to be installed: https://ffmpeg.org/download.html

