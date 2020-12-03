from autoactive.archive.dataobject import Dataobject

from dataclasses import dataclass


@dataclass(init=False)
class Folder(Dataobject):
    def __init__(self):
        super().__init__()
        self.meta.type: str = "no.sintef.folder"
        self.meta.version: int = 1
