import PySimpleGUI as sg 
import utils as ut

greetings = "Hii I'm Word-Bot I can help you with words\n"

layout = [
    [sg.Multiline(greetings , font=('Arial',10),size=(80,20),key='output',disabled=True)],
    [sg.Text('Enter Word:',font=('Arial',10)),sg.InputText('',font=('Arial',10),size=(50,1),key='input',enable_events=True)],
    [sg.Button('Meaning', font=('Arial',12), bind_return_key=True, key='meaning'),
    sg.Button('Synonyms', font=('Arial',12), key='synonym'),
    sg.Button('Antonyms',font=('Arial',12), key='antonym'),
    sg.Button('Clear', font=('Arial',12), key='clear')]
]

def display_error(msg):
    window['output'].print("ERROR: " + msg, text_color='red')

def display_meaning(word):
    meaning = ut.get_meaning(word)
    window['output'].print("WORD: " + word)
    if meaning:
        window['output'].print("MEANING: ", meaning)
    else:
        display_error("Word is not found in corpus")

def display_synonym(word):
    synonym = ut.get_synonyms(word)
    if synonym:
        window['output'].print('SYNONYM: ',synonym)
    else:
        display_error('Synonym of this word not founnd in corpus')

def display_antonym(word):
    antonym = ut.get_antonyms(word)
    if antonym:
        window['output'].print('ANTONYM: ',antonym)
    else :
        display_error('Antonym of this word not founnd in corpus')

def clear_all(texts):
    window.FindElement('output').Update(greetings)
    window.FindElement('input').Update(value='')

if __name__ == '__main__':
    window = sg.Window('Word Explorer', layout)

while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'meaning':
            display_meaning(values['input'])
        elif event == 'synonym':
            display_synonym(values['input'])
        elif event == 'antonym':
            display_antonym(values['input'])
        elif event == 'clear':
            clear_all(values['output'])
window.Close()