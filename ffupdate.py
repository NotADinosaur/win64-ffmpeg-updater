#ffmpeg updater by zozo
#initial ver. 2022-08-11

import requests, zipfile

#download and save latest precompiled ffmpeg build from BtbN
download = requests.get("https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip")
open("ffmpeg.zip", "wb").write(download.content)

#extract downloaded zip file
with zipfile.ZipFile("ffmpeg.zip", "r") as ffmpeg:
    ffmpeg.extractall()

print("done!")
