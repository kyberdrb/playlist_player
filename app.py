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
    print()

    # PlaylistLoader - load(YoutubePlaylist youtubePlaylist) - overload
    ####import subprocess
    ####youtube-dl --flat-playlist --dump-json https://www.youtube.com/playlist?list=UUREvOFg1F4bfZZqdmIJknrg | cut -d' ' -f4 | sed 's/[",]//g' | sed "s/^/https:\/\/www\.youtube\.com\/watch\?v=/g"

    # Playlist - shuffle()
    #   - optional - will be enabled/disabled by a flag
    Playlist.shuffle(playlist)

    # Playlist - getAllPlaylistItems()
    print(Playlist.getAllPlaylistItems(playlist))

    # PlaylistPlayer - play(Playlist)
    PlaylistPlayer.play(playlist)

