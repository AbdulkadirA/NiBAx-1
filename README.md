# BrainChart Toolbox

After proper installation, the tools can be used as follows

```shell
QtBrainChart
```

where `istaging.pkl.gz` and `MUSE_harmonization_model.pkl` are the data and
harmonization models, respectively.

## Setup for development
Install Python version 3.8.8 or newer. Verify with

```shell
python --version # should be 3.8.8 or newer
```

### Prepare environment in Linux (CUBIC)
Assuming current working directory is `BrainChart`.
```shell
python -m venv .env
.env/bin/activate
python -m pip install --upgrade pip
```

### Prepare environment in Windows 10 or Windows 11
Assuming current working directory is `BrainChart`.
```shell
python -m venv .env
& .env/Scripts/Activate.ps1
python -m pip install --upgrade pip
```

### Install BrainChart Toolbox
To install the `BrainChart Toolbox`, do one of these after activating the
virtual environment:

```shell
# Editable version for development
python -m pip install -e . 

# Version from pull request for testing proposed changes
python -m pip install git+https://github.com/CBICA/iSTAGING-Tools.git@refs/pull/57/head

# Main version for testing of what users would get
python -m pip install git+https://github.com/CBICA/iSTAGING-Tools.git
```
