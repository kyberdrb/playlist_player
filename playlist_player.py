import random
import subprocess
import time

songURLs = list()

with open("dnb_instrumental_no_vocals.m3u8", "r") as playlistFile:
    for line in playlistFile:
        if "youtube" in line:
            line = line.rstrip("\n")
            songURLs.append(line)

random.shuffle(songURLs)

for songURL in songURLs:
    print(songURL)

print()

for songURL in songURLs:
    print(songURL)
    p = subprocess.Popen(
        ["vlc", "--play-and-exit", "--playlist-autostart", "--no-video", "--qt-start-minimized", songURL], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    paddingSize = 0
    step = 1
    while p.poll() == None:
        padding = str()
        for eachUnit in range(paddingSize):
            padding += ' '

        if paddingSize == 0:
            sign = "("
            step = 1

        if paddingSize == 4:
            sign = ")"
            step = -1

        if paddingSize != 0 and paddingSize != 4 and step == 1:
            sign = "\\"

        if paddingSize != 0 and paddingSize != 4 and step == -1:
            sign = "/"

        print(padding + sign)
        paddingSize += step
        time.sleep(1)


print()
print("============================================")
print("Playback finished.")
print("============================================")
print()

