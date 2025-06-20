import streamlit as st
import pandas as pd
import os

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
        pedido = {
            "Nome": nome,
            "WhatsApp": whatsapp,
            "Cupcake": cupcake,
            "Torta de Limão": torta,
            "Brigadeiro": brigadeiro
        }

        df = pd.DataFrame([pedido])

        # Cria arquivo CSV ou adiciona ao final
        file_exists = os.path.isfile("pedidos.csv")
        df.to_csv("pedidos.csv", mode="a", index=False, header=not file_exists)

        st.success("✅ Pedido enviado com sucesso!")
        st.write("Resumo do pedido:", pedido)
