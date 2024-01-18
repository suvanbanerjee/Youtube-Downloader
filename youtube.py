import pytube
import re

def download(url, path, quality):
    playlist=r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/playlist(.*)$"
    video=r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/(watch|shorts)(.*)$"
    if re.match(playlist, url):
        playlist = pytube.Playlist(url)
        for video in playlist.videos:
            if quality == "High":
                video.streams.get_highest_resolution().download(path)
            elif quality == "Low":
                video.streams.get_lowest_resolution().download(path)
            return 0
    elif re.match(video, url):
        video = pytube.YouTube(url)
        if quality == "High":
            video.streams.get_highest_resolution().download(path)
        if quality == "Low":
            video.streams.get_lowest_resolution().download(path)
        return 0
    else:
        return -1