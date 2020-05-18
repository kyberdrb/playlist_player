from src.playlist import Playlist

class PlaylistLoader:

    def __init__(self, playlistSource):
        self.playlistSource = playlistSource

    def load(self):
        playlist = Playlist()

        with open(self.playlistSource, "r") as source:
            print("Reading file:\t%s"% self.playlistSource)
            for line in source:
                if "www" in line:
                    line = line.rstrip("\n")
                    playlist.append(line)

        return playlist
