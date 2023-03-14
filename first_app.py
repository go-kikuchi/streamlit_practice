import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('My first app')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
st.write(df)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [35.7, 139.67],
    columns=['lat', 'lon']
)
st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    })

option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

st.write('You selected: ', option)


st.write('Starting a long computation...')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

st.write('...and now we\'re done!')