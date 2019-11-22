import os
from datetime import datetime

class FileInfo():

    ''' Class gets information about specific file

    :arg
        fNameFull (str): Full path to file

    '''

    def __init__(self, fNameFull):

        self._fileInfo = {'name': str,
                        'folder': str,
                        'date': str,
                        'bytes': int,
                        'isdir': int,
                        'datenum': int}

        stats = os.stat(fNameFull)
        mtime = stats.st_mtime

        self._fileInfo['name'] = os.path.basename(fNameFull)
        self._fileInfo['folder'] = os.path.dirname(fNameFull)
        self._fileInfo['date'] = datetime.fromtimestamp(mtime).strftime('%Y-%b-%d %H:%M:%S')
        self._fileInfo['bytes'] = stats.st_size
        self._fileInfo['isdir'] = os.path.isdir(fNameFull)
        self._fileInfo['datenum'] = datetime.fromtimestamp(mtime).toordinal() + 366



    def getFileInfo(self):
        ''' Method returns fileInfo

        :returns
            self._fileInfo (dict): The information about
            the file

        '''

        return self._fileInfo




