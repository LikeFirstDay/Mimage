from tkinter import *

root = Tk()

ent = Entry(root)
ent.pack()
var = StringVar()
ent.config(textvariable=var)
var.set('enter here')

root.mainloop()