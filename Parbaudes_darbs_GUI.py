import PySimpleGUI as sg

sg.theme('SandyBeach')
layout = [[sg.Text('Sveiki, ka tev sauc?',size = (16,1)), sg.InputText(size=20)],
          [sg.Text('Kur tu dzivo',size = (16,1)), sg.InputText(size=20)],
          [sg.Text('',key='radit', size=(40))],
          [sg.Text('',key='sk', size=(40))],

          [sg.Button("Saglabāt datus", key='glab'),
           sg.Button("Skātit dati", key='skat'),
           sg.Button("Beigt", key='q')],]
  
logs = sg.Window('Mans Parbaudes darbs', layout)

while True:
    event, values = logs.read()
    if event == sg.WINDOW_CLOSED or event == 'q':
      break
    if event == 'skat':
        rez=[values[0],values[1]]
        logs['sk'].update(rez)
    if event == 'glab':
       logs['radit'].update('dati saglabāti')
       f = open("dati.txt","a",encoding="utf-8")
       rez=[values[0],values[1]]
       print(rez, file=f)
       f.close()
