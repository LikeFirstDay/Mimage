from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage

path = 'X:\\图片\\按钮\\'

root = Tk()
photoimg = ImageTk.PhotoImage(file=path+'按钮.png')
print(photoimg.width(),photoimg.height())
Button(root,image=photoimg).pack()
root.mainloop()
