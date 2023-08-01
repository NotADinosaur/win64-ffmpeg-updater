# win64-ffmpeg-updater
A basic ffmpeg update script for windows written in python. This script does not do anything about environment variables; it assumes they're already set up correctly - it's an updater, not an installer.  
Depends on python 3.7+ and the `requests`, `colorama`, and `tqdm` packages from `pip`.
# Usage
`ffupdate [--dir DIR] [--keep_docs]`  
`--keep_docs` (or `-k`): whether to keep the docs files ffmpeg comes with. default: false  
`--dir` (or `-d`): directory to extract ffmpeg to. default: current working directory  
# Credits
Thanks to: 
- Various tutorial sites and stackoverflow users for providing code for me to ~~steal~~ use :)
- [BtbN](https://github.com/BtbN) for providing precompiled ffmpeg builds.
