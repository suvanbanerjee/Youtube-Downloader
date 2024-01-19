import PySimpleGUI as sg
from pathlib import Path
import pytube
import re

sg.LOOK_AND_FEEL_TABLE['YouTube'] = \
{'BACKGROUND': '#FFFFFF', 
'TEXT': '#000000', 
'INPUT': '#FFFFFF', 
'TEXT_INPUT': '#000000', 
'SCROLL': '#000000', 
'BUTTON': ('#FF0000', '#FFFFFF'), 
'PROGRESS': ('#FF0000', '#FFFFFF'), 
'BORDER': 1, 'SLIDER_DEPTH': 0,  
'PROGRESS_DEPTH': 0 } 
sg.theme('YouTube') 

layout = [
    [sg.Image(str(Path(__file__).parent.joinpath("logo.png")), size=(400, 200),subsample=5,)],
    [sg.Text("Enter the URL of the YouTube video/playlist you want to Download", font=("Impact", 12))],
    [sg.InputText()],
    [sg.Text("Select Video Quality", font=("Impact",12))],
    [sg.Combo(["High", "Low"], size=(10, 10), key='-COMBO-')],
    [sg.Text("Select the folder where you want to save the video", font=("Impact", 12))],
    [sg.InputText(key="-PATH-"), sg.FolderBrowse()],
    [sg.Text("\n")],
    [sg.Button("Download",size=(10,2),auto_size_button= True), sg.Button("Cancel",size=(10,2),auto_size_button= True)]
]


def download(url, path, quality):
    playlist=r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/playlist(.*)$"
    video=r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/(watch|shorts)(.*)$"
    if re.match(playlist, url):
        playlist = pytube.Playlist(url)
        for video in playlist.videos:
            sg.popup_no_wait("Video no " + str(playlist.video_urls.index(url)+1) + " downloding...")
            video.streams.first().download(path)
        return 0
        # if quality == "High":
        #     video.streams.get_highest_resolution().download(path)
        # if quality == "Low":
        #     video.streams.get_lowest_resolution().download(path)
        # return 0
    else:
        return -1

def main():
    window = sg.Window("YouTube Downloader", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        elif not(values) or values["-PATH-"]  == "" or values["-COMBO-"] == "":
                sg.popup_ok("Please enter a valid URL and path!")
                continue
        elif event == "Download":
            url = values[1]
            path = values["-PATH-"]
            quality=values["-COMBO-"]
            Path(path).mkdir(parents=True, exist_ok=True)
            sg.popup_no_wait("Please wait while we try to download your video")
            flag = download(url, path, quality)
            if flag == -1:
                sg.popup_error("Error in downloading!")
            elif flag == 0:
                sg.popup("Download complete!")
            else:
                sg.popup_error("Internal error in Code!")
    window.close()

if __name__ == "__main__":
    main()