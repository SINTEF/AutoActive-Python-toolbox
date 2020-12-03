import sys
sys.path.insert(0,"..")

from autoactive.autoactive.source import Source
from autoactive.autoactive.datatable import Datatable
from autoactive.autoactive.session import Session
from autoactive.autoactive.folder import Folder
from autoactive.autoactive.archivewriter import ArchiveWriter

import __main__
from pathlib import Path
import numpy as np

so = Source()
this_path = Path(__main__.__file__)
so.add_content_from_file_to_archive(this_path)

time = np.array(range(0,100000000,100000)).astype("int64")
sine = np.sin(2*3.14*time/1000000).astype("float64")
cosi = np.cos(2*3.14*time/1000000).astype("float64")
time_off = time + 1000000

table = Datatable()
table.time = time
table.time.unit = "Epocms"
table.sine = sine
table.cosi = cosi

table_off = Datatable()
table_off.time = time_off
table_off.time.unit = "Epocms"
table_off.sine = sine
table_off.cosi = cosi

session = Session(session_name= "Session")
session.python_data = Folder()
session.python_data.trig = table
session.python_data.trig_off = table_off
session.source = so

write_to = Path.joinpath(this_path.parent, "DOESITWORK.aaz")
aw = ArchiveWriter(write_to)
aw.save_session(session)
aw.close()

