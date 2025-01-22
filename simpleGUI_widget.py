import PySimpleGUI as sg


layout = [[sg.Text('Sveiki, ka tev sauc?',size = (16,1)), sg.InputText()],
          [sg.Text('Kur tu dzivo',size = (15,1)), sg.InputText()],
          [sg.Text('',key='radit', size=(40))],
          [sg.Text('',key='sk', size=(40))],
          [sg.Multiline(size =(80,6),key = '_multiline_')],
          [sg.Button("Saglabāt datus", key='glab'),
           sg.Button("Skātit dati", key='skat'),
           sg.Button("Beigt", key='q')],]
  
logs = sg.Window('Mana pirma programma', layout)

while True:
    event, values = logs.read()
    if event == sg.WINDOW_CLOSED or event == 'q':
      break
    if event == 'skat':
        rez=[values[0],values[1]]
        logs['sk'].update(rez)
    if event == 'glab':
       logs['radit'].update('dati saglabāti')
       f = open("dati.txt","a")
       rez=[values[0],values[1]]
       print(rez, file=f)
       f.close()
       logs.FindElement('_multiline_').update(rez)
