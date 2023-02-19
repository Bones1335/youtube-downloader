#! /usr/bin/python3
# youtubeDownloader.py - Download YouTube videos with URL

from pytube import YouTube
import pyperclip as pc

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been an error in downloading your youtube video.")
    print("Success! Your video has been downloaded!")

print("Put your YouTube link here!! URL: ")
link = pc.paste()

Download(link)