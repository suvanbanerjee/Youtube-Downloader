import PySimpleGUI as sg
import pathlib
from youtube import *

sg.theme("DarkBlue3")

layout = [
    [sg.Text("Enter the URL of the YouTube video you want to download")],
    [sg.InputText()],
    [sg.Text("Select the folder where you want to save the video")],
    [sg.InputText(key="-PATH-"), sg.FolderBrowse()],
    [sg.Button("Download"), sg.Button("Cancel")]
]

def main():
    window = sg.Window("YouTube Downloader", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        elif event == "Download":
            url = values[0]
            path = values["-PATH-"]

            pathlib.Path(path).mkdir(parents=True, exist_ok=True)
            flag = download(url, path)

            if flag == -1:
                sg.popup_error("Error in downloading!")
            elif flag == 0:
                sg.popup_error("Video not found!")
            else:
                sg.popup("Download complete!")

    window.close()

if __name__ == "__main__":
    main()
