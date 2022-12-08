from os import path
import json
from dataclasses import dataclass

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
        self.user.annotations.append({"timestamp": timestamp,
                                      "type": annotationId})
        #self.user.annotations['timestamp'].append(timestamp)
        #self.user.annotations['type'].append(annotationId)

    def setAnnotationInfo(self, annotationId: int, name: str, tag: str, comment: str):
        #assert annotationId in self.user.annotations['type'], "No annotations with this annotationId"
        self.user.annotationInfo[annotationId] = {'name': name,
                                                  'tag': tag,
                                                  'comment': comment}

    def toJsonStructRec(self, sessionId, archiveWriter: ArchiveWriter):
        # annotations are stored in a separate file
        fileName = path.join(sessionId, 'Annotations\\Annotations.json')

        # TODO: assert that all annotationInfo entries are type char (necessary?)
        # TODO: convert annotation keys to char (for json storage) (not necessary, json-package handles it?)

        annotationsDict = {'AutoActiveType': self.meta.AutoActiveType,
                           'is_world_synchronized': self.user.isWorldSynchronized,
                           'version': self.meta.version,
                           'annotation_info': self.user.annotationInfo,
                           'annotations': self.user.annotations
                           }
        #jsonAnnotations = json.dumps(annotationsDict)
        archiveWriter.write_metadata(fileName, annotationsDict)
