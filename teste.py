import streamlit as st

st.write('Demanda mensal de carne moída para uma família de 5 pessoas.')
st.write('A família usa carne moída para fazer vários pratos, inclusive hambúrguer.')
st.write('Dada uma situação, que inclui preços de vários produtos, renda, e preferências , a família decide quanto de carne moída precisa (ou pode) comprar.')

st.slider(label='Preço da carne moída (Kg)', min_value=10, max_value=50, value=30, step=0.01)
