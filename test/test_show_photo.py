import os,sys,math
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage

def makeThumbs(imgdir,size=(100,100),subdir='thumbs'):
    thumbdir = os.path.join(imgdir,subdir)
    if not os.path.exists(thumbdir):
        os.mkdir(thumbdir)

    thumbs = []
    for imgfile in os.listdir(imgdir):
        thumbpath = os.path.join(thumbdir,imgfile)
        if os.path.exists(thumbpath):
            thumbobj = Image.open(thumbpath)
            thumbs.append((imgfile,thumbobj))
        else:
            print('making',thumbpath)
            imgpath = os.path.join(imgdir,imgfile)
            try:
                imgobj = Image.open(imgpath)
                imgobj.thumbnail(size,Image.ANTIALIAS)
                imgobj.save(thumbpath)
                thumbs.append((imgfile,imgobj))
            except:
                print("skipping:",imgpath)
    return thumbs

class ViewOne(Toplevel):
    def __init__(self,imgdir,imgfile):
        Toplevel.__init__(self)
        self.title(imgfile)
        imgpath = os.path.join(imgdir,imgfile)

        imgobj = PhotoImage(file = imgpath)
        Label(self,image=imgobj).pack()
        print(imgpath,imgobj.width(),imgobj.height())
        self.savephoto = imgobj

def viewer(imgdir, kind=Toplevel,cols=None):
    win = kind()
    win.title('Viewer:'+imgdir)


    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))

    savephotos = []
    rownum=0
    while thumbs:
        thumbsrow,thumbs = thumbs[:cols],thumbs[cols:]
        colnum=0
        for (imgfile,imgobj) in thumbsrow:
            size = max(imgobj.size)
            print (size)
            photo = PhotoImage(imgobj)
            link = Button(win,image = photo)
            handler = lambda savefile=imgfile:ViewOne(imgdir,savefile)
            link.config(command=handler)
            link.grid(row=rownum,column=colnum)
            savephotos.append(photo)
            colnum += 1
        rownum += 1
    quit = Button(win, text='Quit', command=win.quit, bg='beige').grid(columnspan=cols,stick=EW)
    return win,savephotos

if __name__ == '__main__':
    imgdir = (len(sys.argv)>1 and sys.argv[1]) or r'X:\图片\卡片'
    main,save = viewer(imgdir,kind=Tk)
    main.mainloop()