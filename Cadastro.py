import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📖",
    layout="centered")

def gravar_dados(nome, cpf, data_nasc, endereco, telefone, tipo):
    if nome and data_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {cpf}, {data_nasc}, {endereco}, {telefone}, {tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.title("Cadastro de Clientes")
st.divider()

col1, col2, col3 = st.columns(3)

nome = col1.text_input("Digite o nome do cliente:",
                     key="nome_cliente")
cpf = col2.text_input("Digite o número do CPF do cliente:", 
                    max_chars=11,
                    key="cpf_cliente")
dt_nasc = col1.date_input("Selecione a idade do cliente:",
                      key="dt_nasc_cliente",
                      format="DD/MM/YYYY")
endereco = st.text_input("Digite o enderço do cliente:",
                         key="endereco_cliente")
telefone = col2.text_input("Digite o número de telefone:",
                         key="telefone_cliente")
tipo = col3.selectbox("Tipo do cliente",
                    ["Pessoa Física",
                     "Jurídica"])

bt_cadastrar = st.button("Cadastrar",
                      key="_bt_cadastrar",
                      on_click=gravar_dados,
                      args=[nome, cpf, dt_nasc, endereco, telefone, tipo])

if bt_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="❌")
