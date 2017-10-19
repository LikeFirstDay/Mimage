"""
初始化设置，
如果已经设置过了，跳过(ok)
"""
import shelve

class Conf:
    def __init__(self):
        self.db = shelve.open('./Conf/conf-shelve')
        if self.db.__len__() == 0:
            self.firstSet()

    def firstSet(self):
        self.db['test'] = 'test first db'
        self.db['height'] = 300
        self.db['width'] = 300
        self.db['title'] = 'Mimage'
        self.db['bg'] = 'light blue'
        self.db['side'] = 'top'
        self.db['svnuser'] = 'yangjun'
        self.db['svnpassword'] = 'qishi520'
    def get(self):
        return self.db

    def set(self):
        self.db.close()