import PySimpleGUI as sg
from pathlib import Path
from youtube import download

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
    [sg.Text("Enter the URL of the YouTube video you want to Download", font=("Impact", 12))],
    [sg.InputText()],
    [sg.Text("Select the folder where you want to save the video", font=("Impact", 12))],
    [sg.InputText(key="-PATH-"), sg.FolderBrowse()],
    [sg.Text("\n")],
    [sg.Button("Download",size=(10,2),auto_size_button= True), sg.Button("Cancel",size=(10,2),auto_size_button= True)]
]

def main():
    window = sg.Window("YouTube Downloader", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        elif not(values) or values["-PATH-"] == "":
                sg.popup_ok("Please enter a valid URL and path!")
                continue
        elif event == "Download":
            url = values[1]
            path = values["-PATH-"]
            Path(path).mkdir(parents=True, exist_ok=True)
            sg.popup_no_wait("Please wait while we try to download your video")
            flag = download(url, path)
            if flag == -1:
                sg.popup_error("Error in downloading!")
            elif flag == 0:
                sg.popup("Download complete!")
            else:
                sg.popup_error("Internal error in Code!")
    window.close()

if __name__ == "__main__":
    main()