from autoactive.autoactive.Folder import Folder
from autoactive.autoactive.Session import Session
from autoactive.datastructures.Table import Table
from autoactive.autoactive.Source import Source
import autoactive.autoactive.ArchiveWriter as ArchiveWriter
import os
import __main__
import numpy as np

so = Source()
thisPath = str(__main__.__file__)
so.addContentFromFileToArchive(thisPath)

time = np.array(range(0,100000000,100000))
sine = np.sin(2*3.14*time/1000000)
cosi = np.cos(2*3.14*time/1000000)

time_off = time + 1000000

table = Table(np.transpose([time,sine, cosi]),['Time', 'sine','cosi'])
table2 = Table(np.transpose([time_off,sine, cosi]),['Time', 'sine','cosi'])

session = Session('Session')
folder = Folder()

session.addChild('PythonData',folder)
folder.addChild('PythonTrig', table)
folder.addChild('PythonoffTrig', table2)
session.addChild('source', so)

aw = ArchiveWriter.AutoActiveWriter(os.getcwd() + '\\' + 'DOESITWORK.aaz')
aw.saveSession(session)
aw.close()

