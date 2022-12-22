""" A test script for reading aaz files"""

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
    parser = ArgumentParser()
    parser.add_argument("fname")
    args = parser.parse_args()

    fname = Path(args.fname)
    assert fname.exists(), (
        f"{fname} does not exist. You can use the write_archive_sine.py to"
        f"create a aaz file"
    )
    assert fname.is_file(), f"{fname} is not a file"

    sess = main(fname)
