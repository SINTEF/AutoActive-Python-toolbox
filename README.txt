The AutoActive Python package is a set of classes used to read and write aaz files. The aaz file type is 
a common filetype used in the AutoActive Research Enviroment. The overall goal of the AutoActive Research
enviroment is to ease the analysis and development of machine learning models using data from multiple types 
of sensors.

The AutoActive Research Enviroment consist of Activity Presenter, AutoActive python package and AutoActive Matlab toolbox.
Activity Presenter is a graphical user interface which makes it easy to synchronize, visualise and organise data
from multiple sensors, while the overall goal of the AutoActive python package and the AutoActive matlab toolbox is to make
it possible to import the preprocessed data into python or matlab where you can utilse all the powerfull algorithms 
already implemented.The AutoActive python package also makes it possible to write the results back to aaz files, and thereby,
also visualising the results in Activity Presneter.

More information about the AutoActive Research Enviroment (ARE) and the aaz file type is available here:
https://github.com/SINTEF/AutoActive-ActivityPresenter

# License
Apache License Version 2.0

# Installation
To use the AutoActive python package you need to clone this repository and import it into
your projects of intereset.

# Examples
There are today two example files in the repository, where one file is an example script of how to
create a new aaz file and write to it to file. This file is named write_archive_sine.py and is located
in the example folder. The second example is an example script of how to 
read data from an aaz file. This file is also located in the example folder and is named read_archive_sine.py
Before running read_archive_sine.py you can create an aaz file with write_archive_sine.py

# Coding style / guidelines
If you whish to contribute to the project please follow these guidelines:
- use_lower_case_with_underscores_naming for everything except Classes
- For classes UseCamelCase
- Remove unneeded code, don't comment out, you have git for this
- Use the black formatter (https://pypi.org/project/black/) to format you code.


# TODO
There are a couple of pressing issues
	1. Session Object returned from ArchiveReader should be immutable
	2. Implement reading and writing of videos.
	3. Implement error handling
	4. Handle Gaitup and catapult imports as these are very common sensors used in sports.
	5. Implemet archivewriter and archivereader with context managers
	6. Finish implementing source