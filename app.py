import streamlit as st
from datetime import date

# Configuração da página para Mobile
st.set_page_config(page_title="Relatório Asfalto", layout="centered")

# Inicialização de "banco de dados" temporário
if 'equipe' not in st.session_state:
    st.session_state.equipe = ["Wellington luis- Encarregado", "Vitor hugo - Apontador"]
if 'maquinas' not in st.session_state:
    st.session_state.maquinas = ["VAN - TKP4H02", "VIBROACABADORA"]

st.title("🚧 AsfaltoPro")

aba = st.tabs(["📝 Lançamento", "⚙️ Cadastros"])

with aba[1]:
    st.subheader("Gerenciar Equipe e Frota")
    nome = st.text_input("Nome e Cargo:")
    if st.button("Adicionar Funcionário"):
        st.session_state.equipe.append(nome)
        st.success(f"{nome} adicionado!")
    
    maquina = st.text_input("Máquina e Placa:")
    if st.button("Adicionar Máquina"):
        st.session_state.maquinas.append(maquina)
        st.success(f"{maquina} adicionada!")

with aba[0]:
    st.header("Novo Relatório")
    
    # Cabeçalho
    data_obra = st.date_input("Data", date.today())
    obra = st.text_input("Obra", "POÁVIAS/RODOBASE - DIADEMA")
    clima = st.selectbox("Clima", ["BOM", "NUBLADO", "CHUVA", "INSTÁVEL"])
    
    # Seleção
    st.divider()
    presenca = st.multiselect("Quem está no trecho?", st.session_state.equipe)
    frota = st.multiselect("Maquinário em uso:", st.session_state.maquinas)
    
    # Produção
    st.divider()
    local = st.text_input("Local", "Av. Corredor Abd")
    fx = st.text_input("Aplicação", "APLICAÇÃO FX 3")
    esp = st.text_input("Espessura", "3CM")
    
    col1, col2 = st.columns(2)
    m2 = col1.number_input("Total M²", step=0.01)
    ton = col2.number_input("Total Ton", step=0.01)

    # Botão de Gerar
    if st.button("GERAR RELATÓRIO PARA WHATSAPP"):
        # Cálculo de rendimento automático
        rendimento = (ton * 1000) / m2 if m2 > 0 else 0
        
        texto = f"""*RELATÓRIO DIÁRIO*

*DATA:* {data_obra.strftime('%d.%m.%Y')}
*OBRA:* {obra.upper()}
*CLIMA:* {clima}

---
*EQUIPE DE APOIO*
"""
        for i, func in enumerate(presenca, 1):
            texto += f"\n{i}. {func}"
            
        texto += f"""

---
*Produção:*
● {local}
{fx}
ESPESSURA {esp}

TOTAL= {m2:,.2f}M²
TONELADAS= {ton:,.2f}ton
(Rendimento: {rendimento:.2f} kg/m²)

---
*MAQUINÁRIO:*
"""
        for m in frota:
            texto += f"\n- {m}"
            
        st.code(texto, language="markdown")
        st.info("Toque e segure no texto acima para copiar e colar no WhatsApp.")
