import streamlit as st
import numpy as np
import pandas as pd
import datetime

"""SYSEN5160"""
"""HW1"""
"""Kevin Lee"""
"""kl938@cornell.edu"""
"""08 February 2022"""





"""Lines 13-17 from Streamlit "Getting Started" example"""
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

"""Lines 21-25 from Streamlit "Getting Started" example"""
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

"""Lines 28-32 from Streamlit "Getting Started" example"""
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

"""Lines 35-40 from Streamlit "Getting Started" example"""
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
"""Lines 45-48 from Streamlit "Data Display" example"""
col1, col2, col3 = st.columns(3)
col1.metric("Bitcoin", "$50,000.00", "10%")
col2.metric("Dogecoin", "$0.00001", "-10%")
col3.metric("Sysen5130coin", "$10,000.00", "10%")

"""Lines 51-54 from Streamlit "Input Widgets" example"""
d = st.date_input(
     "What day is it today?",
     datetime.date(2022, 8, 2))
st.write('Today is:', d)
