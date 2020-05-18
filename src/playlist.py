import random

class Playlist:

    def __init__(self):
        self.playlistItems = list()

    def append(self, playlistItem):
        self.playlistItems.append(playlistItem)

    def shuffle(self):
        random.shuffle(self.playlistItems)

    def getAllPlaylistItemsAsText(self):
        playlistItemsAsText = str()
        for playlistItem in self.playlistItems:
            playlistItemsAsText += playlistItem
            playlistItemsAsText += '\n'
        
        return playlistItemsAsText

    def __iter__(self):
       return iter(self.playlistItems)