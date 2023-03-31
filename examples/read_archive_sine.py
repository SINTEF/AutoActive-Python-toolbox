""" A test script for reading aaz files. Name of azz-file (including file path) must be provided as input parameter.
 Example: python .\read_archive_sine.py '[Path-to-file]//sine.aaz' """

import sys

sys.path.insert(0, "..")
from autoactive.autoactive.archivereader import ArchiveReader

from pathlib import Path
from argparse import ArgumentParser


def main(fname):
    """Reads the aaz file and returns the first session in the file

    :arg
        fname (Path): Path to aaz file

    :returns
        sess (Session): Session object. A pythonic representation of the
        aaz file
    """
    with ArchiveReader(fname) as ar:
        ids = ar.list_ids()
        sess = [ar.open_session(id) for id in ids]
        if len(sess) == 1:
            sess = sess[0]
    return sess


if __name__ == "__main__":
    parser = ArgumentParser(description="Example script showing how to read an aaz-archive")
    parser.add_argument("fname", help="Name of azz-file, including file path")
    args = parser.parse_args()

    fname = Path(args.fname)
    assert fname.exists(), (
        f"{fname} does not exist. You can use the write_archive_sine.py to"
        f"create a aaz file"
    )
    assert fname.is_file(), f"{fname} is not a file"

    sess = main(fname)
