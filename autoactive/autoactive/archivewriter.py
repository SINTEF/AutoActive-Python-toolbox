import zipfile as zp
import pyarrow.parquet as pq
import pyarrow as pa
import json

class ArchiveWriter:

    def __init__(self, path):
        self._file = zp.ZipFile(path, "w", allowZip64=True)

    def open(self, path):

        """ Method that accesses a member
            of the archive as a binary file-like object

        :arg
            path (str): can be either the name of a file
            within the archive or a ZipInfo object

        :returns
            original (zipfile): accessible member in the
            zipfile

        """

        original = self._file.open(path, "w")
        return original

    def close(self):

        """ Method that destroys the object """

        self._file.close()

    def save_session(self, session_handle):

        """ Method saving the session to archive

        :arg
            session_handle (Session): The session object

        """

        session_handle.save(self)

    def write_metadata(self, elem_name, json_struct):

        """ Method saving json object to archive

        :arg
            elem_name (str): The complete path in archive where
            the json object is stored

            jsonStruct (dict): serialiable object

        """

        with self.open(elem_name) as file:
            file.write(json.dumps(json_struct).encode("utf-8"))

    def write_table(self, elem_name, table):

        """ Method transforming table object to
            parquet object and stores it in the archive.

        :arg
            elem_name (str): The complete path in archive where
            the table object is stored

            table (Datatable): The table object

        """

        column_names = table.column_names
        a = table.dtypes
        types = list(map(to_parquet_types, table.dtypes))
        fields = [(n, t, False) for n, t in zip(column_names, types)]
        schema = pa.schema(fields)
        table = pa.Table.from_pandas(table.as_dataframe, schema)

        with self.open(elem_name) as file:
            parquet_writer = pq.ParquetWriter(file, schema)
            parquet_writer.write_table(table)
            parquet_writer.close()

    def copy_content_from_file(self, elem_name, data):
        self._file.write(elem_name, data)


def to_parquet_types(type):

    """Method for converting native types
    into parquet types

    :arg
        type (Type) :

    :return:
        dtype (Parquet type) :

    """
    if str(type) == "int64":
        dtype = pa.int64()
    elif str(type) == "float64":
        dtype = pa.float64()
    else:
        dtype = pa.string()
    return dtype
