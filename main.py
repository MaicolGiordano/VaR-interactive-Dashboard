from data_loader import download_data,clean_data
from portfolio import compute_returns, compute_portfolio_returns
from var_models import historical_var, parametric_var, monte_var

def main():
    tickers = ["SPY","AGG","GLD"]
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    weights = [0.5, 0.3, 0.2]
    portfolio_value = 1000000
    confidence_level = 0.95

    prices = download_data(tickers,start_date,end_date)
    prices = clean_data(prices)
     

    print(prices.head())

    #Compute returns

    returns = compute_returns(prices)
    print(returns.head())
    print(returns.describe())
    portfolio_returns = compute_portfolio_returns(returns,weights)


    var_percent,var_amount = historical_var(
        portfolio_returns,
        confidence_level= confidence_level,
        portfolio_value = portfolio_value
)
    
    print(f"\nHistorical VaR ({int(confidence_level * 100)}% confidence):")
    print(f"Var percent:{var_percent}")
    print(f"Var {var_amount}")

    var_percent_parametric, var_amount_parametric = parametric_var(
        portfolio_returns,
        confidence_level = confidence_level,
        portfolio_value = portfolio_value
    )
    print(f"Paramtric VaR ({int(confidence_level*100)}% confidence:")
    print(f"Var perentage {var_percent_parametric}")
    print(f"Var amount {var_amount_parametric}")


    var_percent_monte, var_amount_monte = monte_var(
        portfolio_returns,
        confidence_level= confidence_level,
        portfolio_value = portfolio_value
    )
    print(f"Monte Carlo VaR{int(confidence_level*100)}% confidence:")
    print(f"Var percent {var_percent_monte}")
    print(f"Var amount {var_amount_monte}")

    
if __name__ == "__main__":
    main()