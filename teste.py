import streamlit as st

st.write('Demanda mensal de carne moída para uma família de 5 pessoas.')
st.write('A família usa carne moída para fazer vários pratos, inclusive hambúrguer.')
st.write('Dada uma situação, que inclui preços de vários produtos, renda, e preferências , a família decide quanto de carne moída precisa (ou pode) comprar.')

st.slider('Preço da carne moída (Kg)', 10.00, 50.00, 30.00)
st.slider('Preço do pão de hambúrguer (unidade)', 5.00, 10.00, 7.50)
