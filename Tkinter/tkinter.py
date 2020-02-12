# Step5=>Function activation on btn click
from tkinter import *
root = Tk()
# define title
root.title('MyAPP')
# define size
root.geometry('300x300')
def fun():
    print('You clicked Me ')
btn=Button(root,text='Click me',command=fun)
btn.pack()
root.mainloop()