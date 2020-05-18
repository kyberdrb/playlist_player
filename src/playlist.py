import random

class Playlist:

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