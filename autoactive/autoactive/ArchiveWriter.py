import zipfile as zp
import pyarrow.parquet as pq
import pyarrow as pa
import json


class AutoActiveWriter:

    ''' Writes data from objects to aaz file

    :arg
        path (str): The complete path of the aaz file

    '''

    def __init__(self, path):
        self._path =  path
        self._file = zp.ZipFile(path, 'w', allowZip64=True)

    def __enter__(self):
        return self

    def __exit__(self, type, value, trackback):
        self.close()
        return False



    def close(self):

        ''' Method that destroys the object '''

        self._file.close()



    def open(self, path):

        ''' Method that accesses a member
            of the archive as a binary file-like object

        :arg
            path (str): can be either the name of a file
            within the archive or a ZipInfo object

        :returns
            original (zipfile): accessible member in the
            zipfile

        '''

        original = self._file.open(path,'w')
        return original



    def writeCopyContentFromFile(self, elemName, data):

        ''' Method that writes the file to archive

        :arg
            elemName (str): The complete path in archive

            data (str): The complete path of the data to write to archive

        '''


        self._file.write(elemName, data)



    def saveSession(self, sessionHandle):

        ''' Method saving the session to archive

        :arg
            sessionHandle (Session): The session object

        '''

        sessionHandle.save(self)

    def writeMetadata(self, elemName, jsonStruct):

        ''' Method saving json object to archive

        :arg
            elemName (str): The complete path in archive where
            the json object is stored

            jsonStruct (dict): serialiable object

        '''

        with self.open(elemName) as file:
            file.write(json.dumps(jsonStruct).encode('utf-8'))

    def writeTable(self, elemName, table):

        ''' Method transforming table object to
            parquet object and stores it in the archive.

        :arg
            elemName(str): The complete path in archive where
            the table object is stored

            table (table): The table object

        '''

        columnNames = table.columns.tolist()
        fields = list()
        for name in columnNames:
            if str(table[name].dtype) == 'int64':
                dtype = pa.int64()
            elif str(table[name].dtype) == 'float64':
                dtype = pa.float64()
            else:
                dtype = pa.string()
            fields.append((name, dtype, False))

        schema = pa.schema(fields)
        table = pa.Table.from_pandas(table, schema)

        with self.open(elemName) as file:
            parquetWriter = pq.ParquetWriter(file, schema)
            parquetWriter.write_table(table)
            parquetWriter.close()






