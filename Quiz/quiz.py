import PySimpleGUI as sg
import random
import sys as system

sg.theme('LightGrey1')

participants=open("./participants.csv","r")
questions=open("./questions.csv","r")
participants = participants.read().split("\n")
questions = questions.read().split("\n")

no_of_questions = 10

layout = [
    [sg.Text('\nQuiz Time\n', font='Helvetica 50 bold', justification='centre', expand_x=True)],
    [sg.Text('All the best\n', font='Helvetica 20', justification='center', expand_x=True)],
    [sg.Column([[sg.Button('Start', size=(5, 2), font='Helvetica 20')]], justification='center')],
]

window = sg.Window('Quiz', layout, finalize=True, resizable=True)
window.maximize()

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event:
        while no_of_questions!=0:
            partc = random.choice(participants)
            questc = random.choice(questions)
            participants.remove(partc)
            questions.remove(questc)

            layout2 = [
                [sg.Text('\n\nParticipant: ' + partc, font='Helvetica 50 bold', justification='center', expand_x=True)],
                [sg.Text('\n\nQuestion: ' + questc + '\n\n', font='Helvetica 40', justification='center', expand_x=True)],
                [sg.Column([[sg.Button('Next', size=(5, 2), font='Helvetica 20')],[sg.Button('Pass', size=(5, 2),button_color="red", font='Helvetica 20')]], justification='center')],
            ]

            token_window = sg.Window('Question', layout2, finalize=True, resizable=True)
            token_window.maximize()
            event, values = token_window.read()
            if event == sg.WINDOW_CLOSED or event == 'Next':
                token_window.close()
                no_of_questions-=1
            elif event== 'Pass':
                pass

        layout3 = [
            [sg.Text('\nCongratulations,\n You survived the quiz, Well Done!\n', font='Helvetica 40 bold', justification='centre', expand_x=True)],
            [sg.Text('Thank you for participating\n', font='Helvetica 20', justification='center', expand_x=True)],
            [sg.Column([[sg.Button('Byee', size=(5, 2), font='Helvetica 20')]], justification='center')]
        ]

        end_window = sg.Window('Byee', layout3, finalize=True, resizable=True)
        end_window.maximize()

        event, values = end_window.read()

        if event == sg.WINDOW_CLOSED or event == 'Byee':
            system.exit()

window.close()