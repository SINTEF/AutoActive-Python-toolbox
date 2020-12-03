from autoactive.datastructures.meta import Meta
from autoactive.datastructures.user import User

from dataclasses import dataclass


@dataclass(init=False)
class Dataobject:
    def __init__(self):
        self._meta: Meta = Meta()
        self._user: User = User()

    @property
    def meta(self):
        return self._meta

    @property
    def user(self):
        return self._user

    def __setattr__(self, key, value):
        if isinstance(value, Dataobject):
            self.user.__dict__[key] = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item not in self.__dict__.keys():
            return self.user.__dict__[item]
        else:
            return self.__dict__[item]

    def to_serializable(self, **kwargs):

        """ Method which transforms the dataobject to a
        serializable object

        :arg
            **kwargs (dict): dictionary containing the archiveWriter,
            uuid and the parent key

        :returns
            dict (dict): representing the dataobject object as a dictionary

        """
        meta = self.meta.__dict__
        user = self.user.__dict__

        return {"meta": meta, "user": user}

    def replace_natives(self, **kwargs):

        """ Transforms the nested python objects to nested
            serializable objects

        :arg
            **kwargs (dict): dictionary containing the archiveWriter
            uuid and the parent key

        """

        ser_obj = self.to_serializable(**kwargs)
        for key, value in ser_obj["user"].items():
            kwargs["parent_key"] = key
            if isinstance(value, Dataobject):
                ser_obj["user"][key] = value.replace_natives(**kwargs)
        return ser_obj