import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import hvplot.pandas
import streamlit as st

st.header('Projeto Integrador I')
df = pd.read_parquet('fatec.parquet')
df = df[['ad_id', 'id_type', 'latitude', 'longitude', 'datetime_local']]
st.write(df)

st.map(df)
#gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.longitude, df.latitude), crs = 4326)
#st.write(gdf.plot(column='ad_id', markersize=5))
