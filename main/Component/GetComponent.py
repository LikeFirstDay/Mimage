"""
主UI界面
"""
class AllComponent:
    def __init__(self,mod_Tk=None,mod_os=None,db=None):
        self.mod_Tk = mod_Tk
        self.mod_os = mod_os
        self.db = db
        self.command = \
            {
                'up':self.__svn_up,
            }

    def getFrame(self,parent=None,bg='light blue', height=400, width=400,side='top',expand='yes',fill='both'):
        self.frame = self.mod_Tk.Frame(parent,bg=bg, height=height, width=width)
        self.frame.pack(side=side, expand=expand, fill=fill)
        return self.frame

    def getEnt(self,parent=None,side='top',fill='x',expand='yes'):
        self.ent = self.mod_Tk.Entry(parent)
        self.ent.pack(side=side, fill=fill, expand=expand)
        self.ent.focus()
        self.ent.bind('<Return>', self.EntEvent)
        return self.ent

    def EntEvent(self,event):
        command = self.ent.get().split(' ')
        if len(command)==1:
            self.command[command]()
        else:
            self.command[command[0]](command[0:])

    def __svn_up(self,args):
        for i in args:
            self.mod_os.system('svn update {路径} {帐号} {密码}'.format(i,self.db['svnuser'],self.db['svnpassword']))
        print('ss')