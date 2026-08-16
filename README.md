# lyric-importer
import lyrics for local flac files

- recursively searching subdirectories is mostly working
- added functionality to view lyrics (since sometimes lyric provider will apply incorrect lyrics in cases where several songs with the same name exist)
    - now added further functionality to skip all lyrics or show all lyrics, since otherwise y or n would need to be pressed for every song in the directory
work in progress

known issues
- some issues with syncing timestamps to lyrics (not in my control)
- not autoapplying lyrics to flac (in progress)
