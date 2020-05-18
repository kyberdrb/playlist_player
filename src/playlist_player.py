import time
import subprocess

class PlaylistPlayer:

    def __init__(self):
        self.playlist = None

    def updatePlaylist(self, playlist):
        self.playlist = playlist

    def play(self):
        for songURL in self.playlist:
            print(songURL)
            print()

            # Option "--play-to-the-end": start the player in a detached thread; the thread will terminate after 
            #  the playlist item will go to the end, instead of terminating the player with the script at 'CTRL + C', i.e. KeyboardInterrupt exception
            p = subprocess.Popen(
                ["vlc", "--play-and-exit", "--playlist-autostart", "--no-video", "--qt-start-minimized", songURL], 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # WaveDrawer - constructor
            paddingSize = 0
            step = 1

            # WaveDrawer - draw
            while p.poll() == None:
                padding = str()
                for eachUnit in range(paddingSize):
                    padding += ' '

                # if wave.hitLeftBorder():
                if paddingSize == 0:
                    # wave.bounceOffFromLeftBorder()
                    sign = "("
                    step = 1

                # if wave.hitRightBorder():
                if paddingSize == 4:
                    # wave.bounceOffFromRightBorder()
                    sign = ")"
                    step = -1

                # Encapsulate compound condition into a separate boolean function
                # if wave.goesForward():
                if paddingSize != 0 and paddingSize != 4 and step == 1:
                    sign = "\\"

                # Encapsulate compound condition into a separate boolean function
                # if waveDrawer.goesBackward():
                if paddingSize != 0 and paddingSize != 4 and step == -1:
                    sign = "/"

                print(padding + sign)
                paddingSize += step

                # PlaylistPlayer - play(Playlist) cont.
                time.sleep(1)

        # Option "--loop / --no-loop": when specified, shuffle again and play, otherwise stop at the end of the playlist
        #  default: enabled (--loop)
        print()
        print("============================================")
        print("Playback finished.")
        print("============================================")
        print()