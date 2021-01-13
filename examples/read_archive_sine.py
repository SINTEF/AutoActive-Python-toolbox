import sys

sys.path.insert(0, "..")

from autoactive.autoactive.archivereader import ArchiveReader

from pathlib import Path

fname = Path(
    r"C:\Users\kasperb\Documents\Projects\AutoActive\Kode\autoactive-python\examples\DOESITWORK.aaz"
)
ar = ArchiveReader(fname)
ids = ar.list_ids()
s = ar.open_session(ids[0])
