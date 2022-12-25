import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.live import StockDataStream

st.write('Hello APP NT!')

API_KEY = st.secrets.alpaca_api_key
SECRET_KEY = st.secrets.alpaca_secret_key


def historical_data():
    client = StockHistoricalDataClient(API_KEY, SECRET_KEY)
    request_params = StockBarsRequest(
        symbol_or_symbols=["SPY"],
        timeframe=TimeFrame.Day,
        start="2022-01-01 00:00:00"
    )
    bars = client.get_stock_bars(request_params)
    return bars.df


bars_df = historical_data()
bars_df['index'] = list(range(len(bars_df['open'])))
fig = px.line(
    bars_df,
    x='index',
    y='open'
)
st.plotly_chart(fig, theme=None, use_container_width=True)


def life_data():
    stock_stream = StockDataStream(API_KEY, SECRET_KEY)

    async def bar_callback(bar):
        for property_name, value in bar:
            print(f"\"{property_name}\": {value}")

    # Subscribing to bar event
    symbol = "TSLA"
    stock_stream.subscribe_bars(bar_callback, symbol)

    stock_stream.run()