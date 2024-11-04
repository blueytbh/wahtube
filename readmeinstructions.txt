FIRST MAKE SURE PYTHON IS INSTALLED

WHEN IT'S INSTALLED, GO TO YOUR TERMINAL AND EXECUTE THE FOLLOWING COMMAND: "pip install yt-dlp"

INSTALL FFMPEG AND VLC

VLC: (https://www.videolan.org/vlc/)

FFMPEG: (https://github.com/BtbN/FFmpeg-Builds/releases)

VLC SHOULD BE SAVED LIKE "\VIDEOLAN\VLC\vlc.exe\" (list the exe file)

FFMPEG SHOULD BE SAVED LIKE "wherever_ffmpeg_is\bin\" (do not list any exe file)

FIND THESE 6 LINES OF CODE IN WAHHHHTUBE.PY AND DELETE THE "_______________" AND REPLACE IT WITH YOUR VLC, FFMPEG, AND VIDEO SAVE PATH. 

# VIDEO SAVE PATH
SAVE_PATH = r"C:\_______________"
# \FFMPEG\BIN\ PATH
FFMPEG_PATH = r"C:\_______________"  
# VLC PATH
VLC_PATH = r"C:\_______________"
