#ffmpeg updater by zozo
#initial ver. 2022-08-11
#last updated 2022-08-12

import requests, zipfile, time

#download and save latest precompiled ffmpeg build from BtbN
def download():
    print("downloading...")
    downloadFile = requests.get("https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip")
    open("ffmpeg.zip", "wb").write(downloadFile.content)

#extract downloaded zip file
def extract():
    print("extracting...")
    with zipfile.ZipFile("ffmpeg.zip", "r") as ffmpeg:
        ffmpeg.extractall()

startTime = time.time()
download()
extract()
finishTime =  time.time()
timeLapsed = time.strftime("%Mm %Ss", time.gmtime(finishTime - startTime))
print("done! in " + str(timeLapsed))
