#ffmpeg updater by zozo
#initial ver. 2022-08-11
#last updated 2022-08-16

import requests, zipfile, time, colorama, os, sys

#download and save latest precompiled ffmpeg build from BtbN
def download():
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
        open("ffmpeg.zip", "wb").write(downloadFile.content)


#extract downloaded zip file
def extract():
    print("extracting...")
    with zipfile.ZipFile("ffmpeg.zip", "r") as ffmpeg:
        for file in ffmpeg.infolist():
            if file.is_dir() == False:
                if "bin" in file.filename:
                    file.filename = os.path.basename(file.filename)
                    ffmpeg.extract(file, "bin")
    #delete zip after extracting contents
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
