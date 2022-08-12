# win64-ffmpeg-updater
A basic ffmpeg update script for windows written in python. Probably works (well, most of the time anyways). This script does not do anything about environment variables; it assumes they're already set up correctly. It's an updater, not an installer.
# Usage
Put the `.py` (or `.exe`) file in the folder you want ffmpeg to be, and then run it. The resulting folder structure will be like this: 
```
<ffmpeg folder>
├── ffupdate.py
├──bin
│  ├── ffmpeg.exe
│  ├── ffplay.exe
│  └── ffprobe.exe
├── doc
│   └── <doc files> 
└── LICENSE.txt
```
# Credits
Thanks to various tutorial sites and stackoverflow users for providing code for me to ~~steal~~ use :)
