import streamlit as st
import numpy as np
import pandas as pd
import datetime
from PIL import Image

"""SYSEN5160"""
"""HW1"""
"""Kevin Lee"""
"""kl938@cornell.edu"""
"""08 February 2022"""



"""From Streamlit "Data Display" example"""
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
    
"""From Streamlit "Data Display" example"""
col1, col2, col3 = st.columns(3)
col1.metric("Bitcoin", "$50,000.00", "10%")
col2.metric("Dogecoin", "$0.00001", "-10%")
col3.metric("Sysen5130coin", "$10,000.00", "10%")

"""From Streamlit "Input Widgets" example"""
d = st.date_input(
     "What day is it today?",
     datetime.date(2022, 8, 2))
st.write('Today is:', d)

"""From Streamlit "Input Widgets" example"""
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)
    
"""From Streamlit "Media Elements" example"""
image = Image.open('sunrise.jpg')

st.image(image, caption='Sunrise by the mountains')
