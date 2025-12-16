import streamlit as st
import pandas as pd

st.title("Peak Sales Forecast Dashboard")

data = pd.read_csv("data/sales.csv")
st.line_chart(data["sales"])
