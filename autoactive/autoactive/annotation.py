import json
from os import path
from dataclasses import dataclass
import numpy as np

from autoactive.archive.dataobject import Dataobject
from autoactive.autoactive.archivewriter import ArchiveWriter


@dataclass(init=False)
class Annotation(Dataobject):

    def __init__(self):
        super().__init__()
        self.meta.type = "no.sintef.annotation"
        self.meta.version = '1.0.0'
        self.meta.AutoActiveType = 'Annotation'
        self.user.annotations = list()
        self.user.annotationInfo = {}
        self.user.isWorldSynchronized = False

    def addAnnotation(self, timestamp, annotationId: int):
        if isinstance(timestamp, np.int32) or isinstance(timestamp, np.int64):
            timestamp = int(timestamp)
        if isinstance(timestamp, np.float32) or isinstance(timestamp, np.float64):
            timestamp = int(timestamp)
        self.user.annotations.append({"timestamp": timestamp,
                                      "type": annotationId})

    def setAnnotationInfo(self, annotationId: int, name: str, tag: str, comment: str):
        self.user.annotationInfo[annotationId] = {'name': name,
                                                  'tag': tag,
                                                  'comment': comment}

    def toJsonStructRec(self, sessionId: str, archiveWriter: ArchiveWriter):
        # annotations are stored in a separate file
        fileName = path.join(sessionId, 'Annotations\\Annotations.json')

        # TODO: assert that all annotationInfo entries are type char (necessary?)

        annotationsDict = {'AutoActiveType': self.meta.AutoActiveType,
                           'is_world_synchronized': self.user.isWorldSynchronized,
                           'version': self.meta.version,
                           'annotation_info': self.user.annotationInfo,
                           'annotations': self.user.annotations
                           }
        archiveWriter.write_metadata(fileName, annotationsDict)
        self.user.__delattr__('annotations')
        self.user.__delattr__('annotationInfo')
        self.user.__delattr__('isWorldSynchronized')
        self.meta.attachments = ['/Annotations/Annotations.json']

    def from_serializable(self, archive_reader):
        """ Method which transforms the serializable object to an
        annotation-instance

        :arg
            archive_reader (ArchiveReader): Object for reading data
            from aaz file

        :returns
            self (Annotation): Object storing annotations
        """

        fileName = archive_reader.open_session_id + '/Annotations/Annotations.json'
        dict_ = archive_reader.read_metadata(fileName)
        self.user.annotations = dict_['annotations']
        self.user.annotationInfo = dict_['annotation_info']
        self.user.isWorldSynchronized = False
        delattr(self.meta, "attachments")
        return self

    @classmethod
    def from_dict(cls, dict_, archive_reader):
        """ Class constructor used when object is
            constructed from file

        :arg
            dict_ (dict): Metadata used for creating the Datatable object

            archive_reader (ArchiveReader): Object for reading data
            from aaz file

        :returns
            obj (Annotation): Object storing 1d sensor data
            referencing the same timeline
        """

        obj = Annotation.__new__(cls)
        super().__init__(obj)
        obj.to_natives(dict_, archive_reader)
        return obj