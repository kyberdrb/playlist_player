from src.playlist import Playlist

def play():
    # PlaylistLoader - empty ctor/ctor(PlaylistFile)/ctor(YoutubePlaylist) - polymorphism? overload? - first overload, then polymorphism
    import sys
    playlistFile = "dnb_instrumental_no_vocals.m3u8"
    if len(sys.argv) >= 2:
        playlistFile = sys.argv[1]
        print("Argument provided:\t%s"% playlistFile)

    # PlaylistLoader - load(PlaylistFile playlistFile) - overload
    playlistItems = list()

    with open(playlistFile, "r") as playlist:
        print("Reading file:\t%s"% playlistFile)
        for line in playlist:
            if "www" in line:
                line = line.rstrip("\n")
                playlistItems.append(line)

    # PlaylistLoader - load(YoutubePlaylist youtubePlaylist) - overload
        import subprocess
        #youtube-dl --flat-playlist --dump-json https://www.youtube.com/playlist?list=UUREvOFg1F4bfZZqdmIJknrg | cut -d' ' -f4 | sed 's/[",]//g' | sed "s/^/https:\/\/www\.youtube\.com\/watch\?v=/g"

    # Playlist - shuffle()
    Playlist.shuffle(playlistItems)

    # Playlist - getAllPlaylistItems()
    for songURL in playlistItems:
        print(songURL)

    print()

    # PlaylistPlayer - play(Playlist)
    import time
    import subprocess
    for songURL in playlistItems:
        print(songURL)

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

# first encapsulate the rest of this file into a 'main()' method
# then add launch condition
if __name__ == "__main__":
    play()

