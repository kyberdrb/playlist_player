class PlaylistLoader:

    def __init__(self, playlistFile):
        self.playlistFile = playlistFile

    def load(self):
        playlistItems = list()

        with open(self.playlistFile, "r") as playlist:
            print("Reading file:\t%s"% self.playlistFile)
            for line in playlist:
                if "www" in line:
                    line = line.rstrip("\n")
                    playlistItems.append(line)

        return playlistItems
