import numpy as np
from scipy.stats import norm

def historical_var(portofolio_returns, confidence_level = 0.95,portfolio_value = 1000000):
    alpha = 1 - confidence_level
    var_percent = -np.percentile(portofolio_returns,alpha * 100)
    var_amount = var_percent * portfolio_value

    return var_percent, var_amount

def parametric_var(portfolio_returns, confidence_level = 0.95, portfolio_value = 1000000):
    mean = portfolio_returns.mean()
    std = portfolio_returns.std()

    alpha = 1 - confidence_level
    z_score = norm.ppf(alpha)

    var_percent = -(mean + z_score*std)
    var_amount = var_percent * portfolio_value
    
    return var_percent, var_amount


def monte_var(portfolio_returns, confidence_level = 0.95, portfolio_value = 1000000,simulations = 1000):
    
    mean = portfolio_returns.mean()
    std = portfolio_returns.std()

    simulated_returns = np.random.normal(
        loc = mean,
        scale = std,
        size = simulations
    )
    alpha = 1-confidence_level

    var_percent = -np.percentile(simulated_returns, alpha * 100)
    var_amount = var_percent * portfolio_value

    return var_percent, var_amount


def historical_short(portfolio_returns, confidence_level = 0.95, portfolio_value = 1000000):
    alpha = 1 - confidence_level
    var_threshold = np.percentile(portfolio_returns, alpha * 100)
    tail_lossess = portfolio_returns[portfolio_returns <= var_threshold]

    es_percent = -tail_lossess.mean()
    es_amount = es_percent * portfolio_value

    return es_percent, es_amount
