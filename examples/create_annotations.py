from pathlib import Path

from autoactive.autoactive.annotation import Annotation
from autoactive.autoactive.archivewriter import ArchiveWriter
from autoactive.autoactive.session import Session
from autoactive.autoactive.folder import Folder
from autoactive.autoactive.source import Source

from examples.write_archive_sine import create_sample_datatable

annotation_provider = Annotation()
annotation_provider.addAnnotation(0.0, 1)
annotation_provider.addAnnotation(31300000.0, 2)
annotation_provider.setAnnotationInfo(1, "navn", "tag", "kommentar")
annotation_provider.setAnnotationInfo(2, "navn", "tag", "kommentar")

# todo: figure out how to specify time type for annotations

writer = ArchiveWriter('oyvinds_arkiv.aaz')
session = Session(session_name="Session")
session.python_data = Folder()
session.python_data.trig = create_sample_datatable()

session.AnnotationProvider = annotation_provider

so = Source()
this_path = Path(__file__).resolve()
so.add_content_from_file_to_archive(this_path)
session.source = so
writer.save_session(session) 

print('done')
