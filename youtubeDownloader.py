#! /usr/bin/python3
# youtubeDownloader.py - Download YouTube videos with URL

from pytube import YouTube
import pyperclip as pc

LINK_CHECK = "https://www.youtube.com/"

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been an error in downloading your youtube video.")
    print("Success! Your video has been downloaded!")

while True:
    print("Pulling your YouTube link from the clipboard...")
    link = pc.paste()
    
    if LINK_CHECK not in link:
        input("You haven't provided a YouTube link. Please try again: ")
    else:
        Download(link)
        break
