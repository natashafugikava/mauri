import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

tab1, tab2, tab3 = st.tabs(['Demanda', 'Teste', 'Carne'])

with tab1:
  st.subheader('Efeito da variação no preço do próprio bem')
  
  x1=[]
  y1=[]
  for i in range(200, 1800):
    x1.append(i/100)
  for j in range(len(x1)):
     y1.append(-(1/2)*x1[j]+10)
      
  fig, ax = plt.subplots()
  plt.xlabel('Quantidade demandada')
  plt.ylabel('Preço (R$)')
  ax.scatter(x1,y1,s=10)
  st.pyplot(fig)
  
  st.subheader('Renda afetando a demanda')
  demanda = st.slider('Aumento da renda', 0.00, 1.00, 0.00, format=None)
  
  x2=[]
  for i in range(len(x1)):
    x2.append(x1[i]+5*demanda)
  y2=[]
  for i in range(len(y1)):
    y2.append(y1[i]+demanda*10)
  linhaH = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
  yH = [7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5]
  linhaV = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
  xV = [5.0,5,5,5,5,5,5,5,5,5,5,5,5,5]
  xV2 = []
  for i in range(len(xV)):
    try:
      xV2.append(x2[y2.index(7.5)])
    except:
      pass
    
  fig2, ax2 = plt.subplots()
  plt.xlabel('Quantidade demandada')
  plt.ylabel('Preço (R$)')
  plt.xlim([0,22])
  plt.ylim([0, 20])
  ax2.scatter(linhaH, yH, color='black', s=3)
  try:
    ax2.scatter(xV2,linhaV, color='black', s=3)
  except:
    pass
  ax2.scatter(xV, linhaV, color='black', s=3)
  ax2.scatter(x2,y2,color='red', s=5)
  ax2.scatter(x1,y1,s=5)
  try:
    ax2.scatter(x2[y2.index(7.5)], 7.5, color='black', s=50)
  except:
    pass
  ax2.scatter(5, 7.5, color='black', s=50)
  st.pyplot(fig2)    
    
with tab2:
  st.subheader('teste')
  st.write('a')
  
with tab3:
  st.header('Carne')
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

    x =[]
    y =[]
    for i in range(10000, 50000):
      x.append(i/1000)
    for i in range(len(x)):
      y.append(teto/x[i] + teto/(0.2*x[i] + hamb/6 + ketchup/10 + 0.02*queijo))

    data = pd.DataFrame({'x': x, 'y':y})
    fig, ax = plt.subplots()
    plt.xlabel('Preço da carne moída (Kg)')
    plt.ylabel('Consumo mensal de carne moída (Kg)')
    plt.ylim([0, 120])
    ax.scatter(x,y)
    ax.scatter(carne, consumo, color='red', s=100)
    st.pyplot(fig)
