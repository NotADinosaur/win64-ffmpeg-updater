#ffmpeg updater by zozo
#initial ver. 2022-08-11
#last updated 2023-08-01

import requests, zipfile, time, colorama, os, sys, argparse

colorama.just_fix_windows_console()
startTime = time.time()
#set up cli arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", default = os.getcwd(), help = "directory to extract ffmpeg to. default: current working directory")
parser.add_argument("-k", "--keep_docs", action = "store_true", help = "whether to keep the docs files ffmpeg comes with. default: false")
args = parser.parse_args()
#download and save latest precompiled ffmpeg build from BtbN
print("downloading...")
try:
    downloadFile = requests.get("https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip", timeout = 60)
#throw a connection error if something goes wrong
except requests.exceptions.RequestException:
    print("\033[0;31m" + "connection error: " + "\033[0;0m" + "an error occured while downloading ffmpeg")
    #delete any partially downloaded files
    if os.path.isfile("ffmpeg.zip") == True:
        os.remove("ffmpeg.zip")
    input("press enter key to exit")
    sys.exit()
else:
    with open("ffmpeg.zip", "wb") as save:
        save.write(downloadFile.content)
#extract downloaded zip file
print("extracting...")
try:
    with zipfile.ZipFile("ffmpeg.zip", "r") as ffmpeg:
        for file in ffmpeg.infolist():
            if file.is_dir() == False:
                if args.keep_docs == False:
                    if "bin" in file.filename:
                        file.filename = os.path.basename(file.filename)
                        ffmpeg.extract(file, args.dir)
                elif args.keep_docs == True:
                    extDoc = args.dir + "\\doc"
                    if "bin" in file.filename:
                        file.filename = os.path.basename(file.filename)
                        ffmpeg.extract(file, args.dir)
                    else:
                        file.filename = os.path.basename(file.filename)
                        ffmpeg.extract(file, extDoc)
except:
    print("\033[0;31m" + "file error: " + "\033[0;0m" + "an error occured while extracting files.")
    input("press enter key to exit")
    sys.exit()
#delete zip after extracting contents
os.remove("ffmpeg.zip")
finishTime =  time.time()
#convert time into human-readable format
if float(time.strftime("%M", time.gmtime(finishTime - startTime))) < 1:
    timeElapsed = time.strftime("%Ss", time.gmtime(finishTime - startTime))
else:
    timeElapsed = time.strftime("%Mm %Ss", time.gmtime(finishTime - startTime))
print("\033[0;32m" + "done! " + "\033[0;0m" + "in " + str(timeElapsed))
input("press enter key to exit")
