# registration form in python tkinter frame
from tkinter import *
root=Tk()

#resizing the screen

root.geometry("520*520")
root.title("Registration Form")

#assigning colors by use of fg

w=Label(root,text="Username",font=("Bold",20),fg="blue")
w.place(x=160,y=20)

#label the username

w=Label(root,text="Username",font=("Bold",10))
w.place(x=30,y=100)

#iput box

w.Entry(root, width=20,font=("italic",16))
w.place(x=120,y=100)

#label the password

w=Label(root,text="Password",font=("Bold",10))
w.place(x=30,y=140)

#iput box

w.Entry(root, width=20,font=("italic",16))
w.place(x=120,y=140)

#label the email

w=Label(root,text="Email",font=("Bold",10))
w.place(x=30,y=180)

#iput box

w.Entry(root, width=20,font=("italic",16))
w.place(x=120,y=180)


#adding checkbox
#label the password

w=Label(root,text="Status",font=("Bold",10))
w.place(x=30,y=220)

var1=IntVar()
Checkbutton(root,text="Married",variable=var1,fg="brown",font=("italic",13)).place(x=107,y=220)
var2=IntVar()
Checkbutton(root,text="Single",variable=var2,fg="brown",font=("italic",13)).place(x=250,y=220)

#adding radio button
w.label(root,text="Gender",font=("bold",11))
w.place(x=30,y=260)
#radio button we use only one IntVar() unlike in checkbox
var=IntVar()
Radiobutton(root,text="Male",fg="brown",font=("italic",13),variable=var,value=1).place(x=107,y=260)
Radiobutton(root,text="Female",fg="brown",font=("italic",13),variable=var,value=2).place(x=240,y=260)
 

#adding button

w=Button(root,text="SignUp",font=("bold",12),bg="white")
w.place(x=160,y=360)






#close tkinter

root.mainloop()
