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
    p = subprocess.Popen(["vlc", "--play-and-exit", "--playlist-autostart", "--no-video", "--qt-start-minimized", songURL], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    spaces = 0
    step = 1
    while p.poll() == None:
        padding = str()
        for space in range(spaces):
            padding += ' '

        if step == 1:
            if spaces == 0:
                sign = "("
                step = 1
            elif spaces == 4:
                sign = ")"
                step = -1
            else:
                sign = "\\"

        if step == -1:
            if spaces == 0:
                sign = "("
                step = 1
            elif spaces == 4:
                sign = ")"
                step = -1
            else:
                sign = "/"

        print(padding + sign)

        spaces += step

        time.sleep(1)


print()
print("============================================")
print("Playback finished.")
print("============================================")
print()

