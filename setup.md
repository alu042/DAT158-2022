# Set up your computer

If you prefer to work with the course material on your own computer rather than using cloud solutions, then you should install Python and the necessary Python libraries following these instructions. 

## Note for Mac users
If you're using MacOS, you may have to install Xcode (free). Download here: https://developer.apple.com/xcode/resources/. Install using the Terminal:
* Start `terminal.app` (search using CMD+SPACE)
* Run `xcode-select --install`

## Step 1: Install Anaconda
I recommend that you install Python using the [Anaconda Distribution](https://www.anaconda.com/products/distribution#Downloads). We will use the Conda Package Management System included in the Anaconda Distribution

> From the [documentation](https://conda.io/docs): _"Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer."_

After installing Anaconda run `python --version` in a terminal (if you're using Windows, use the "Anaconda Prompt"). If the output contains "Anaconda", then you're ready for the next step.

## Step 2: Install and test the course environment
After installing Anaconda, run through the following steps (on Windows, use the "Anaconda Prompt").

### Install Git

```bash 
conda install git
```

### Download the course repository: 
```bash
git clone https://github.com/alu042/DAT158-2022
cd DAT158-2022
```

### Configure the Python environment
```bash
conda env update
```

### Activate the environment
```bash
conda activate dat158
```

### Install a Jupyter kernel
```bash
python -m ipykernel install --user --name dat158 --display-name "DAT158"
```

### Test your installation
Go through the notebook `notebooks/0.0-test.ipynb`:
```bash
jupyter notebook
```
You can alternatively use [JupyterLab](https://github.com/jupyterlab/jupyterlab): 
```bash
jupyter lab
```

# Updating
The code and environment will be updated throughout the course. Run the following commands regularly: 
* Update code: `git pull`
* Update environment: 
```bash
conda activate dat158
conda env update
```


# Troubleshooting
* If you're using GNU/Linux or MacOS and the `conda activate dat158` command fails, run `source ~/.bash_profile` and try again.
* If you're on a Mac and the `conda env update` command fails with a `gcc` error, install [Xcode](https://developer.apple.com/xcode/resources/) through the App store and use it to install **command line tools**. 
