# App
from tkinter import * 
from tkinter import messagebox
import random




ans=['python','lucknow','italy','engineer','maths','automata','india','laptop','phone']
jmb=['yponth','ckluonw','altit','gieneren','tsham','mautota','idani','ptlapo','openh']
sc=['1','2','3','4','5','6','7','8','9']

logic = random.randrange(0,10,1)

def fun():
    global ans,jmb,logic,sc
    lb1.config(text=jmb[logic])

def checkans():
    global ans,jmb,logic,sc
    var = e1.get()
    counter=-1
    if(var == ans[logic]):
        messagebox.showinfo('Good','Right Answer Dude')
        reset()
    else:
        messagebox.showerror('oops','Wrong Answer')
        e1.delete(0,END)

def reset():
    global ans,jmb,logic,sc
    logic=random.randrange(0,10,1)
    lb1.config(text=jmb[logic])
    e1.delete(0,END)


root=Tk()
root.geometry('300x400')
root.title('Jumbled Word App')

lb1=Label(
root,
text='Play Game',
font=('Verdana',18),
)
lb1.pack(pady=30)


# collect
# userans = StringVar()
e1 = Entry(
root,
font=('Verdana',15),
# textvariable = userans
)
e1.pack(pady=30)

btnchk=Button(
root,
text='Check',
font = ('Cursive',12),
width='14',
bg='Blue',
fg='White',
relief=GROOVE,
command=checkans
)
btnchk.pack(pady=20)

btnrst=Button(
root,
text='Reset',
font = ('Cursive',12),
width='14',
bg='Red',
fg='White',
relief=GROOVE,
command=reset
)
btnrst.pack()


# calling function
fun()
root.mainloop()