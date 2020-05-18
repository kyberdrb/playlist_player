from src.playlist import Playlist
from src.playlist_loader import PlaylistLoader
from src.argument_parser import ArgumentParser
from src.playlist_player import PlaylistPlayer

if __name__ == "__main__":
    argumentParser = ArgumentParser()
    playlistSource = argumentParser.getPlaylistSource()

    # PlaylistLoader
    #   - empty ctor
    #   - and/or ctor(PlaylistFile)/ctor(YoutubePlaylist)
    #     - polymorphism? overload? - first overload, then polymorphism
    playlistLoader = PlaylistLoader(playlistSource)

    # PlaylistLoader - load(PlaylistFile playlistSource) - overload
    playlist = playlistLoader.load()

    # Move all print commands to a separate class 'Screen'
    print()

    # PlaylistLoader - load(YoutubePlaylist youtubePlaylist) - overload
    ####import subprocess
    ####youtube-dl --flat-playlist --dump-json https://www.youtube.com/playlist?list=UUREvOFg1F4bfZZqdmIJknrg | cut -d' ' -f4 | sed 's/[",]//g' | sed "s/^/https:\/\/www\.youtube\.com\/watch\?v=/g"

    # Playlist shuffle will be optional and enabled by default, 
    # if not specified at application start:
    #   - it will be enabled/disabled by a option '--shuffle/--no-shuffle'
    playlist.shuffle()

    print(playlist.getAllPlaylistItemsAsText())

    playlistPlayer = PlaylistPlayer()
    playlistPlayer.updatePlaylist(playlist)
    playlistPlayer.play()
