import streamlit as st
import pandas as pd
import altair as alt

# situação exemplo de oferta e demanda de carne moída que depende de vários fatores
st.write('Demanda mensal de carne moída para uma família de 5 pessoas.')
st.write('A família usa carne moída para fazer vários pratos, inclusive hambúrguer.')
st.write('Dada uma situação, que inclui preços de vários produtos e sua renda, a família decide quanto de carne moída precisa (ou pode) comprar.')

col1, col2 = st.columns([1,3])

# barras que determinam o preço dos produtos e o salário da família
with col1:
  # (nome do produto, preço mínimo, preço máximo, preço padrão)
  carne = st.slider('Preço da carne moída (Kg)', 10.00, 50.00, 30.00)
  hamb = st.slider('Preço do pão de hambúrguer (6 unidades)', 5.00, 20.00, 7.50)
  ketchup = st.slider('Preço do ketchup (500g)', 5.00, 20.00, 10.00)
  queijo = st.slider('Preço da mussarela (Kg)', 20.00, 100.00, 45.00)
  renda = st.slider('Renda mensal (R$)', 1000.00, 20000.00, 2000.00)
  
# preço médio da fabricação de um sanduíche que usa:
# 200g de carne, 1 pão, 50g de ketchup e 20g de queijo
lanche = 0.2*carne + hamb/6 + ketchup/10 + 0.02*queijo

# a família vai gastar até 3% de sua renda com carne moída para fins diversos
# a família vai gastar até 3% de sua renda na confecção de sanduíches
  
with col2:
  st.write('Espaço reservado para o gráfico.')
