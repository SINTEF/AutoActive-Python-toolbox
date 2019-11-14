
class Dataobject():

    ''' Parent class for all data objects  '''



    def toSerializable(self, **kwargs):

        ''' Method which transforms the dataobject to a
        serializable object

        :arg
            **kwargs (dict): dictionary containing the archiveWriter,
            uuid and the parent key

        :returns
            dict (dict): representing the dataobject object as a dictionary

        '''

        return {'meta': self.meta, 'user': self.user}



    def replaceNatives(self, **kwargs):

        ''' Transforms the nested python objects to nested
            serializable objects

        :arg
            **kwargs (dict): dictionary containing the archiveWriter
            uuid and the parent key

        '''

        serializableObj = self.toSerializable(**kwargs)
        for key in serializableObj['user'].keys():
            kwargs['parentKey'] = key
            if issubclass(serializableObj['user'][key].__class__, self.__class__.__bases__) == True:
                if serializableObj['user'][key].__class__.__name__ in ['Table', 'Source', 'Video']:
                    temp = serializableObj['user'][key].toSerializable(**kwargs)
                    serializableObj['user'][key] = temp
                else:
                    serializableObj['user'][key] = serializableObj['user'][key].replaceNatives(**kwargs)

        return serializableObj


    def addChild(self, name, child):
        ''' Method adds child to the parentobject

        :arg
            name (str): The name of the new child element

            child (dataobject): The child object that is added to the structure
        '''

        self.user[name] = child

