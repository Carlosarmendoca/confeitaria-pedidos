import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Autenticação com Google Sheets
scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("pedidos-confeitaria-11afb40cb7ed.json", scopes)
client = gspread.authorize(creds)

# Abre a planilha (coloque seu ID aqui)
SHEET_ID = "1BRXyNFd0Evog97EhbNTmE7J7dp1rP10t3bQtJA41_M8"
sheet = client.open_by_key(SHEET_ID).sheet1

st.title("🧁 Pedido – Confeitaria Doçura")

# Dados do cliente
nome = st.text_input("Nome completo")
whatsapp = st.text_input("WhatsApp")

# Produtos e quantidades
st.subheader("Escolha seus produtos")
cupcake = st.number_input("Cupcake – R$8", min_value=0, step=1)
torta = st.number_input("Torta de Limão – R$45", min_value=0, step=1)
brigadeiro = st.number_input("Brigadeiro – R$3", min_value=0, step=1)

# Botão de envio
if st.button("Enviar pedido"):
    if not nome or not whatsapp:
        st.warning("Por favor, preencha seu nome e WhatsApp.")
    else:
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        pedido = [
            data,
            nome,
            whatsapp,
            cupcake,
            torta,
            brigadeiro
        ]
        
        # Envia para a planilha
        sheet.append_row(pedido)

        st.success("✅ Pedido enviado com sucesso!")
        st.write("Resumo do pedido:")
        st.write({
            "Data": data,
            "Nome": nome,
            "WhatsApp": whatsapp,
            "Cupcake": cupcake,
            "Torta de Limão": torta,
            "Brigadeiro": brigadeiro
        })
