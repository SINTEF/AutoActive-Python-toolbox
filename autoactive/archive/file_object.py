from autoactive.archive.data_object import Dataobject
from autoactive.datastructures.file_info import FileInfo
import os
import numpy as np
from autoactive.autoactive.folder import Folder


class Fileobject(Dataobject):

    """ Parent class for all file objects (such as video and source)
        Note that fileobjects also are dataobjects."""

    def __init__(self):
        self.type = str()
        self.version = np.nan
        self.meta = dict()
        self.user = dict()
        self.read_delayed = True
        self.fileText = "No text added"
        self.meta["write_type"] = "none"
        self._extension = "genfile"
        self._origName = "noname"
        self._aaElemNameFullPath = ""

    def addContentFromFileToArchive(self, fNameFull):

        """ Method saving content from file to the aaz file.

        Args:
            fNameFull (str) : The full path of the file

        Returns:
            selfObj (source) : Returns the source object """

        self.user["file_name_full"] = fNameFull
        self._origName = os.path.basename(fNameFull)
        fileInfo = FileInfo(fNameFull)
        f = fileInfo.getFileInfo()
        fObj = self.newFolderFromDict(f)
        self.user["file_details"] = fObj
        self.meta["write_type"] = "from_file"
        return self

    def newFolder(self):

        """ Method creating a new folder object

        Returns:
            Folder object

        """

        return Folder()

    def newFolderFromDict(self, dict):
        """ Method which transforms dictionary to folder

        :arg
            dict (dict): dictionary to be transformed

        :returns
            fObject (folder): folder object

        """
        fObj = self.newFolder()
        for key, values in dict.items():
            fObj.user[key] = values
        return fObj

    def toSerializable(self, **kwargs):

        """ Method which transforms the fileobject to a
        serializable object

        :arg
            **kwargs (dict): dictionary containing the archiveWriter
            uuid and the parent key

        :returns
            dict (dict): representing the fileobject as a dictionary

        """

        file_detailts = self.user["file_details"].toSerializable(**kwargs)
        path = "/" + kwargs["parentKey"] + "/" + file_detailts["user"]["name"]
        self.meta["attachments"] = [path]
        kwargs["archiveWriter"].writeCopyContentFromFile(
            file_detailts["user"]["folder"] + "\\" + file_detailts["user"]["name"],
            kwargs["uuid"] + path,
        )
        self.user["file_details"] = file_detailts
        return {"meta": self.meta, "user": self.user}
