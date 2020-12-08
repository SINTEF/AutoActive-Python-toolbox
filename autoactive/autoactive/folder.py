from autoactive.archive.dataobject import Dataobject

from dataclasses import dataclass


@dataclass(init=False)
class Folder(Dataobject):
    def __init__(self):
        super().__init__()
        self.meta.type: str = "no.sintef.folder"
        self.meta.version: int = 1

    def from_serializable(self, archive_reader):
        assert False, "Not implemented"

    @classmethod
    def from_dict(cls, dict_, archive_reader):
        obj = Folder.__new__(cls)
        super().__init__(obj)
        obj.to_natives(dict_, archive_reader)
        return obj

