import streamlit as st # type: ignore
import pandas as pd
import numpy as np

st.title("Hello World")

st.write("Writing in streamlit")

df = pd.DataFrame({'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]})
st.write('Here is the data frame:')
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)