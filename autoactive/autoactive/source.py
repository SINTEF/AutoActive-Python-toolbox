from autoactive.archive.file_object import Fileobject


class Source(Fileobject):

    """ Class containing information about the source file.
        Meaning information about the main python file """

    def __init__(self):
        self.meta = {"type": "no.sintef.source", "version": 1}
        self.user = dict()

    def addContentFromFileToArchive(self, fNameFull):

        """ Method which saves content from file to the aaz file.
            Inherits functionality from addContentFromFileToArchive
            in parent class

        :arg
            fNameFull (str) : The full path of the file

        :returns
            selfObj (source) : Returns the source object """

        selfObj = super().addContentFromFileToArchive(fNameFull)
        selfObj.user["language"] = "PYTHON"
        return selfObj
