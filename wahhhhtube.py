import yt_dlp
import os
import subprocess
import time
import sys

# VIDEO SAVE PATH
SAVE_PATH = r"C:\_______________"
# FFMPEG\BIN PATH
FFMPEG_PATH = r"C:\_______________"  
# VLC PATH
VLC_PATH = r"C:\_______________"

# VIDEO LINK INPUT
link = input("Enter the YouTube video link: ")

# YT-DLP OPTIONS
ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # DOWNLOAD AT 1080P MAX
    'outtmpl': f"{SAVE_PATH}/%(title)s.%(ext)s",                      # FILE NAME OUTPUT
    'ffmpeg_location': FFMPEG_PATH,
    'postprocessors': [
        {   # AUDIO/VIDEO MERGE
            'key': 'FFmpegMerger',
        },
        {   # Converts the merged file to mp4 if needed
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Note: spelling here is 'preferedformat'
        }
    ],
}

with yt_dlp.YoutubeDL (ydl_opts) as ydl:
    video_metadata = ydl.extract_info(link, download=False)

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(link, download=True)
except: 
    pass

if os.path.isfile(f"{SAVE_PATH}/{video_metadata['title']}.webm"):
    subprocess.Popen([VLC_PATH, f"{SAVE_PATH}/{video_metadata['title']}.webm"])

# VIDEO FORMATS
elif os.path.isfile(f"{SAVE_PATH}/{video_metadata['title']}.mkv"):
    subprocess.Popen([VLC_PATH, f"{SAVE_PATH}/{video_metadata['title']}.mkv"])
elif os.path.isfile(f"{SAVE_PATH}/{video_metadata['title']}.mp4"):
    subprocess.Popen([VLC_PATH, f"{SAVE_PATH}/{video_metadata['title']}.mp4"])
elif os.path.isfile(f"{SAVE_PATH}/{video_metadata['title']}.mov"):
    subprocess.Popen([VLC_PATH, f"{SAVE_PATH}/{video_metadata['title']}.mov"])
else:
    print("WAHHHHHHHHHHHHHHHHH",file=sys.stderr)
    sys.exit(1)
