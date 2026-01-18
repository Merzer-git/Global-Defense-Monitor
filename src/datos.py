import pandas as pd
import streamlit as st

@st.cache_data
def cargar_datos():
    df = pd.read_parquet("data/datos_militares_final.parquet")
    return df