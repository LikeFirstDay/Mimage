from tkinter import *

def onMove(var):
    print('in onMove',var)



root = Tk()
var = IntVar()

c1 = Scale(root,label='c1',command=onMove,variable=var,from_=0,to=6,length=200,tickinterval=1,showvalue=YES,orient='horizontal').pack()
c2 = Scale(root,label='c2',command=onMove,variable=var,from_=0,to=6).pack()

root.mainloop()