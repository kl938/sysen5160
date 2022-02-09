"""
SYSEN5160
HW1
Kevin Lee
kl938@cornell.edu
08 February 2022
"""

import streamlit as st
import numpy as np
import pandas as pd

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
