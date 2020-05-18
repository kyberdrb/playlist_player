from src.playlist import Playlist

class PlaylistLoader:

    def __init__(self, playlistSource):
        self.playlistSource = playlistSource

    def load(self):
        playlistItems = list()
        playlist = Playlist()

        with open(self.playlistSource, "r") as source:
            print("Reading file:\t%s"% source)
            for line in source:
                if "www" in line:
                    line = line.rstrip("\n")
                    playlistItems.append(line)
                    playlist.append(line)

        return playlistItems
