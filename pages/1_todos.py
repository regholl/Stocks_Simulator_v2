import streamlit as st


# new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
# st.markdown(new_title, unsafe_allow_html=True)

st.markdown('''
# <p style="font-family:sans-serif; color:Green; font-size: 42px;"> TODOS </p>
''', unsafe_allow_html=True)

st.checkbox('connect alpaca', value=True, disabled=True)
st.checkbox('graph: graph of one stock', value=False, disabled=False)
st.checkbox('graphs: graphs of stock indicators down the main one', value=False, disabled=False)
st.checkbox('graph: strategy yields', value=False, disabled=False)
st.checkbox('graph: distributions of std', value=False, disabled=False)
st.checkbox('graph: correlation matrix', value=False, disabled=False)
st.checkbox('optimization options', value=False, disabled=False)
