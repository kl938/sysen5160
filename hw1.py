import streamlit as st
import numpy as np
import pandas as pd
import datetime
from PIL import Image
import matplotlib.pyplot as plt

"""SYSEN5160"""
"""HW1"""
"""Kevin Lee"""
"""kl938@cornell.edu"""
"""08 February 2022"""

"""From Streamlit "Write and Magic" example"""
st.write(1234)
st.write(pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
 }))

"""From Streamlit "Write and Magic" example"""
df = pd.DataFrame({'col1': [1,2,3]})
df  # Draw the dataframe

x = 10
'x', x  # Draw the string 'x' and then the value of x

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # Draw a Matplotlib chart

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
image = Image.open('cornell.png')

st.image(image, caption='Cornell University')

"""From Streamlit "Layout Containers" example"""
col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)

"""From Streamlit "Layouts and Containers" example"""
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

"""From Streamlit "Status elements" example"""
st.success('This is a success message!')

"""From Streamlit "Status Elements" example"""
st.warning('This is a warning')

"""From Streamlit Control flow example"""
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

""" """

