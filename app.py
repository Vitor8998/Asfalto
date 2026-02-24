import streamlit as st
from datetime import date

st.set_page_config(page_title="Apontamento de Obra", layout="wide")

# --- BANCO DE DADOS SIMULADO (Pode ser substituído por um arquivo) ---
if 'equipe' not in st.session_state:
    st.session_state.equipe = ["Wellington luis", "Vitor hugo", "Gilvan augusto"] # Exemplo
if 'maquinas' not in st.session_state:
    st.session_state.maquinas = ["VAN - TKP4H02", "ROLO PNEU", "VIBROACABADORA"]

st.sidebar.title("Navegação")
aba = st.sidebar.radio("Ir para:", ["Lançamento Diário", "Cadastros"])

# --- ABA DE CADASTROS ---
if aba == "Cadastros":
    st.header("⚙️ Cadastro de Recursos")
    
    novo_func = st.text_input("Novo Funcionário (Nome - Cargo):")
    if st.button("Adicionar Funcionário"):
        st.session_state.equipe.append(novo_func)
        st.success("Adicionado!")

    nova_maq = st.text_input("Nova Máquina/Veículo (Nome - Placa):")
    if st.button("Adicionar Máquina"):
        st.session_state.maquinas.append(nova_maq)
        st.success("Adicionado!")

# --- ABA DE LANÇAMENTO ---
else:
    st.header("📝 Relatório de Obra")
    
    col1, col2 = st.columns(2)
    with col1:
        data_obra = st.date_input("Data:", date.today())
        obra_nome = st.text_input("Obra:", "POÁVIAS/RODOBASE - DIADEMA")
    with col2:
        clima = st.selectbox("Clima:", ["BOM", "NUBLADO", "CHUVA", "INSTÁVEL"])

    st.subheader("👥 Selecione a Equipe no Trecho")
    equipe_selecionada = st.multiselect("Funcionários presentes:", st.session_state.equipe)

    st.subheader("🚜 Maquinário Utilizado")
    maquinas_selecionadas = st.multiselect("Equipamentos em operação:", st.session_state.maquinas)

    st.subheader("🛣️ Produção")
    local = st.text_input("Local (Ex: Av. Corredor Abd):")
    fx = st.text_input("Faixa/Capa (Ex: APLICAÇÃO FX 3):")
    espessura = st.text_input("Espessura (Ex: 3CM):")
    
    c1, c2 = st.columns(2)
    m2 = c1.number_input("Total M²:", format="%.2f")
    ton = c2.number_input("Total Toneladas:", format="%.2f")

    if st.button("GERAR RELATÓRIO FINAL"):
        st.divider()
        relatorio = f"""
RELATÓRIO DIÁRIO

DATA: {data_obra.strftime('%d.%m.%Y')}
OBRA: {obra_nome.upper()}
CLIMA: {clima}

---
EQUIPE DE APOIO
"""
        for i, nome in enumerate(equipe_selecionada, 1):
            relatorio += f"\n{i}. {nome}"
            
        relatorio += f"""

---
Produção:
● {local}
{fx}
ESPESSURA {espessura}

TOTAL= {m2:,.2f}M²
TONELADAS= {ton:,.2f}ton

---
EQUIPAMENTOS:
"""
        for maq in maquinas_selecionadas:
            relatorio += f"\n{maq}"

        st.text_area("Copiável:", relatorio, height=400)
        st.download_button("Baixar Relatório .txt", relatorio, file_name=f"Relatorio_{data_obra}.txt")
