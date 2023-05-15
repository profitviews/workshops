# Introduction

This project is based on a series of workshops given by [ProfitView](https://profitview.net). You can watch the video replay of the events here:

- [Algorithmic Trading with Python - Part I](https://profitview.net/events/algorithmic-trading-with-python)
- [Algorithmic Trading with Python - Part II](https://profitview.net/events/algorithmic-trading-with-python-part-2)
- [Algorithmic Trading with Python - Part III](https://profitview.net/events/algorithmic-trading-with-python-part-3) (coming - Wednesday 10 May)

Further workshops will have the code examples stored in this repository.

The third workshop will go through the implementation of the order and position management of the strategy in a live environment.

**Note:** this repository and associated talks are for educational
purposes only. Nothing contained herein constitutes as investment
advice or offers any advice with respect to the suitability of any
crypto security or trading strategy.


# Getting Started

## 1. Clone this repo

In a suitable directory on your local computer run

```shell
git clone https://github.com/profitviews/workshops.git
```

to clone this repository. Ensure you have the [GitHub CLI](https://github.com/cli/cli) installed.

## 2. Install Python 

If you don't already have Python 3.9 or later installed, the recommended way to install Python is by using `pyenv`. Follow the instructions on the [project page](https://github.com/pyenv/pyenv) to install it for your operating system.

Once available, install Python 3.9.15

```shell
pyenv install 3.9.15

pyenv global 3.9.15
```

## 3. Create a `pyenv` virtual environment

The well known package manager [venv](https://docs.python.org/3/library/venv.html) is a bit outdated, so it's recommended to use 
`pyenv-virtualenv` which works with `pyenv`. Follow the instructions on the [project page](https://github.com/pyenv/pyenv-virtualenv) to install it for your operating system.

Once installed create a Python virtual environment to use for this project, and activate it.

```shell
pyenv virtualenv workshops

pyenv activate workshops
```

## 4. Install the project dependencies

```shell
pip install -r requirements.txt
```

You may get some errors installing the first time round, if you don't have all the non-Python dependencies installed. 

For example TA-Lib is written in C and the Python module is simply a Cython (C-extension) to this main library. The TA-Lib dependencies can be found [here](https://github.com/TA-Lib/ta-lib-python#dependencies).

Once all non-Python dependencies are installed re-run the pip install command above, to ensure all libraries are available.

## 5. Run the Jupyter Lab notebook

From your command line run

```shell
jupyter lab
```

A new browser tab should open up with the project contents, where you can run the notebook `.ipynb` files from.
