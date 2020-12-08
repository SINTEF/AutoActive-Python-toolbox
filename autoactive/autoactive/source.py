from autoactive.archive.fileobject import Fileobject

from dataclasses import dataclass


@dataclass
class Source(Fileobject):

    def __init__(self):
        super().__init__()
        self.meta.type: str = "no.sintef.source"
        self.meta.version: int = 1
        self.user.language: str = "PYTHON"

    def to_natives(self, arhive_reader):
        return self


