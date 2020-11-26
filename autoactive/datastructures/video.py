from autoactive.archive.file_object import Fileobject


class Video(Fileobject):

    """ Class containing information about a video file """

    def __init__(self):
        self.meta = {"type": "no.sintef.video", "version": 1}
        self.user = {}

    def toSerializable(self, **kwargs):

        """ Method which transforms the video object to a
        serializable object

        :arg
            **kwargs (dict): dictionary containing the archiveWriter
            uuid and the parent key

        :returns
            dict (dict): representing the video object as a dictionary

        """

        self.meta["time_scale"] = 1
        self.meta["start_time"] = 0
        self.meta["is_world_clock"] = False
        videoObjJson = super().toSerializable(**kwargs)
        return videoObjJson
