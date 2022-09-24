# win64-ffmpeg-updater
A basic ffmpeg update script for windows written in python. Probably works (well, most of the time anyways). This script does not do anything about environment variables; it assumes they're already set up correctly. It's an updater, not an installer.
# Usage
Put the `.py` (or `.exe`) (hopefully coming soon :tm:) file in the folder you want ffmpeg to be, and then run it. By default, the resulting folder structure will be like this: 
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
# Config
This script has two optional settings you can configure by creating a `config.txt` file in the same directory as the script.  
You can set the location ffmpeg is saved to by having a line containing `extDir = C:\path\to\location`, 
and you can set whether or not the doc files by having a line containing `getDocs = True` or `getDocs = False`.  
All other lines will be ignored, so you can write any comments you feel are necessary. An example config is included in the repo for reference.
# Credits
Thanks to: 
- Various tutorial sites and stackoverflow users for providing code for me to ~~steal~~ use :)
- [BtbN](https://github.com/BtbN) for providing precompiled ffmpeg builds.
