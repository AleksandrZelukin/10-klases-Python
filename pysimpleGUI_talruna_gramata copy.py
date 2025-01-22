from PySimpleGUI import Text, InputText,Button,Window,WINDOW_CLOSED
import csv

izkartojums = [[Text('Vārds')],
               [InputText(key='-vards-')],
               [Text('Talruna numurs')],
               [InputText('(+371)',key='-num-')],
               [Button('Saglabāt', key='s'),Button('Beigt', key='q')]]

win = Window('Virsrāksts', izkartojums)
phonebook=[]
while True:
    event, values = win.read()
    if event == WINDOW_CLOSED or event == 'q':
      break
    if event == 's':
      # phonebook[values[0]]=values[1]
      # print(phonebook)
      # phonebook.append(values[0])
      # phonebook.append(values[1])
      with open('talruna_gramata.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow({values["-num-"],values["-vards-"]})

