class PlaylistLoader:

    def __init__(self, playlistFile):
        self.playlistFile = playlistFile

    @staticmethod
    def load(playlistFile):
        playlistItems = list()

        with open(playlistFile, "r") as playlist:
            print("Reading file:\t%s"% playlistFile)
            for line in playlist:
                if "www" in line:
                    line = line.rstrip("\n")
                    playlistItems.append(line)

        return playlistItems
