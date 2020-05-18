from src.playlist import Playlist
from src.playlist_loader import PlaylistLoader
from src.argument_parser import ArgumentParser

def play():
    argumentParser = ArgumentParser()
    playlistSource = argumentParser.getPlaylistSource()

    # PlaylistLoader
    #   - empty ctor
    #   - and/or ctor(PlaylistFile)/ctor(YoutubePlaylist)
    #     - polymorphism? overload? - first overload, then polymorphism
    playlistLoader = PlaylistLoader(playlistSource)

    # PlaylistLoader - load(PlaylistFile playlistSource) - overload
    playlistItems = PlaylistLoader.load(playlistSource)
    print()

    # PlaylistLoader - load(YoutubePlaylist youtubePlaylist) - overload
    ####import subprocess
    ####youtube-dl --flat-playlist --dump-json https://www.youtube.com/playlist?list=UUREvOFg1F4bfZZqdmIJknrg | cut -d' ' -f4 | sed 's/[",]//g' | sed "s/^/https:\/\/www\.youtube\.com\/watch\?v=/g"

    # Playlist - shuffle()
    #   - optional - will be enabled/disabled by a flag
    Playlist.shuffle(playlistItems)

    # Playlist - getAllPlaylistItems()
    print(Playlist.getAllPlaylistItems(playlistItems))

    # PlaylistPlayer - play(Playlist)
    import time
    import subprocess
    for songURL in playlistItems:
        print(songURL)
        print()

        # Option "--play-to-the-end": start the player in a detached thread; the thread will terminate after 
        #  the playlist item will go to the end, instead of terminating the player with the script at 'CTRL + C', i.e. KeyboardInterrupt exception
        p = subprocess.Popen(
            ["vlc", "--play-and-exit", "--playlist-autostart", "--no-video", "--qt-start-minimized", songURL], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # WaveDrawer - constructor
        paddingSize = 0
        step = 1

        # WaveDrawer - draw
        while p.poll() == None:
            padding = str()
            for eachUnit in range(paddingSize):
                padding += ' '

            # if wave.hitLeftBorder():
            if paddingSize == 0:
                # wave.bounceOffFromLeftBorder()
                sign = "("
                step = 1

            # if wave.hitRightBorder():
            if paddingSize == 4:
                # wave.bounceOffFromRightBorder()
                sign = ")"
                step = -1

            # Encapsulate compound condition into a separate boolean function
            # if wave.goesForward():
            if paddingSize != 0 and paddingSize != 4 and step == 1:
                sign = "\\"

            # Encapsulate compound condition into a separate boolean function
            # if waveDrawer.goesBackward():
            if paddingSize != 0 and paddingSize != 4 and step == -1:
                sign = "/"

            print(padding + sign)
            paddingSize += step

            # PlaylistPlayer - play(Playlist) cont.
            time.sleep(1)

    # Option "--loop / --no-loop": when specified, shuffle again and play, otherwise stop at the end of the playlist
    #  default: enabled (--loop)
    print()
    print("============================================")
    print("Playback finished.")
    print("============================================")
    print()

if __name__ == "__main__":
    play()

