# Example trader

An example trading agent for David Knott.

## Usage

````
python -m example_trader.example_trader
````

Twice every second, reads the current price and decides whether to buy or sell and how much.

Press `Ctrl+C` to stop.

## How does it work?

Using the price history, computes the [Kelly fraction](https://www.investopedia.com/articles/trading/04/091504.asp): the optimal fraction of the agent's total holdings that should be invested in the asset. Buys or sells to maintain that fraction.

## Requirements

Dependencies:

* numpy
* requests

Dev dependencies:

* pytest

Run tests with `py.test`.

