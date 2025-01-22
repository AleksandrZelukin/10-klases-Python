from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x200+800+300')
root.title('Mans pirmais logs')


def atb():
	#atbilde2["text"] = atbilde.get()
	atbilde2.config(text=('Mans vards ',atbilde.get()))
    
info = Label(root,text="Sveiki, draugs! Ka tevi saus?",font=('Arial',18, 'bold'))
info.pack()

atbilde = Entry(root)
atbilde.pack(pady=20)


btn = Button(root, text='nospiež mani', command=atb)
btn.pack()

atbilde2 = Label(root,text='Mans vards',font='32')
atbilde2.pack()


btn2 = Button(root, text='Iziet no progrāmmas', bg='red', fg='yellow', command=root.destroy )
btn2.pack(side=BOTTOM)

root.mainloop()

'''
# Python program to create a close button
# using destroy Non-Class method
from tkinter import *

# Creating the tkinter window
root = Tk()
root.geometry("200x100")

# Button for closing
exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)

root.mainloop()
===========================================================

# Python program to create a close button
# using destroy Non-Class method
from tkinter import *

# Creating the tkinter window
root = Tk()
root.geometry("200x100")

# Function for closing window


def Close():
	root.destroy()


# Button for closing
exit_button = Button(root, text="Exit", command=Close)
exit_button.pack(pady=20)

root.mainloop()
==============================================================

# Python program to create a close button
# using destroy Class method
from tkinter import *

# Class for tkinter window


class Window():
	def __init__(self):

		# Creating the tkinter Window
		self.root = Tk()
		self.root.geometry("200x100")

		# Button for closing
		exit_button = Button(self.root, text="Exit", command=self.root.destroy)
		exit_button.pack(pady=20)

		self.root.mainloop()


# Running test window
test = Window()

====================================================================
# Python program to create a close button
# using destroy Class method
from tkinter import *

# Class for tkinter window


class Window():
	def __init__(self):

		# Creating the tkinter Window
		self.root = Tk()
		self.root.geometry("200x100")

		# Button for closing
		exit_button = Button(self.root, text="Exit", command=self.Close)
		exit_button.pack(pady=20)

		self.root.mainloop()

	# Function for closing window
	def Close(self):
		self.root.destroy()


# Running test window
test = Window()

========================================================================
# Python program to create a close button
# using quit method
from tkinter import *

# Creating the tkinter window
root = Tk()
root.geometry("200x100")

# Button for closing
exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)

root.mainloop()
exit(0)


'''