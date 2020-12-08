from autoactive.archive.fileobject import Fileobject

from dataclasses import dataclass


@dataclass
class Source(Fileobject):

    def __init__(self):
        super().__init__()
        self.meta.type: str = "no.sintef.source"
        self.meta.version: int = 1
        self.user.language: str = "PYTHON"

    def from_serializable(self, archive_reader):
        return self

    @classmethod
    def from_dict(cls, dict_, archive_reader):
        obj = Source.__new__(cls)
        super().__init__(obj)
        obj.to_natives(dict_, archive_reader)
        return obj



