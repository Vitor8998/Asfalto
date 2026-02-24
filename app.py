import streamlit as st
from datetime import date

# Configuração da página e Estilo Visual Professional
st.set_page_config(page_title="AsfaltoPro Professional", layout="centered")

# CSS para design profissional
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
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
    </style>
    """, unsafe_allow_html=True)

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

# --- FUNÇÃO DE LIMPEZA ---
def resetar_dia():
    for c in ['loc_f', 'm2_f', 'loc_a', 'm2_a', 'viagens', 'temp_equipe', 'temp_frota', 'obs', 'p_nfe']:
        if c in st.session_state:
            if c == 'viagens': st.session_state[c] = []
            else: del st.session_state[c]
    st.rerun()

# --- TÍTULO ---
st.markdown("<h1 style='text-align: center; color: #333;'>🏗️ ASFALTO<span style='color: #FFC107;'>PRO</span></h1>", unsafe_allow_html=True)

aba = st.tabs(["🚀 Lançamento", "📂 Histórico", "⚙️ Cadastros"])

# --- ABA 3: CADASTROS (CORRIGIDA) ---
with aba[2]:
    st.subheader("👥 Equipe & Frota")
    
    # Adicionar Funcionário
    c_f1, c_f2 = st.columns([3,1])
    n_f = c_f1.text_input("Novo Nome:", key="input_novo_f")
    if c_f2.button("Add", key="btn_add_f") and n_f:
        st.session_state.equipe_lista.append(n_f)
        st.rerun()
            
    with st.expander("Gerenciar Equipe (Excluir)"):
        # Criamos uma cópia para iterar sem erro de mutação
        for i, nome in enumerate(list(st.session_state.equipe_lista)):
            col_n, col_d = st.columns([5,1])
            col_n.write(f"• {nome}")
            if col_d.button("🗑️", key=f"del_f_{i}"):
                st.session_state.equipe_lista.pop(i)
                st.rerun()

# --- ABA 2: HISTÓRICO ---
with aba[1]:
    st.subheader("📅 Relatórios Salvos")
    if not st.session_state.historico:
        st.info("Nenhum registro encontrado.")
    else:
        for idx, r in enumerate(reversed(st.session_state.historico)):
            with st.expander(f"📌 {r['data']} - {r['obra']}"):
                st.code(r['texto'])
        if st.button("🗑️ Limpar Todo Histórico"):
            st.session_state.historico = []
            st.rerun()

# --- ABA 1: LANÇAMENTO ---
with aba[0]:
    if st.button("⚡ SELECIONAR EQUIPE COMPLETA"):
        st.session_state.temp_equipe = st.session_state.equipe_lista
        st.session_state.temp_frota = st.session_state.maquinas_lista
        st.rerun()

    with st.container():
        c1, c2 = st.columns(2)
        data_obra = c1.date_input("🗓️ Data", date.today())
        clima = c2.selectbox("🌤️ Clima", ["BOM", "NUBLADO", "CHUVA", "INSTÁVEL"])
        obra = st.text_input("📍 Obra", "POÁVIAS/RODOBASE - DIADEMA")

    st.markdown("### 👷 Recursos")
    sel_equipe = st.multiselect("Funcionários", sorted(st.session_state.equipe_lista), default=st.session_state.get('temp_equipe', []))
    sel_frota = st.multiselect("Equipamentos", sorted(st.session_state.maquinas_lista), default=st.session_state.get('temp_frota', []))

    st.divider()
    st.markdown("### 🚚 Recebimento de Massa")
    v_col1, v_col2 = st.columns([2,1])
    p_nfe = v_col1.number_input("Peso da Nota (Ton)", step=0.01, key="p_nfe")
    if v_col2.button("➕ ADICIONAR"):
        if p_nfe > 0:
            st.session_state.viagens.append(p_nfe)
            st.rerun()
    
    total_ton = sum(st.session_state.viagens)
    mc1, mc2 = st.columns(2)
    mc1.metric("Total Toneladas", f"{total_ton:.2f} t")
    mc2.metric("Nº de Viagens", len(st.session_state.viagens))

    st.divider()
    st.markdown("### 📏 Produção")
    loc_a = st.text_input("Trecho/Rua", "Av. Corredor Abd", key="loc_a")
    col_p1, col_p2 = st.columns(2)
    m2_a = col_p1.number_input("Área Aplicação (m²)", step=0.01, key="m2_a")
    m2_f = col_p2.number_input("Área Fresagem (m²)", step=0.01, key="m2_f")
    
    obs = st.text_area("🗒️ Observações", key="obs")

    st.divider()
    if st.button("✅ GERAR RELATÓRIO"):
        rel = f"""RELATÓRIO DIÁRIO\n\nDATA: {data_obra.strftime('%d.%m.%Y')}\nOBRA: {obra.upper()}\nCLIMA: {clima}\n\n---\nEQUIPE DE APOIO:"""
        for i, f in enumerate(sel_equipe, 1): rel += f"\n{i}. {f}"
        rel += f"\n\n---\nPRODUÇÃO:\n● {loc_a}\nTOTAL M²: {m2_a:,.2f}\nFRESAGEM: {m2_f:,.2f} M²\nTOTAL TON: {total_ton:,.2f}\nVIAGENS: {len(st.session_state.viagens)}"
        rel += f"\n\nEQUIPAMENTOS:"
        for m in sel_frota: rel += f"\n- {m}"
        if obs: rel += f"\n\nOBS: {obs}"
        
        st.session_state.historico.append({"data": data_obra.strftime('%d/%m'), "obra": obra, "texto": rel})
        st.code(rel)

    if st.button("♻️ NOVO DIA (LIMPAR)"):
        resetar_dia()
