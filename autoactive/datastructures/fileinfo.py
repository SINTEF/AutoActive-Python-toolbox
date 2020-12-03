from pathlib import Path
import os
from datetime import datetime
from dataclasses import dataclass


@dataclass(init=False)
class Fileinfo:
    def __init__(self, fname: Path):
        self.name: str = fname.name
        self.folder: str = os.path.dirname(fname)
        self.isdir: int = Path.is_dir(fname)
        self.date: str = datetime.fromtimestamp(os.stat(fname).st_mtime).strftime(
            "%Y-%b-%d %H:%M:%S"
        )
        self.bytes: int = os.stat(fname).st_size
        self.datenum: int = datetime.fromtimestamp(
            os.stat(fname).st_mtime
        ).toordinal() + 366
