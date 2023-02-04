""" Script for creating a session with 1d sensor data
    and saving the session to a aaz file """

import sys

sys.path.insert(0, "..")

from autoactive.autoactive.source import Source
from autoactive.autoactive.datatable import Datatable
from autoactive.autoactive.session import Session
from autoactive.autoactive.folder import Folder
from autoactive.autoactive.archivewriter import ArchiveWriter
from autoactive.autoactive.annotation import Annotation

from pathlib import Path
import numpy as np
from argparse import ArgumentParser


def save_session(session, fname):
    """Saves session to file

    :arg
        session (Session): session object to save to file

        fname (Path): Path to where to save the session object
    """
    with ArchiveWriter(fname) as aw:
        aw.save_session(session)


def create_sample_datatable(offset=0):
    """Adds sample data to datatable

    :arg
        offset (int): Offset of timeline

    :returns
        table (Datatable): dataobject storing 1d sensor data
    """

    time = np.array(range(0, 100000000, 100000)).astype("int64") + offset
    sine = np.sin(2 * np.pi * time / 1000000).astype("float64")

    table = Datatable()
    table.time = time
    table.time.unit = "Epocms"
    table.sine = sine
    return table


def annotate_sine(table):
    period = 1000000
    idx_zeros = np.where(np.remainder(2 * table.as_dataframe.time.values, period) == 0)
    zeros = table.as_dataframe.time.loc[idx_zeros]
    peaks = zeros[0:-1:2] + period / 4
    valleys = peaks + period / 2
    annotations = Annotation()
    for zero in zeros:
        annotations.addAnnotation(zero, 1)
    for peak in peaks:
        annotations.addAnnotation(peak, 2)
    for valley in valleys:
        annotations.addAnnotation(valley, 3)

    annotations.setAnnotationInfo(1, "zero", "zero", "This is a zero")
    annotations.setAnnotationInfo(2, "peak", "peak", "This is a maximum")
    annotations.setAnnotationInfo(3, "valley", "valley", "This is a minimum")

    return annotations


def main(fname):
    """Creates a session and saves it to an aaz file

    :arg:
        fname (Path): Path to where to save the session
    """
    so = Source()
    this_path = Path(__file__).resolve()
    so.add_content_from_file_to_archive(this_path)

    table = create_sample_datatable()
    annotations = annotate_sine(table)

    session = Session(session_name="Session")
    session.python_data = Folder()
    session.python_data.trig = table
    session.annotations = annotations
    session.source = so

    save_session(session, fname)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("fname")
    args = parser.parse_args()

    fname = Path(args.fname)
    assert fname.name.split(".")[-1] == "aaz", "The file must be an aaz file"
    main(fname)
