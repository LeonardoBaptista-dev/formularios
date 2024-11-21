import streamlit as st

# Configuração do título da página
st.set_page_config(page_title="Formulário - Sucesso em Vendas", layout="centered")

# Adicionar a logo no topo
st.image("LOGO SUCESSO EM VENDAS HORIZONTAL AZUL.png", width=200)

# Título e descrição
st.markdown("<h2 style='text-align: center; color: #007BFF;'>Formulário - Sucesso em Vendas</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Por favor, preencha o formulário abaixo para que possamos ajudá-lo da melhor forma!</p>", unsafe_allow_html=True)

# Embedding do Typeform
typeform_embed = """
<div data-tf-live="01JD7E0BF6RPPBPDRR8SW75P0H"></div>
<script src="//embed.typeform.com/next/embed.js"></script>
"""
st.components.v1.html(typeform_embed, height=700)
