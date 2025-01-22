import PySimpleGUI as sg
layout = [[sg.Text("Cik un kadas monetas nodot atlikumā?")],
          [sg.Text('Summa:',size=12),sg.InputText('',background_color='yellow',key='-a-',size=6)],
          [sg.Text("50 centu:",size=12),sg.InputText('',key='-b-',size=6)],
          [sg.Text("20 centu:",size=12),sg.InputText('',key='-c-',size=6)],
          [sg.Text("10 centu:",size=12),sg.InputText('',key='-d-',size=6)],
          [sg.Text("5 centu:",size=12),sg.InputText('',key='-e-',size=6)],
          [sg.Text("2 centu:",size=12),sg.InputText('',key='-f-',size=6)],
          [sg.Text('1 cents',size=12),sg.InputText('',key='-g-',size=6)],
          [sg.Button('Aprēķinat', key='s'),sg.Button('Beigt', key='q')]]

logs = sg.Window('KASE', layout)
while True:
    event, values = logs.read()
    if event == sg.WINDOW_CLOSED or event == 'q':
      break
    if event == 's':     
        a = int(values['-a-'])
        b = a // 50
        c = (a - b * 50)//20
        d = (a - b * 50 - c *20)//10
        e = (a - b * 50 - c *20 - d * 10)//5
        f = (a - b * 50 - c *20 - d * 10 - e * 5)//2
        g = (a - b * 50 - c *20 - d * 10 - e * 5 - f * 2)//1

        logs.find_element('-b-').update(b)
        logs.find_element('-c-').update(c)
        logs.find_element('-d-').update(d)
        logs.find_element('-e-').update(e)
        logs.find_element('-f-').update(f)
        logs.find_element('-g-').update(g)
