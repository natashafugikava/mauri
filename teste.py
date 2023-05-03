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
teto = renda*0.03
consumo = teto/carne + teto/lanche
  
with col2:
  st.write('Espaço reservado para o gráfico.')
  st.write(f'Gasto total com carne e sanduíches: R$ {2*teto:.2f}')
  st.write(f'Consumo total de carne para outros fins: {teto/carne:.2f} Kg')
  st.write(f'Consumo total de carne com sanduíches: {teto/lanche*0.2:.2f} Kg')
  st.write(f'Consumo total de sanduíches mensais: {teto/lanche:.2f} unidades')
  st.write(f'Consumo total de sanduíches mensais por pessoa: {teto/lanche/5:.2f} unidades')
import altair as alt
import pandas as pd

import altair as alt
import pandas as pd

x =[]
y =[]
for i in range(10, 50, 0.001):
  x.append(i)
  y.append(teto/i + teto/(0.2*i + hamb/6 + ketchup/10 + 0.02*queijo))

data = pd.DataFrame({'t': range(101)})
