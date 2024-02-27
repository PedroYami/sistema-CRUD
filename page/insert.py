import streamlit as st
import controller.users as users

def inserir():
    st.title('Digite seus Dados')
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Digite o nome')
        input_matricula = st.text_input(label='Digite a matrícula')
        input_senha = st.text_input(label='Digite a senha')
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            users.incluir(input_name, input_matricula, input_senha)
            st.success('Dados incluidos')