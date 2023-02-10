#! /usr/bin/python3
# youtubeDownloader.py - Download YouTube videos with URL

from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been an error in downloading your youtube video.")
    print("Success! Your video has been downloaded!")

link = input("Put your YouTube link here!! URL: ") 
Download(link)