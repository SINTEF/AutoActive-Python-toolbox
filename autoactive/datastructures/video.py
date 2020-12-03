from autoactive.archive.fileobject import Fileobject


class Video(Fileobject):

    """ Class containing information about a video file """

    def __init__(self):
        super().__init__()
        self.meta.type = "no.sintef.video"
        self.meta.version = 1

    def toSerializable(self, **kwargs):

        """ Method which transforms the video object to a
        serializable object

        :arg
            **kwargs (dict): dictionary containing the archiveWriter
            uuid and the parent key

        :returns
            video_obj_json (dict): representing the video object as a dictionary

        """

        self.meta.time_scale = 1
        self.meta.start_time = 0
        self.meta.is_world_clock = False
        video_obj_json = super().toSerializable(**kwargs)
        return video_obj_json
