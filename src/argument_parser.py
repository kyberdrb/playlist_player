import sys

class ArgumentParser:

    def getPlaylistSource(self):
        playlistSource = "dnb_instrumental_no_vocals.m3u8"
        if len(sys.argv) >= 2:
            playlistSource = sys.argv[1]
            print("Argument provided:\t%s"% playlistSource)

        return playlistSource