from autoactive.archive.dataobject import Dataobject
from autoactive.toolboxinfo import toolbox_version


from datetime import datetime
from dataclasses import dataclass
import uuid
import platform
import os


@dataclass(init=False)
class Session(Dataobject):
    def __init__(self, session_name: str = None):
        super().__init__()
        self.meta.type = "no.sintef.session"
        self.meta.version = 1
        self.user.created = (
            datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+01:00"
        )
        self.user.name = session_name

    def save(self, archive_writer):

        """ Method saves the session object to the archive

        :arg
            archive_writer (ArchiveWriter): object handle to
            archiveWriter

        """

        self.meta.id = str(uuid.uuid4())
        self.meta.based_on = []
        self.meta.enviroment = Enviroment().__dict__
        json_struct = self.replace_natives(
            archive_writer=archive_writer, uuid=self.meta.id
        )
        elem_name = f"{self.meta.id}/AUTOACTIVE_SESSION.json"
        archive_writer.write_metadata(elem_name, json_struct)

    def to_natives(self):
        assert False, "not implemented"




@dataclass()
class Enviroment:

    """Class containting information about the computer enviroment"""

    platform: str = platform.platform()
    computername: str = os.environ["COMPUTERNAME"]
    username: str = os.getlogin()
    addonstring: str = ""
    aaversion: str = toolbox_version
