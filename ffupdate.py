#ffmpeg updater by zozo
#initial ver. 2022-08-11
#last updated 2023-07-31

import requests, zipfile, time, colorama, os, sys

#temporary variables between config file and arguments
extDir = os.getcwd()
extBin = extDir + "\\bin"
extDoc = extDir + "\\doc"
getDocs = True

#program starts here
colorama.init()
startTime = time.time()
#download and save latest precompiled ffmpeg build from BtbN
print("downloading...")
try:
    downloadFile = requests.get("https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip", timeout = 60)
#throw a connection error if something goes wrong
except requests.exceptions.RequestException:
    print("\033[0;31mconnection error: \033[0;0m" + "an error occured while downloading ffmpeg")
    #delete any partially downloaded files
    if os.path.isfile("ffmpeg.zip") == True:
        os.remove("ffmpeg.zip")
    input("press any key to exit")
    sys.exit()
else:
    with open("ffmpeg.zip", "wb") as save:
        save.write(downloadFile.content)
#extract downloaded zip file
print("extracting...")
with zipfile.ZipFile("ffmpeg.zip", "r") as ffmpeg:
    for file in ffmpeg.infolist():
        if file.is_dir() == False:
            if getDocs == True:
                if "bin" in file.filename:
                    file.filename = os.path.basename(file.filename)
                    ffmpeg.extract(file, extBin)
                elif "doc" in file.filename:
                    file.filename = os.path.basename(file.filename)
                    ffmpeg.extract(file, extDoc)
                else:
                    file.filename = os.path.basename(file.filename)
                    ffmpeg.extract(file, extDir)
            elif getDocs == False:
                if "bin" in file.filename:
                    file.filename = os.path.basename(file.filename)
                    ffmpeg.extract(file, extBin)
#delete zip after extracting contents
os.remove("ffmpeg.zip")
finishTime =  time.time()
#convert time into human-readable format
if float(time.strftime("%M", time.gmtime(finishTime - startTime))) < 1:
    timeLapsed = time.strftime("%Ss", time.gmtime(finishTime - startTime))
else:
    timeLapsed = time.strftime("%Mm %Ss", time.gmtime(finishTime - startTime))
print("\033[0;32mdone! \033[0;0m" + "in " + str(timeLapsed))
input("press any key to exit")
