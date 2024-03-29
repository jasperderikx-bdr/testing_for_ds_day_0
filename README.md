<h2 align="center">

<img src="https://d1xdv7s0q9b0j6.cloudfront.net/static/images/logo.e2d3098a.2865948e8900.svg" width="200px"/><br/>
![Conda Latest Release](https://anaconda.org/conda-forge/pandas/badges/version.svg)
![PyPI - Python Version](https://img.shields.io/badge/python-3.10-blue)
![wheel](https://img.shields.io/badge/wheel-yes-green)
![Code style](https://img.shields.io/badge/Code_style-flake8-lightgrey)
![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat)

Testing for Data Science</h2>

<h4 align="center">Day 0</h4>

With these prerequisites you can make sure everything is set up correctly for the full training. 
Don't expect to learn a lot; the main goal is to address if anything is not working for you.

## ⚡ Installation

---

### 1. Virtual Environment

Create a virtual environment for this repo, for instance with [Anaconda](https://docs.anaconda.com/anaconda/install/):

```sh
conda create --name testing_for_ds -y python=3.10
conda activate testing_for_ds
```

You can use the same virtual environment for the whole training.
Note: if you just installed anaconda, you might have to initialize your terminal with ```conda init <SHELL_NAME>``` and restart your terminal afterwards.

### 2. Install dependencies

Install the project in develop mode, with:
   
```sh
pip install -e ".[develop]"
```
This will install all the dependencies listed in ```requirements.txt``` and ```requirements.dev.txt```. Have a look at them to get an idea with what we're working.

### 3. setup pre-commit

We will be using pre-commit for this project, install it with:

```sh
pre-commit install
```

If you commit your code, pre-commit will run some checks. Only if you pass the checks, the commit is completed.
For example, it checks whether you've used type-hinting. See .pre-commit-config.yaml for the full configuration.

### 4. create your own branch


```sh
git checkout -b <branch-name>
git push --set-upstream origin <branch-name>
```

Note: if you run into the error: "The unauthenticated git protocol on port 9418 is no longer supported.", this [stackoverflow page](https://stackoverflow.com/questions/70663523/the-unauthenticated-git-protocol-on-port-9418-is-no-longer-supported) might help.

## 📋 Assignment

---

After you completed the installation, it's time to do a little coding. 
If you run pytest:

```sh
pytest
```

you will see that not all tests pass. Open the file: ```tests\test_exercises.py``` and follow the instructions in the comments.

You've completed the assignment if:
- All tests pass.
- All pre-commit steps are successful.
- You pushed your code to your personal branch.

Please let me know if anything is not working!
