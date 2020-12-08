from autoactive.archive.dataobject import Dataobject
from autoactive.autoactive.folder import Folder
from autoactive.datastructures.fileinfo import Fileinfo

from dataclasses import dataclass
from pathlib import Path


@dataclass(init=False)
class Fileobject(Dataobject):
    def __init__(self):
        super().__init__()
        self.type: str = None
        self.version: int = None
        self.meta.write_type: str = None

    def add_content_from_file_to_archive(self, fname):

        """ Method saving content from file to the aaz file.

        Args:
            fname (Path) : The full path of the file

        Returns:
            self (Source) : Returns the source object """

        self.user.file_name_full = str(fname)
        file_details = Fileinfo(fname)
        self.user.file_details = self.dataclass_to_folder(file_details)
        self.meta.write_type = "from_file"
        return self

    def dataclass_to_folder(self, data) -> Folder:

        """ Method which transforms dictionary to folder

        :arg
            data (Datatable): data to be transformed

        :returns
            folder (Folder): folder object

        """

        folder = Folder()
        folder.user.__dict__ = data.__dict__
        return folder

    def to_serializable(self, **kwargs):
        elem_path = f"{self.user.file_details.user.folder}\\{self.user.file_details.user.name}"
        path = f"{kwargs['uuid']}/{kwargs['parent_key']}/{self.user.file_details.user.name}"
        self.meta.attachments = [f"/{kwargs['parent_key']}/{self.user.file_details.user.name}"]
        kwargs["archive_writer"].copy_content_from_file(elem_path, path)
        meta = self.meta.__dict__
        user = self.meta.__dict__
        return {"meta":meta, "user":user}

