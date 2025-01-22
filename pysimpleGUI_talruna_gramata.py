import PySimpleGUI

izkartojums = [[PySimpleGUI.Text('Vārds')],
               [PySimpleGUI.InputText()],
               [PySimpleGUI.Text('Talruna numurs')],
               [PySimpleGUI.InputText('(+371)')],
               [PySimpleGUI.Button('Saglabāt', key='s'),PySimpleGUI.Button('Beigt', key='q')]]

logs = PySimpleGUI.Window('Virsrāksts', izkartojums)
phonebook={}
while True:
    event, values = logs.read()
    if event == PySimpleGUI.WINDOW_CLOSED or event == 'q':
      break
    if event == 's':
      phonebook[values[0]]=values[1]
      print(phonebook)