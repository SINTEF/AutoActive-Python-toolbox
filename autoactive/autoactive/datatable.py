from autoactive.archive.dataobject import Dataobject
from autoactive.datastructures.meta import Meta
from autoactive.datastructures.user import User

from dataclasses import dataclass
from functools import singledispatch
import numpy as np
import pandas as pd


@dataclass
class Data:
    data = None
    unit = None


@dataclass(init=False)
class Datatable(Dataobject):
    @property
    def column_names(self):
        return self.user.__dict__.keys()

    @property
    def dtypes(self):
        return [d.data.dtype for d in self.user.__dict__.values()]

    @property
    def units(self):
        return [d.unit for d in self.user.__dict__.values()]

    @property
    def data(self):
        return [d.data for d in self.user.__dict__.values()]

    @property
    def as_dict(self):
        return {key: value for (key, value) in zip(self.column_names, self.data)}

    @property
    def as_dataframe(self):
        return pd.DataFrame(self.as_dict)

    def __init__(self):
        super().__init__()
        self.meta.type = "no.sintef.table"
        self.meta.version = 1

    def __setattr__(self, name, value):
        _setattr(value, name, self)

    def __getattr__(self, item):
        return self.user.__dict__[item]

    def to_serializable(self, **kwargs):

        """ Method which transforms the table object to a
        serializable object

        :arg
            **kwargs (dict): dictionary containing the archiveWriter
            uuid and the parent key

        :returns
            dict (dict): representing the table object as a dictionary

        """

        assert "time" in self.column_names, "No time column found"
        assert self.time.unit != None, "The time column must have a unit"
        path = f"{str(kwargs['uuid'])}/data/{str(kwargs['parent_key'])}.parquet"
        self.meta.attachments = [f"/data/{str(kwargs['parent_key'])}.parquet"]
        self.meta.units = self.units
        self.meta.is_world_clock = False
        kwargs["archive_writer"].write_table(path, self)
        return {"user": dict(), "meta": self.meta.__dict__}

    def to_natives(self, archive_reader):
        for file in self.meta.attachments:
            df = archive_reader.read_table(archive_reader.open_session_id + file)
            for i, column in enumerate(df.columns):
                self.__setattr__(column, df[column].values)
                self.user.__dict__[column].unit = self.meta.units[i]
        delattr(self.meta, "units")
        delattr(self.meta, "attachments")
        return self


@singledispatch
def _setattr(value, name, self: Datatable) -> None:
    assert False, "Type not implemented"


@_setattr.register(np.ndarray)
def _(value, name, self: Datatable) -> None:
    d = Data()
    d.data = value
    self.user.__dict__[name] = d


@_setattr.register(Meta)
@_setattr.register(User)
def _(value, name, self: Datatable) -> None:
    self.__dict__[name] = value
