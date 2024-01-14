import pytube
import os

def download(url, download_path):
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        
        video.download(download_path)
        return 1
    except:
        return 0


