from Tkinter import *
import sys

def command1():
	if entry1.get() =='admin' and entry2.get() =='password' or entry1.get() =='test' and entry2.get() =='pass':
		root.deiconify()
		top.destroy()

def command2():
	top.destroy()
	root.destroy()
	sys.exit()

root=Tk()
top = TopLevel()

top.geometry('300*260')
top.title('Login screen')
top.configure(backgroud='white')
photo2 = PhotoImage(file='1.gif')
photo = Label(top, images=photo2, bg='white')
lbl1 = Label(top, text='Username:', font=('Helvetica',10))
entry1 = Entry(top)
lbl2 = Label(top, text='Password:', font=('Helvetica',10))
entry2 = Entry(top, show="*")
button2 = button(top, text='cancel', command=lambda:command2())

entry3.bind('<Return>', command1)

lbl = Label(top, text='Copyright Bonnie Login screen 2020', font='Arial'9)

photo.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl3.pack()

root.title('Main Screen')
root.configure(backgroud='white')
root.geometry('860*650')

root.withdraw()
root.mainloop()