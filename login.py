from tkinter import *
from tkinter import messagebox
from subprocess import call

def Ok():
    uname=e1.get()
    password=e2.get()

    if  ( uname=="" and password==""):
        messagebox.showwarning("Invalid","Blank not Allowed")
        return False
    elif (uname=="smehs" and password=="1234"):
        messagebox.showinfo("Logged in","Login Success")
        messagebox.showinfo("Message","Please Return to the IDLE")
        root.destroy()
        call(["python","LMS.py"])
        return True
    else:
        messagebox.showerror("","Incorrect Username and Password")
        return False

root=Tk()
root.title("Login Page")
root.geometry("300x200")
root.minsize(300,200)
root.maxsize(300,200)
# global e1
# global e2
Label(root,text="Username").place(x=10,y=10)
Label(root,text="Password").place(x=10,y=40)

e1=Entry(root)
e1.place(x=140,y=10)
e2=Entry(root)
e2.place(x=140,y=40)
e2.config(show="*")

Button(root,text="Login",command=Ok,height=2,width=10).place(x=10,y=90)



root.mainloop()
