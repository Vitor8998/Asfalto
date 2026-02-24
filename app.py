import streamlit as st
from datetime import date

# Configuração da página e Estilo Visual
st.set_page_config(page_title="AsfaltoPro Professional", layout="centered")

# CSS Customizado para dar "vida" ao app
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #FFC107;
        color: black;
        font-weight: bold;
        border: none;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div[data-testid="stExpander"] {
        border: 1px solid #d1d5db;
        border-radius: 10px;
        background-color: white;
    }
    </style>
    """, unsafe_index=True)

# --- INICIALIZAÇÃO DE DADOS ---
if 'equipe_lista' not in st.session_state:
    st.session_state.equipe_lista = [
        "Wellington luis- Encarregado", "Vitor hugo - Apontador", "Gilvan augusto - Motorista",
        "Claudinei brito jr. - Motorista", "Eduardo cruz - Op. De máquina", "Zenilton brito - Aux. De acabadora",
        "Erenilson santos - Op. De máquina", "Claudinei brito - Op. De máquina", "Ismar vicente - Op. De máquina",
        "Julio cesar - Rasteleiro", "Jhonatan kawalan - Rasteleiro", "Wagner nogueira - Ajd. Geral",
        "Elias silva - Ajd. Geral", "Laercio manoel - Ajd. Geral", "Wellington rodrigues - Ajd. Geral",
        "Israel - Op. De máquina", "Luan silveira - Op. De máquina", "Luan borges - Rasteleiro", "Alex rocha - Rasteleiro"
    ]
if 'maquinas_lista' not in st.session_state:
    st.session_state.maquinas_lista = [
        "VAN - TKP4H02", "CARRETA - IEU2A98", "PLATAFORMA - GHZ2H26", "BOBCAT", 
        "ROLO PNEU", "ROLO CHAPA", "VIBROACABADORA", "CA/ ESPARGIDOR - TIX6G72"
    ]
if 'viagens' not in st.session_state: st.session_state.viagens = []
if 'historico' not in st.session_state: st.session_state.historico = []

# --- FUNÇÕES ---
def resetar_dia():
    for c in ['loc_f', 'm2_f', 'loc_a', 'm2_a', 'viagens', 'temp_equipe', 'temp_frota', 'obs']:
        if c in st.session_state:
            if c == 'viagens': st.session_state[c] = []
            else: del st.session_state[c]
    st.rerun()

# --- TÍTULO ---
st.markdown("<h1 style='text-align: center; color: #333;'>🏗️ ASFALTO<span style='color: #FFC107;'>PRO</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Gestão de Pavimentação de Alta Performance</p>", unsafe_allow_html=True)

aba = st.tabs(["🚀 Lançamento", "📂 Histórico", "⚙️ Cadastros"])

# --- ABA 3: CADASTROS ---
with aba[2]:
    st.subheader("👥 Equipe & Frota")
    with st.container():
        col_f1, col_f2 = st.columns([3,1])
        n_f = col_f1.text_input("Novo Nome:")
        if col_f2.button("Add", key="f_btn") and n_f:
            st.session_state.equipe_lista.append(n_f)
            st.rerun()
            
        with st.expander("Gerenciar Lista de Funcionários"):
            for i, n in enumerate(st.session_state.equipe_
