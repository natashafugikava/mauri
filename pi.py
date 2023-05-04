import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import hvplot.pandas
import streamlit as st

st.header('Projeto Integrador I')
df = pd.read_parquet('fatec.parquet')
st.write(df)
