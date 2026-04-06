import yfinance as yf
import pandas as pd


def download_data(tickers, start_date, end_date):
    data = yf.download(tickers,start = start_date, end = end_date)
    prices = data["Close"].copy()
    return prices


def clean_data(prices):
    cleaned = prices.dropna().copy()
    return cleaned