import streamlit as st
from datetime import date

# Configuração da página para Celular
st.set_page_config(page_title="AsfaltoPro - Apontamento", layout="centered")

# --- BANCO DE DADOS EM MEMÓRIA ---
if 'equipe' not in st.session_state:
    st.session_state.equipe = [
        "Wellington luis- Encarregado", "Vitor hugo - Apontador", "Gilvan augusto - Motorista",
        "Claudinei brito jr. - Motorista", "Eduardo cruz - Op. De máquina", "Zenilton brito - Aux. De acabadora",
        "Erenilson santos - Op. De máquina", "Claudinei brito - Op. De máquina", "Ismar vicente - Op. De máquina",
        "Julio cesar - Rasteleiro", "Jhonatan kawalan - Rasteleiro", "Wagner nogueira - Ajd. Geral",
        "Elias silva - Ajd. Geral", "Laercio manoel - Ajd. Geral", "Wellington rodrigues - Ajd. Geral",
        "Israel - Op. De máquina", "Luan silveira - Op. De máquina", "Luan borges - Rasteleiro", "Alex rocha - Rasteleiro"
    ]
if 'maquinas' not in st.session_state:
    st.session_state.maquinas = [
        "VAN - TKP4H02", "CARRETA - IEU2A98", "PLATAF
