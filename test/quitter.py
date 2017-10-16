"""
验证退出请求的Quit按钮；
复用、连接其他GUI的实例，并按要求重新封装
"""

from tkinter import *
from tkinter.messagebox import askokcancel
import math

class Quitter(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        widget = Button(self,text='Quit',command=self.quit)
        widget.pack(side=LEFT,expand=YES,fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit',"Really quit?")
        if ans: Frame.quit(self)

