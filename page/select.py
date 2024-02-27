import streamlit as st
import controller.users as users

def consultar():
    st.title('Consultar')
    colunas = st.columns((1,2))
    campos = ['Chave', 'Name']
    
    for item in users.selecionar():
        col1, col2 = st.columns((1,2))
        
        col1.write(item[0])
        col2.write(item[1])
        
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)