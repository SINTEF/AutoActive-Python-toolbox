from autoactive.archive.fileobject import Fileobject


class Video(Fileobject):

    """ Class containing information about a video file """

    def __init__(self):
        super().__init__()
        self.meta.type = "no.sintef.video"
        self.meta.version = 1
        self.meta.time_scale = 1
        self.meta.start_time = 0
        self.meta.is_world_clock = False


