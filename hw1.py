"""
SYSEN5160
HW1
Kevin Lee
kl938@cornell.edu
08 February 2022
"""

import streamlit as st
import pandas as pd

"""Lines 13-17 from Streamlit "Getting Started" example"""
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

