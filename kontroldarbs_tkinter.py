import tkinter as tk

root = tk.Tk()
root.title("Tkinter piemērs")

label = tk.Label(root, text="Ievadi tekstu:")
label.pack()

entry = tk.Entry(root)
entry.pack()

def show_text():
    label.config(text=entry.get())

button = tk.Button(root, text="Parādīt", command=show_text)
button.pack()

root.mainloop()