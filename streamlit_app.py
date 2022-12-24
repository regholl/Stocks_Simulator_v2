import streamlit as st

st.write('Hello APP NT!')

st.write('# Secrets:')
st.write(f'{st.secrets.db_username} {st.secrets.db_password}')
