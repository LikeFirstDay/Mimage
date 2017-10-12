from tkinter import *
from PIL import ImageTk,Image
path = 'X:\\图片\\按钮\\'


photoimg = ImageTk.PhotoImage(file=path+'按钮.png')
Button(image=photoimg).pack()
Button.mainloop()
