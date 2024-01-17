import pytube
import re

def download(url: str, path: str) -> int:
    playlist=r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/playlist(.*)$"
    video=r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/(watch|shorts)(.*)$"
    if re.match(playlist, url):
        playlist = pytube.Playlist(url)
        for video in playlist.videos:
            video.streams.get_highest_resolution().download(path)
            return 0
    elif re.match(video, url):
        video = pytube.YouTube(url)
        video.streams.get_highest_resolution().download(path)
        return 0
    else:
        return -1