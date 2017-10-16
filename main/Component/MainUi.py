"""
主UI界面
"""

class MainUi:
    def __init__(self,module=None,parent=None):
        self.frame = module.Frame(parent)
        self.ent = module.Entry(self.frame)
        self.ent.insert(0,'get something')
        self.ent.pack(side='top',fill='x')
        self.ent.focus()
        self.ent.bind('<Return>',(lambda event:print(self.ent.get())))