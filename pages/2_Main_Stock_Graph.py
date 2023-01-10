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
from globals import stocks_names_list

st.set_page_config(layout="wide")
API_KEY = st.secrets.alpaca_api_key
SECRET_KEY = st.secrets.alpaca_secret_key


# ------------------------------------ #
# ------------------------------------ #
# ------------------------------------ #
# FUNCTIONS
# ------------------------------------ #
# ------------------------------------ #
# ------------------------------------ #

@st.cache(allow_output_mutation=True)
def historical_data(stock):
    client = StockHistoricalDataClient(API_KEY, SECRET_KEY)
    request_params = StockBarsRequest(
        symbol_or_symbols=[stock],
        timeframe=TimeFrame.Hour,
        start="2018-01-01 00:00:00"
    )
    bars = client.get_stock_bars(request_params)
    curr_bars_df = bars.df
    curr_bars_df['datetime'] = [index[1] for index in curr_bars_df.index]
    # return bars.df
    return curr_bars_df


# ------------------------------------ #
# ------------------------------------ #
# ------------------------------------ #
# ST
# ------------------------------------ #
# ------------------------------------ #
# ------------------------------------ #

# ------------------------------------ #
# ------------------------------------ #
# ------------------------------------ #
# Sidebar
# ------------------------------------ #
# ------------------------------------ #
# ------------------------------------ #
# st.sidebar.write('## Select a stock:')
selected_stock = st.sidebar.selectbox("Select a stock:", stocks_names_list)  # , label_visibility='hidden'
rsi_bool = st.sidebar.checkbox('rsi', value=True, disabled=False)
ma_bool = st.sidebar.checkbox('ma', value=False, disabled=False)

# ------------------------------------ #
# ------------------------------------ #
# ------------------------------------ #
# Main
# ------------------------------------ #
# ------------------------------------ #
# ------------------------------------ #

st.write(f'# Stock Analysis - {selected_stock}')

with st.spinner('Wait for it...'):
    cols_names = ['1D','5D','1M','6M','YTD','1Y','5Y','MAX']
    cols = st.columns(8)
    for col, col_name in zip(cols, cols_names):
        with col:
            st.button(f'{col_name}')
    bars_df = historical_data(selected_stock)
    fig = px.line(bars_df, x='datetime', y='close', title='Time Series with Range Slider and Selectors')
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    st.plotly_chart(fig, theme=None, use_container_width=True)
    expander = st.expander("See The Data")
    expander.write(bars_df)

# bars_df['index'] = list(range(len(bars_df['open'])))
# # index_list = list(range(len(bars_df['open'])))
# fig = px.line(
#     bars_df,
#     # x=index_list,
#     x='index',
#     y='open'
# )



if rsi_bool:
    st.write('here RSI graph')

if ma_bool:
    st.write('here MA graph')

# ------------------------------------ #
# ------------------------------------ #
# ------------------------------------ #

st.subheader("Define a custom colorscale")
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_conatiner_width=True)

df = px.data.gapminder()
print()
fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)