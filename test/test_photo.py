path = r'X:\图片\\'

from tkinter import *
from glob import glob
import random

def draw():
    name,photo=random.choice(igm)
    lbl.config(text=name)
    pix.config(image=photo)


win =Tk()
lbl = Label(win,text="none",bg='blue',fg='red')
pix = Button(win,text="Press me",command=draw,bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)

files = glob(path+'*.gif')
igm = [(x,PhotoImage(file=x)) for x in files ]
print(files)


win.mainloop()