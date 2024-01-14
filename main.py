import PySimpleGUI as sg
import pathlib
from youtube import *


sg.theme("DarkBlue3")  # Make it according to your choice

layout = [
    [sg.Text("Enter the URL of the YouTube video you want to download")],
    [sg.InputText()],
    [sg.Text("Enter the path where you want to save the video")],
    [sg.InputText()],
    [sg.Button("Ok"), sg.Button("Cancel")]
] # This is the layout of the GUI if you want to change it, go ahead


def main():
    '''
    this is the main function in python the concept of main function is not there
    but it is a good practice to write the main function
    '''
    window = sg.Window("YouTube Downloader", layout)
    while True:
        event, values = window.read()
        if event == "Ok":
            url = values[0]
            path = values[1]

            pathlib.Path(path).mkdir(parents=True, exist_ok=True)
            flag = download(url, path)
            if flag == -1:
                sg.popup("Error in downloading!")
            elif flag == 0:
                sg.popup("Video not found!")
        elif event == sg.WINDOW_CLOSED or event == "Cancel":
                window.close()
                break


if __name__ == "__main__":
    """if the file is run directly then the __name__ variable is set to __main__
    if the file is imported then the __name__ variable is set to the name of the file"""
    main() # Main function is called here