import streamlit as st

# Configuração do título da página
st.set_page_config(page_title="Formulário - Sucesso em Vendas", layout="centered")

# Estilização personalizada
st.markdown(
    """
    <style>
        /* Centralizar a logo */
        .center-logo {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        /* Centralizar título e descrição */
        .center-text {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Adicionar a logo centralizada
st.markdown(
    """
    <div class="center-logo">
        <img src="assets/img/LOGO SUCESSO EM VENDAS HORIZONTAL AZUL.png" alt="Sucesso em Vendas" width="300">
    </div>
    """,
    unsafe_allow_html=True,
)

# Título e descrição
st.markdown("<h2 class='center-text' style='color: #007BFF;'>Formulário - Sucesso em Vendas</h2>", unsafe_allow_html=True)
st.markdown("<p class='center-text'>Por favor, preencha o formulário abaixo para que possamos ajudá-lo da melhor forma!</p>", unsafe_allow_html=True)

# Embedding do Typeform
typeform_embed = """
<div data-tf-live="01JD7E0BF6RPPBPDRR8SW75P0H" data-tf-hide-headers data-tf-hide-footer></div>
<script src="//embed.typeform.com/next/embed.js"></script>
"""
st.components.v1.html(typeform_embed, height=700)
