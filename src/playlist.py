import random

class Playlist:

    def __init__(self):
        self.playlistItems = list()

    def append(self, playlistItem):
        self.playlistItems.append(playlistItem)

    @staticmethod
    def shuffle(playlistItems):
        random.shuffle(playlistItems)

    @staticmethod
    def getAllPlaylistItems(playlistItems):
        playlistItemsAsText = str()
        for songURL in playlistItems:
            playlistItemsAsText += songURL
            playlistItemsAsText += '\n'
        
        return playlistItemsAsText