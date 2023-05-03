import streamlit as st
import pandas as pd
import altair as alt

st.write('Demanda mensal de carne moída para uma família de 5 pessoas.')
st.write('A família usa carne moída para fazer vários pratos, inclusive hambúrguer.')
st.write('Dada uma situação, que inclui preços de vários produtos, renda, e preferências , a família decide quanto de carne moída precisa (ou pode) comprar.')

col1, col2 = st.columns([1,3])
  
with col1:
  carne = st.slider('Preço da carne moída (Kg)', 10.00, 50.00, 30.00)
  hamb = st.slider('Preço do pão de hambúrguer (unidade)', 5.00, 10.00, 7.50)
  ketchup = st.slider('Preço do ketchup (500g)', 5.00, 20.00, 10.00)
  queijo = st.slider('Preço da mussarela (Kg)', 20.00, 100.00, 45.00)
  renda = st.slider('Renda mensal (R$)', 1000.00, 20000.00, 2000.00)
  
with col2:
  st.write('Espaço reservado para o gráfico.')
