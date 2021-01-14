""" Script for creating a session with 1d sensor data
    and saving the session to a aaz file """

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
from argparse import ArgumentParser

def save_session(session, fname):
    """ Saves session to file

    :arg
        session (Session): session object to save to file

        fname (Path): Path to where to save the session object
    """

    aw = ArchiveWriter(fname)
    aw.save_session(session)
    aw.close()

def create_sample_datatable(offset = 0):
    """ Adds sample data to datatable

    :arg
        offset (int): Offset of timeline

    :returns
        table (Datatable): dataobject storing 1d sensor data
    """

    time = np.array(range(0, 100000000, 100000)).astype("int64") + offset
    sine = np.sin(2 * 3.14 * time / 1000000).astype("float64")
    cosi = np.cos(2 * 3.14 * time / 1000000).astype("float64")

    table = Datatable()
    table.time = time
    table.time.unit = "Epocms"
    table.sine = sine
    table.cosi = cosi
    return table

def main(fname):
    """ Creates a session and saves it to an aaz file

    :arg:
        fname (Path): Path to where to save the session
    """
    so = Source()
    this_path = Path(__main__.__file__)
    so.add_content_from_file_to_archive(this_path)

    table = create_sample_datatable()
    table_off = create_sample_datatable(1000000)

    session = Session(session_name= "Session")
    session.python_data = Folder()
    session.python_data.trig = table
    session.python_data.trig_off = table_off
    session.source = so

    save_session(session, fname)



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("fname")
    args = parser.parse_args()

    fname = Path(args.fname)
    assert fname.name.split(".")[-1] == "aaz", "The file must be an aaz file"
    main(fname)
