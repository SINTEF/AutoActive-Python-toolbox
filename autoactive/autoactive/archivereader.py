import zipfile as zp
from autoactive.autoactive.session import Session
from dataclasses import dataclass
import json

@dataclass(frozen=True)
class ArchiveOverview():
    id : str = None
    name : str = None

class ArchiveReader():

    def __init__(self, path):
        self.path = path
        self._file = zp.ZipFile(path, "r", allowZip64=True)
        self.overview = self.get_overview()


    def read(self, path):

        """ Method that accesses a member
            of the archive as a binary file-like object

        :arg
            path (str): can be either the name of a file
            within the archive or a ZipInfo object

        :returns
            original (zipfile): accessible member in the
            zipfile

        """

        original = self._file.open(path, "r")
        return original

    def list_ids(self):
        fnames = self._file.namelist()
        session_names = [fname.split("/")[0] for fname in fnames]
        return list(set(session_names))

    def get_metadata_name_from_id(self, id):
        elem_names = self._file.namelist()
        elem_name = [ename for ename in elem_names if id in ename and ".json" in ename]
        assert len(elem_name) == 1
        elem_name = elem_name[0]
        return elem_name

    def read_session_name_from_metadata(self, elem_name):
        name = self.read_metadata(elem_name)["user"]["name"]
        return name

    def read_metadata(self, elem_name):
        with self.open(elem_name) as file:
            metadata = json.load(file)
        return metadata

    def get_session_name_from_id(self,id):
        elem_name = self.get_metadata_fname_from_id(id)
        session_name = self.read_session_name_from_metadata(elem_name)
        return session_name

    def get_overview(self):
        archive_overview = list()
        ids = self.list_ids()
        for id in ids:
            name = self.get_session_name_from_id(id)
            archive_overview.append(ArchiveOverview(id, name))
        return archive_overview



