# Portfolio Value at Risk Dashboard

In the project i built a simple dashboard for portfolio risk analysis with Historical, parametric and Monte Carlo VaR models.

## Dashboard preview

[Dashboard](assets/dashboard1.png)

[Dashboard_graph](assets/dashboard2.png)


## Overview of the features

Users can select different assets from a list then:
- Select multiple assets
- Define the weights in the portfolio (no shorting allowed)
- Analyze the risk with different Value at Risk models
- Visualize portfolio returns over time (2023 - 2025)
- Visualize portfolio correlations


## Features
- Multi-asset portfolio selection
- Custom portfolio weights
- Historical VaR
- Parametric VaR
- Monte Carlo VaR
- Expected Shortfall
- Cumulative portfolio return plot
- Portfolio correlation heatmap
- Interactive streamlit dashboard


## Risk models

### Historical VaR
It uses the historical distribution of returns to compute the Value at Risk at a given confidence level

## Parametric VaR
It assumes that the returns are normally distributed and computes the Value at Risk at a given confidence level.

## Monte carlo VaR
It runs a number of simulation of future outcomes, computes portfolio loss in every scenario, and then computes the Value at Risk given the portfolio simulated loss distribution.

## Technologies
- Python
- numpy
- pandas
- streamlit
- matplotlib
- scipy
- yfinance


## Installation

Clone the github repositories:

``` bash
git clone https://github.com/MaicolGiordano/VaR-interactive-Dashboard.git
cd Var-interactive-Dashboard
```

Install the required libraries:

``` bash
pip install -r requirements.txt
```

Run the dashboard:

``` bash
streamlit run dashboard.py
```