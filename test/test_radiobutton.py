from tkinter import *
root = Tk()
var = StringVar()

def ss(event):
    print(var.get())
for i in range(10):
    rad = Radiobutton(root,text=str(i+1),variable=var,value=str(i)+'a')

    rad.pack(side=LEFT)
    rad.bind('<Button-1>', ss)

var.set(' ')
root.mainloop()