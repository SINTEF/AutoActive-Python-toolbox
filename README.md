The AutoActive Python package is a set of classes used to read and write aaz files. The aaz file type is 
a common filetype used in the AutoActive Research Enviroment. The overall goal of the AutoActive Research
Enviroment is to ease the analysis and development of machine learning models using data from multiple types 
of sensors.

The AutoActive Research Enviroment consists of Activity Presenter, AutoActive Python package and AutoActive Matlab toolbox.
Activity Presenter is a graphical user interface which makes it easy to synchronize, visualise and organise data
from multiple sensors, while the overall goal of the AutoActive Python package and the AutoActive Matlab toolbox is to make
it possible to import the preprocessed data into Python or Matlab where you can utilse all the powerfull algorithms 
already implemented.The AutoActive Python package also makes it possible to write the results back to aaz files, and thereby,
also visualising the results in Activity Presenter.

More information about the AutoActive Research Enviroment (ARE) and the aaz file type is available here:
https://github.com/SINTEF/AutoActive-ActivityPresenter

# License
Apache License Version 2.0

# Installation
To use the AutoActive Python package you need to clone this repository and import it into
your projects of intereset.

# Examples
There are today two example files in the repository, where the first is an example script to shown how to
create a new aaz file and write it to a file. This file is named write_archive_sine.py and is located
in the example folder. The second example is an example script to show how to 
read data from an aaz file. This file is also located in the example folder and is named read_archive_sine.py
Before running read_archive_sine.py you can create an aaz file with write_archive_sine.py

# Coding style / guidelines
If you whish to contribute to the project please follow these guidelines:
- use_lower_case_with_underscores_naming for everything except Classes
- For classes UseCamelCase
- Remove unused code, don't comment out, you have git for this
- Use the black formatter (https://pypi.org/project/black/) to format you code.


# TODO
There are a couple of pressing issues
	1. Session Object returned from ArchiveReader should be immutable
	2. Implement reading and writing of videos.
	3. Implement error handling
	4. Handle Gaitup and Catapult imports as these are very common sensors used in sports.
	5. Implement archivewriter and archivereader with context managers
