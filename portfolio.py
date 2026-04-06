import pandas as pd
import numpy as np


def compute_returns(prices):
    log_prices = np.log(prices)
    returns = log_prices.diff().dropna().copy()

    return returns


def compute_portfolio_returns(returns,weights):
    weights = np.array(weights)

    if not np.isclose(weights.sum(),1):
        raise ValueError("The sum of weights must be equal to one")
    
    portfolio_returns = returns.dot(weights)
    portfolio_returns.name = "Portfolio_return"

    return portfolio_returns



