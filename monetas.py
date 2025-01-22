import PySimpleGUI as sg
layout = [[sg.Text("Cik nodot atlikumā?")],
          [sg.InputText('',size=6)],
          [sg.Text('',key='radit')],
          [sg.Multiline(size =(60,6),key = '_multiline_')],
          [sg.Button('Aprēķinat', key='s'),sg.Button('Beigt', key='q')]]

logs = sg.Window('KASE', layout)
# a = int(input("Atlikuma summa:  "))
atlikums = {}
while True:
    event, values = logs.read()
    if event == sg.WINDOW_CLOSED or event == 'q':
      break
    if event == 's':     
        a = int(values[0])
        b = a // 50
        c = (a - b * 50)//20
        d = (a - b * 50 - c *20)//10
        e = (a - b * 50 - c *20 - d * 10)//5
        f = (a - b * 50 - c *20 - d * 10 - e * 5)//2
        g = (a - b * 50 - c *20 - d * 10 - e * 5 - f * 2)//1
        # print("(50 centu)", b )
        # print("(20 centu)", c)
        # print("(10 centu)", d )
        # print("(5 centu)", e )
        # print("(2 centu)", f )
        # print("(1 centu)", g )
        # print("control:  ", b*50 + c*20 + d*10 + e*5 + f*2 + g)
        atlikums["50 centu:"]=b
        atlikums["20 centu:"]=c
        atlikums["10 centu:"]=d
        atlikums["5 centu:"]=e
        atlikums["2 centu:"]=f
        atlikums["1 centu:"]=g
        logs['radit'].update(atlikums)
        logs.FindElement('_multiline_').update(atlikums)
# a = int(input("Get coins:  "))
# b = a // 25
# c = (a - b * 25)//10
# d = (a - b * 25 - c *10)//5
# e = (a - b * 25 - c *10 - d * 5)//1
# print("Quarter (25с)", b )
# print("Disme (10с)", c)
# print("Nickel (5с)", d )
# print("Penny (1с)", e )
# print("control:  ", b*25 + c*10 + d*5 + e)