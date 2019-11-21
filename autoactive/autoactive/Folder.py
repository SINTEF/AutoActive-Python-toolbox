from autoactive.archive.Dataobject import Dataobject

class Folder(Dataobject):

    ''' Class containing information about the folder '''

    def __init__(self):
        self.user = dict()
        self.meta = {'type':'no.sintef.folder','version':1}



