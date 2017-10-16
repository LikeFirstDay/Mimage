from tkinter import *
root = Tk()
mbutton = Menubutton(root,text = 'Food')
picks = Menu(mbutton)
mbutton.config(menu=picks)
picks.add_command(label='quit',command = root.quit)
mbutton.pack()
mbutton.config(bg='white',bd=4,relief=RAISED)
root.mainloop()