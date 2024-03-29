The AutoActive Python package is a set of classes used to read and write aaz files. The aaz file type is 
a common filetype used in the AutoActive Research Enviroment. The overall goal of the AutoActive Research
Enviroment is to ease the analysis and development of machine learning models using data from multiple types 
of sensors.

The AutoActive Research Enviroment consists of Activity Presenter, AutoActive Python toolbox and AutoActive Matlab toolbox.
Activity Presenter is a graphical user interface which makes it easy to synchronize, visualise, annotate and organise data
from multiple sensors, while the overall goal of the AutoActive Python package and the AutoActive Matlab toolbox is to make
it possible to import the preprocessed data into Python or Matlab where you can utilise all the powerful algorithms 
already implemented.The AutoActive Python package also makes it possible to write the results back to aaz files, and thereby,
also visualising the results in Activity Presenter.

A typical usecase would be supervised machine learning on time series data, where you have one or more video files
with "ground truth" observations. In this case, the workflow would be to manually annotate the video(s) using Activity Presenter
and then train your machine learning application by reading the annotations from the aaz-archive. Alternatively, you can manually validate predictions made by a machine learning application by writing the results to an aaz-archive using this toolbox, and then inspecting the results using Activity Presenter. 

More information about the AutoActive Research Enviroment (ARE) and the aaz file type is available here:
https://github.com/SINTEF/AutoActive-ActivityPresenter

# License
Apache License Version 2.0

# Installation
To use the AutoActive Python package you need to clone this repository and import it into
your projects of interest.

# Requirements
- pandas
- numpy
- pyarrow

See requirements.txt

# Examples
There are two example files in the repository's example folder: "write_archive_sine.py" and "read_archive_sine.py". The first file ("write_archive_sine.py") demonstrates how to write a time series (a sine function) to an aaz-archive. The sine-function's peaks, valleys and zero-crossings are added as annotations in the aaz-archive. The second example ("read_archive_sine.py") shows how to read the archive you generated when running "write_archive_sine.py". 

# Coding style / guidelines
If you whish to contribute to the project please follow these guidelines:
- use_lower_case_with_underscores_naming for everything except Classes
- For classes UseCamelCase
- Remove unused code, don't comment out, you have git for this
- Use the black formatter (https://pypi.org/project/black/) to format you code.


# TODO
There are a couple of pressing issues
	1. Session Object returned from ArchiveReader should be immutable
	2. Implement error handling
	3. Handle Gaitup and Catapult imports as these are very common sensors used in sports.

