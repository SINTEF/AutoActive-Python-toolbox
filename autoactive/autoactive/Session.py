from datetime import datetime
from autoactive.archive.Dataobject import Dataobject
import uuid
import platform
import os
from autoactive.autoactive.AutoActivePythonVersion import Toolboxversion
from copy import copy

class Session(Dataobject):

    ''' Class containing information about the session '''

    _sessionFilename = 'AUTOACTIVE_SESSION.json'
    _sessionStateInit = 1
    _sessionStateUpdated = 2
    _sessionStateSaved = 3
    _sessionStateLoaded = 4
    _sessionStateTextArr = {'Init', 'Updated', 'Saved', 'Loaded'}


    def __init__(self, sessionName):
        self.user = dict()
        self.meta = {'type':'no.sintef.session', 'version':1}
        self.meta['id'] = 'Not saved'
        self.user['created'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.user['name'] = sessionName
        self.sessionState = self._sessionStateInit
        self.basedOn = dict()
        self.archiveFilename = 'Not saved'


    def save(self, archiveWriter):

        ''' Method saves the session object to the archive

        :arg
            archiveWriter (archiveWriter): object handle to
            archiveWriter

        '''

        self.meta['id'] = str(uuid.uuid4())
        self.meta['based_on'] = []

        [myPlatform, computername, username, addonstring, aaversion] = self.locDisplayPythonInformation()
        self.meta['enviroment'] = {}
        self.meta['enviroment']['platform'] = myPlatform
        self.meta['enviroment']['computername'] = computername
        self.meta['enviroment']['username'] = username
        self.meta['enviroment']['addons'] = addonstring
        self.meta['enviroment']['autoactive'] = aaversion

        enrichedFolders = copy(self)
        jsonStruct = enrichedFolders.replaceNatives(archiveWriter = archiveWriter, uuid = self.meta['id'])
        elemName = self.meta['id'] + '/' + self._sessionFilename
        archiveWriter.writeMetadata(elemName, jsonStruct)


    def locDisplayPythonInformation(self):

        ''' Method gets information about the enviroment

        :returns
            arr (list): Information about the enviroment
        '''

        myPlatform = platform.platform()
        computername = os.environ['COMPUTERNAME']
        username = os.getlogin()
        addonstring = ''
        aaversion = Toolboxversion()
        return [myPlatform, computername, username, addonstring, aaversion]


