"""
开始做GUI工具
使用的tkinter模块
主要的需求：
可复用，框架，
"""

#解决第一次设置的问题
import tkinter
import os
from Conf.Conf import Conf
from Component import GetComponent

def main():
    conf = Conf()
    db = conf.get()
    root = tkinter.Tk()
    root.title(db['title'])

    GetAllC = GetComponent.AllComponent(mod_Tk=tkinter,mod_os=os,db=db)
    frame = GetAllC.getFrame(root,db['bg'],db['height'],db['width'])
    frame1 = GetAllC.getFrame(root, db['bg'])
    GetAllC.getEnt(frame)   #输入框




    root.mainloop()
    conf.set()



if __name__ == '__main__':
    main()