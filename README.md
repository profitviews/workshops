# Introduction

This project is based on a series of workshops given by [ProfitView](https://profitview.net). You can watch the video replay of the events here:

- [Algorithmic Trading with Python - Part I](https://profitview.net/events/algorithmic-trading-with-python)
- [Algorithmic Trading with Python - Part II](https://profitview.net/events/algorithmic-trading-with-python-part-2)
- [Algorithmic Trading with Python - Part III](https://profitview.net/events/algorithmic-trading-with-python-part-3)

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

Now that the dependencies are installed in your virtual environment, you will also need to make the `pyenv` kernel available for Jupyter. 

To do this run the following, with the `workshops` environment activated:

```shell
python -m ipykernel install --user --name=workshops
```

If you list the available Jupyter kernels, you should now see this `pyenv` kernel:

```shell
jupyter kernelspec list 
```

Now you will be able to run Jupyter Lab each time by running the following: 

```shell
jupyter lab
```

A new browser tab should open up with the project contents, where you can run the notebook `.ipynb` files from. Note that you will need to select the `workshops` kernel if it is not already selected to ensure that all the dependencies are available in your notebook.

## 6. Running the Trading Strategy in a live environment

Before running the trading strategy in ProfitView, we recommend you get familiar with the documentation, available [here](https://profitview.net/docs/trading/).

The file contains the code covered in the 3rd workshop. 

Steps:

a. Create an account on ProfitView if you haven't done so already - link [here](https://profitview.net/register).

b. After signing up, go to [BitMEX](https://www.bitmex.com/) and create an API key with "Key Permissions" set to "Order". No withdrawal access is required, so keep this unchecked.

c. Add this API key to ProfitView within [Settings > Exchanges](https://profitview.net/app/settings/exchanges). 

d. To create a Trading Bot instance, you will need to be on at least the [Hobbyist plan](https://profitview.net/app/settings/plans).

e. Once the required plan has been activated, go to the [Trading Bots](https://profitview.net/trading/bots) page, and use the file [MACD.py](blob/main/MACD.py), at your own discretion to run the code covered in the 3rd workshop.

f. Note that you will need to subscribe to market data for the symbols you are interested in trading by clicking the thunder bolt icon on the left side of the code editor.


## 7. Follow ups and Help

If you have any issues running anything above, please do not hesistate to reach out either by emailing support@profitview.net or messaging the [Telegram group](https://t.me/+7B-cYq4n8ds0ZmU0). We are very happy to help.