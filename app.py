import os
import json
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime  # <== Importar datetime

scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

json_creds = os.getenv("GOOGLE_CREDS")

if not json_creds:
    st.error("Erro: variável GOOGLE_CREDS não definida")
else:
    # Converte as barras duplas \n em quebras de linha reais
    json_creds = json_creds.replace('\\n', '\n')

    creds_dict = json.loads(json_creds)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
    client = gspread.authorize(creds)

    # Abre a planilha
    SHEET_ID = "1BRXyNFd0Evog97EhbNTmE7J7dp1rP10t3bQtJA41_M8"
    sheet = client.open_by_key(SHEET_ID).sheet1

    st.title("🧁 Pedido – Confeitaria Doçura")

    nome = st.text_input("Nome completo")
    whatsapp = st.text_input("WhatsApp")

    st.subheader("Escolha seus produtos")
    cupcake = st.number_input("Cupcake – R$8", min_value=0, step=1)
    torta = st.number_input("Torta de Limão – R$45", min_value=0, step=1)
    brigadeiro = st.number_input("Brigadeiro – R$3", min_value=0, step=1)

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
