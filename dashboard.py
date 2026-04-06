import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from data_loader import download_data,clean_data
from portfolio import compute_returns, compute_portfolio_returns
from var_models import historical_var, parametric_var, monte_var,historical_short





st.sidebar.title("Portfolio parameters")

available_tickers = {
       "SPY - S&P 500 ETF":"SPY",
        "AGG - US Bond ETF":"AGG",
        "GLD - Gold ETF": "GLD",
        "AAPL - Apple": "AAPL",
        "MSFT - Microsoft": "MSFT",
        "GOOGL - Alphabet": "GOOGL",
        "AMZN - Amazon": "AMZN",
        "NVDA - Nvidia": "NVDA",
        "TSLA - Tesla": "TSLA",
        "META - Meta": "META",
        "JPM - JPMorgan": "JPM",
        "XOM - Exxon Mobil": "XOM",
        "JNJ - Johnson & Johnson": "JNJ",
        "KO - Coca-Cola": "KO",
        "WMT - Walmart": "WMT"
 }




selected_labels = st.sidebar.multiselect(
    "Select assets",
    list(available_tickers.keys()),
    default = ["SPY - S&P 500 ETF","AGG - US Bond ETF","GLD - Gold ETF"]
    )

selected_tickers = [available_tickers[i] for i in selected_labels]

weights = []

for ticker in selected_tickers:
    weight = st.sidebar.number_input(f"Weight for {ticker}",
                                min_value =0.0,
                                max_value = 1.0,
                                value = 0.0,
                                step = 0.1)
    weights.append(weight)

weights_df = pd.DataFrame({
        "Asset":selected_labels,
        "Weight":(f"{w*100:.2f}%" for w in weights)
    })

st.subheader("Selected portfolio")
st.dataframe(weights_df)

if len(selected_tickers) == 0:
        st.warning("Please select at least one asset.")
        st.stop()
if len(selected_tickers) > 6:
       st.warning("Please select at most 6 assets")
       st.stop()
if abs(sum(weights) - 1.0) > 0.0001:
        st.error("The sum of weights must be equal to 1")
        st.stop()    

portfolio_value = st.sidebar.number_input("Portfolio_value", value = 1000000, step = 1000)

confidence_level = st.sidebar.slider("Confidence Level", 
                                min_value = 0.90, 
                                max_value = 0.99, 
                                value = 0.95)

simulations = st.sidebar.slider(
        "Monte Carlo simulations",
        100,
        20000,
        10000
    )

prices = download_data(selected_tickers, "2023-01-01","2025-12-31")
prices = clean_data(prices)



returns = compute_returns(prices)
correlation = returns.corr()


portfolio_returns = compute_portfolio_returns(returns, weights)
cum_ret = np.exp(portfolio_returns.cumsum())-1

hist_var_percent, hist_var_amount = historical_var(
        portfolio_returns,
        confidence_level,
        portfolio_value
    )

param_var_percent, param_var_amount = parametric_var(
        portfolio_returns,
        confidence_level,
        portfolio_value
    )

mc_var_percent, mc_var_amount = monte_var(
        portfolio_returns,
        confidence_level,
        portfolio_value,
        simulations
    )
es_hist_percent, es_hist_amount = historical_short(
       portfolio_returns,
       confidence_level,
       portfolio_value
) 





st.subheader("Correlation matrix of assets")
fig2,ax2 = plt.subplots()
cax = ax2.imshow(correlation, cmap="coolwarm")
for i in range(len(correlation.index)):
    for j in range(len(correlation.columns)):
        ax2.text(
            j,
            i,
            f"{correlation.iloc[i, j]:.2f}",
            ha="center",
            va="center",
            color="black"
        )

ax2.set_xticks(range(len(correlation.columns)))
ax2.set_yticks(range(len(correlation.index)))


ax2.set_xticklabels(correlation.columns, rotation=45)
ax2.set_yticklabels(correlation.index)
fig2.colorbar(cax)
st.pyplot(fig2)


st.subheader("Value at Risk and Expected shortfall")

st.metric("Historical VaR:",f"€{hist_var_amount:,.2f}")
st.metric("Parametric VaR:",f"€{param_var_amount:,.2f}")
st.metric("Monte Carlo VaR:",f"€{mc_var_amount:,.2f}")
st.metric("Expected shortfall", f"€{es_hist_amount:,.2f}")
st.write(f"{es_hist_percent:,.2%} of the portfolio ")





fig1, ax1 = plt.subplots()
ax1.plot(cum_ret.index, cum_ret.values)
ax1.set_xlabel("Date")
ax1.set_ylabel("Cumulative return")
ax1.set_title("Cumulative Portfolio return")
ax1.grid(True)
plt.xticks(rotation = 45)
st.pyplot(fig1)


