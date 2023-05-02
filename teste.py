import streamlit as st

st.write('Demanda mensal de carne moída para uma família de 5 pessoas.')
st.write('A família usa carne moída para fazer vários pratos, inclusive hambúrguer.')
st.write('Dada uma situação, que inclui preços de vários produtos, renda, e preferências , a família decide quanto de carne moída precisa (ou pode) comprar.')

# st.slider('Preço da carne moída (Kg)', 10, 50, 30, 0.01)
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
