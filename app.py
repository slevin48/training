import streamlit as st
import pandas as pd

st.write("# My Dashboard")

df = pd.read_excel('data.xlsx')
st.write(df)

st.bar_chart(df)