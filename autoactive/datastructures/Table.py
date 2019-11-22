import pandas as pd
from autoactive.archive.Dataobject import Dataobject
import numpy as np


class Properties():

    ''' It is intended as a helper class for the
        Table class, describing the properties of
        the data in the Table class. It is
        instantiated from a table object and it is
        not suppose to be instantiated by the user

    :arg
        columnNames (list): list of the column names
        of the data in table object.


    '''

    def __init__(self, columnNames):

        self._properties = {'Description': '',
                           'UserData': [],
                           'DimensionNames': [],
                           'VariableNames': [],
                           'VariableDescription': [],
                           'VariableUnits': {},
                           'VariableContinuity': [],
                           'RowNames': []
                           }

        self._properties['VariableNames'] = columnNames


    def getProperties(self):

        ''' Returns itself

        :returns
            self (properties): Returns itself

        '''

        return self



class Table(Dataobject):

    ''' Class simmulates the Table class from matlab.
    The input can either be list/array of data and a
    belonging list describing the column names org it
    can be a dataframe. Eitherway there must be a column
    named Time where the time format is epoch ...

    :arg
        data (list/array): data

        columnNames (list): Describing the column names

        df (dataframe): data

    '''


    def __init__(self, data = [] , columnNames = None, df = None):

        self.meta = {'type': 'no.sintef.table', 'version': 1}
        if data != []:
            properties = Properties(columnNames)
            self.user = {'Data':  pd.DataFrame(data, columns= columnNames),
                        'properties': properties.getProperties()}
            self.user['data'] = self.setDatatypes(self.user['Data'])
        else:
            properties = Properties(df.columns.tolist())
            self.user = {'Data': df,
                         'properties': properties.getProperties()}

    def setDatatypes(self, df):
        for columnName in df.columns:
            columnData = df[columnName].values[::100]
            try:
                if np.array_equal(columnData, columnData.astype('int64')) == True:
                    df[columnName] = df.astype('int64')
                else:
                    df[columnName] = df[columnName].astype('float64')
            except ValueError:
                df[columnName] = df[columnName].astype(str)
        return df


    def toSerializable(self, **kwargs):


        ''' Method which transforms the table object to a
        serializable object

        :arg
            **kwargs (dict): dictionary containing the archiveWriter
            uuid and the parent key

        :returns
            dict (dict): representing the table object as a dictionary

        '''

        for key, value in self.user.items():
            if isinstance(value, pd.DataFrame):
                units = list()
                path = '/' + str(key) + '/' + str(kwargs['parentKey']) + '.parquet'
                for columnName, columnData in self.user['Data'].iteritems():
                    if columnName == 'Time': units.append("Epocms")
                    else: units.append("")
                self.meta['attachments'] = [path]
                self.meta["units"] = units
                kwargs['archiveWriter'].writeTable(str(kwargs['uuid']) + path,value)
        self.user = dict()
        self.meta['is_world_clock'] = False
        return {"user": self.user, "meta": self.meta}