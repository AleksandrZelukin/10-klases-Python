from tkinter import *

a = Tk()
a.title("Manas pogas")
a.geometry("300x300+800+400")

entry = Entry(font="32")
entry.pack()
label50 = Label()
label50.pack()
label20 = Label()
label20.pack()
label10 = Label()
label10.pack()
label5 = Label()
label5.pack()
label2 = Label()
label2.pack()
label1 = Label()
label1.pack()

def display():
    a = int(entry.get())//50
    b = (int(entry.get())-a*50)//20
    c = (int(entry.get())-a*50-b*20)//10
    d = (int(entry.get())-a*50-b*20-c*10)//5
    e = (int(entry.get())-a*50-b*20-c*10-d*5)//2
    f = (int(entry.get())-a*50-b*20-c*10-d*5-e*2)//1
    label50["text"] = ("50 centu monetas: ",a)
    label20["text"] = ("20 centu monetas: ",b)
    label10["text"] = ("10 centu monetas: ",c)
    label5["text"] = ("5 centu monetas: ",d)
    label2["text"] = ("2 centu monetas: ",e)
    label1["text"] = ("1 centu monetas: ",f)
    
def clear():
    entry.delete(0, END)
    label50["text"] = entry.get()
    label20["text"] = entry.get()
    label10["text"] = entry.get()   
    label5["text"] = entry.get()
    label2["text"] = entry.get()
    label1["text"] = entry.get()
       


# def calculate_coins(amount):
#     coins = [50, 20, 10, 5, 2, 1]
#     result = []
#     for coin in coins:
#         count = amount // coin
#         amount -= count * coin
#         result.append(count)
#     return result

# def display():
#     amount = int(entry.get())
#     counts = calculate_coins(amount)
#     labels = [label50, label20, label10, label5, label2, label1]
#     for label, count in zip(labels, counts):
#         label["text"] = f"{label.cget('text').split(':')[0]}: {count}"
        
btn1 = Button(a, text="ievads", command=display)
btn2 = Button(a, text="notirit", command=clear)
btn3 = Button(a, text="iziet", command=exit)
btn1.place(relx=.2, rely=.8)
btn2.place(relx=.4, rely=.8)
btn3.place(relx=.6, rely=.8)


a.mainloop()