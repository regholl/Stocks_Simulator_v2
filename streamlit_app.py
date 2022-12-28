import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
# from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.live import StockDataStream

st.write('# Welcome To Market Analysis App!')


# def life_data():
#     stock_stream = StockDataStream(API_KEY, SECRET_KEY)
#
#     async def bar_callback(bar):
#         for property_name, value in bar:
#             st.write(f"\"{property_name}\": {value}")
#
#     # Subscribing to bar event
#     symbol = "TSLA"
#     stock_stream.subscribe_bars(bar_callback, symbol)
#
#     stock_stream.run()


# st.write('before!!!')
# life_data()
# st.write('after!!!')



