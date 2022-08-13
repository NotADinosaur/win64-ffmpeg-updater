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

#program starts here
startTime = time.time()
download()
extract()
finishTime =  time.time()
if float(time.strftime("%M", time.gmtime(finishTime - startTime))) < 1:
    timeLapsed = time.strftime("%Ss", time.gmtime(finishTime - startTime))
else:
    timeLapsed = time.strftime("%Mm %Ss", time.gmtime(finishTime - startTime))
print("done! in " + str(timeLapsed))
