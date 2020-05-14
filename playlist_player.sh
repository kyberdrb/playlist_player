#/bin/sh

PLAYLIST_ARG=$1
PLAYLIST=${PLAYLIST_ARG:="dnb_instrumental_no_vocals.m3u8"}

case $PLAYLIST in
    dnb)
        PLAYLIST="dnb_instrumental_no_vocals.m3u8"
        ;;
    house)
        PLAYLIST="house_instrumental_no_vocals.m3u8"
        ;;
    *)
        PLAYLIST=$PLAYLIST_ARG
        ;;
esac

vlc --play-and-exit --random --loop "$PLAYLIST"
