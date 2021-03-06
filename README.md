## GENERAL INFO
A project to convert few most common astronomy format data used in photometry. Program provides user with easy way to format data into two-column text format. It allows to create customizable graph, calculate periods and save it as .png files.

### FEATURES
* Converting from databases: Hipparcos, Integral, NSVS, ASAS, Munipack, Kepler, Catalina
* Creating customizable graphs
* Calculating periods
* Multiconverting all files at once.

### DEPENDENCIES
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [PIP](https://pypi.python.org/pypi/pip)
* [GIT](http://git-scm.com/downloads)

### Installation
1. Checkout the repo from git
2. Install python dependencies by running `pip install -r requirements.txt`
3. Run `python astroConverter.py`

### Troubleshooting
* In case of problems with running `python astroConverter.py`, instead of 'python' try using full path to your installation. For example: `c:\python34\python.exe astroConverter.py`
* In case of problems with installing dependencies try using command `pip3.4 install -r requirements.txt`. Or  `path_to_your_python_executable -m pip install -r requirements.txt` This problem may occur if you have installed multiple versions of python.
