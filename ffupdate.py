#ffmpeg updater by zozo
#initial ver. 2022-08-11
#last updated 2022-08-14

import requests, zipfile, time, colorama, os

#download and save latest precompiled ffmpeg build from BtbN
def download():
    print("downloading...")
    downloadFile = requests.get("https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip")
    open("ffmpeg.zip", "wb").write(downloadFile.content)

#extract downloaded zip file
def extract():
    print("extracting...")
    with zipfile.ZipFile("ffmpeg.zip", "r") as ffmpeg:
        for file in ffmpeg.infolist():
            if file.filename[-1] == "/":
                continue
            if "bin" in file.filename:
                file.filename = os.path.basename(file.filename)
                ffmpeg.extract(file, "bin")
            elif "doc" in file.filename:
                file.filename = os.path.basename(file.filename)
                ffmpeg.extract(file, "doc")
            else:
                file.filename = os.path.basename(file.filename)
                ffmpeg.extract(file, "testdir")
    #delete zip after exracting contents
    os.remove("ffmpeg.zip")

#program starts here
colorama.init()
startTime = time.time()
download()
extract()
finishTime =  time.time()
if float(time.strftime("%M", time.gmtime(finishTime - startTime))) < 1:
    timeLapsed = time.strftime("%Ss", time.gmtime(finishTime - startTime))
else:
    timeLapsed = time.strftime("%Mm %Ss", time.gmtime(finishTime - startTime))
print("\033[0;32mdone! \033[0;0m" + "in " + str(timeLapsed))
input("press any key to exit")
