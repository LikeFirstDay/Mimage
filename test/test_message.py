from tkinter import *
from quitter import Quitter


root = Tk()
ent = Entry(root)
ent.insert(0,'Type words here')
ent.config(state=DISABLED,show='')
ent.pack(side=TOP,fill=X)

ent.focus()
ent.bind('<Return>',(lambda event: print('Input => "%s"' % ent.get())))

msg = Message(root,text='????')
msg.config(bg='pink',font=('times',16,'italic'))
msg.pack(fill=X,expand=YES)
root.mainloop()