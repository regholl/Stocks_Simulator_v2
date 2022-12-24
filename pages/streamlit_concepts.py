import streamlit as st
import pandas as pd
import numpy as np

st.write('# How to get secrets:')
st.write(f'{st.secrets.db_username} {st.secrets.db_password}')

st.write('# Dataframes')

st.write(" ## Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)
st.table(df)
st.dataframe(df)

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=[f'col {i}' for i in range(20)])

st.dataframe(dataframe.style.highlight_max(axis=0))

st.write('# Charts')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# ------------------------------ #

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.write('# Widgets')

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.write(st.session_state.name)
st.write(st.session_state)

st.write('# Checkbox')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.write(chart_data)

st.write('# Selecbox')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4, 5],
    'second column': [10, 20, 30, 40, 50]
})

option = st.selectbox(
    'Which number do you like best?',
    df['second column'])

st.write('You selected: ', option)

st.write('# Layout')




