from tkinter import *
states = []
def onPress(i):
    states[i] = not states[i]
    print(states)

root = Tk()
for i in range(10):
    chk = Checkbutton(root,text=str(i),command=(lambda i=i:onPress(i)))
    chk.pack(side=LEFT)
    states.append(False)
root.mainloop()
