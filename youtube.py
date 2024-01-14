import pytube


def download(url, path):
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        
        video.download(path)
        return 1
    except:
        return 0