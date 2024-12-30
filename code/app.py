import streamlit as st
import pandas as pd

st.write("# My Dashboard")

df = pd.read_excel('data/data.xlsx')

st.sidebar.write("## Data from Excel")
st.sidebar.write(df)

st.bar_chart(df)