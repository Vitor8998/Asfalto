import streamlit as st
from datetime import date

# Configuração da página para Celular
st.set_page_config(page_title="AsfaltoPro - Apontamento", layout="centered")

# --- INICIALIZAÇÃO DO BANCO DE DADOS ---
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
        "VAN - TKP4H02", "CARRETA - IEU2A98", "PLATAFORMA - GHZ2H26", "BOBCAT", 
        "ROLO PNEU", "ROLO CHAPA", "VIBROACABADORA", "CA/ ESPARGIDOR - TIX6G72"
    ]
if 'historico' not in st.session_state:
    st.session_state.historico = []
if 'viagens' not in st.session_state:
    st.session_state.viagens = []

# --- FUNÇÃO DE LIMPEZA CORRIGIDA ---
def resetar_formulario():
    # Em vez de setar os valores, limpamos as chaves para o Streamlit recriar os campos do zero
    chaves_para_limpar = ['loc_f', 'm2_f', 'loc_a', 'm2_a', 'viagens']
    for chave in chaves_para_limpar:
        if chave in st.session_state:
            if chave == 'viagens':
                st.session_state[chave] = []
            else:
                del st.session_state[chave]
    st.rerun()

st.title("🚧 AsfaltoPro")

aba = st.tabs(["📝 Lançamento", "📂 Histórico", "⚙️ Cadastros"])

# --- ABA 3: CADASTROS ---
with aba[2]:
    st.subheader("Gerenciar Equipe e Frota")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        nome_novo = st.text_input("Novo Funcionário:")
        if st.button("Adicionar Nome"):
            st.session_state.equipe.append(nome_novo)
            st.rerun()
    with col_c2:
        maquina_nova = st.text_input("Nova Máquina:")
        if st.button("Adicionar Máquina"):
            st.session_state.maquinas.append(maquina_nova)
            st.rerun()

# --- ABA 2: HISTÓRICO ---
with aba[1]:
    st.subheader("Relatórios Salvos")
    if not st.session_state.historico:
        st.write("Nenhum relatório salvo.")
    else:
        for i, rel in enumerate(reversed(st.session_state.historico)):
            with st.expander(f"Relatório {rel['data']} - {rel['obra']}"):
                st.code(rel['texto'], language="markdown")
        if st.button("🗑️ Limpar Todo Histórico"):
            st.session_state.historico = []
            st.rerun()

# --- ABA 1: LANÇAMENTO ---
with aba[0]:
    st.header("Relatório Diário")
    
    data_obra = st.date_input("Data", date.today())
    obra = st.text_input("Obra", "POÁVIAS/RODOBASE - DIADEMA")
    clima = st.selectbox("Clima", ["BOM", "NUBLADO", "CHUVA", "INSTÁVEL"])
    
    st.divider()
    presenca = st.multiselect("Equipe no Trecho:", sorted(st.session_state.equipe))
    frota = st.multiselect("Maquinário em Uso:", sorted(st.session_state.maquinas))
    
    st.divider()
    st.subheader("⛏️ Produção de Fresagem")
    check_fresagem = st.checkbox("Houve fresagem?")
    loc_f = st.text_input("Local da Fresagem", key="loc_f")
    m2_f = st.number_input("Total M² (Fresagem)", step=0.01, key="m2_f")
    esp_f = st.text_input("Espessura (Fresagem)", "5CM")
    
    st.divider()
    st.subheader("🚛 Controle de Massa (Viagens)")
    
    col_v1, col_v2 = st.columns([2, 1])
    peso_nfe = col_v1.number_input("Peso da Nota (Toneladas)", min_value=0.0, step=0.01)
    if col_v2.button("➕ Adicionar"):
        if peso_nfe > 0:
            st.session_state.viagens.append(peso_nfe)
            st.rerun()
    
    total_ton = sum(st.session_state.viagens)
    st.info(f"🚚 **Total Acumulado:** {total_ton:.2f} ton | **Viagens:** {len(st.session_state.viagens)}")
    
    st.divider()
    st.subheader("🏗️ Aplicação (Capa)")
    loc_a = st.text_input("Local da Aplicação", key="loc_a")
    faixa_a = st.text_input("Faixa/Capa", "APLICAÇÃO FX 3")
    esp_a = st.text_input("Espessura (Capa)", "3CM")
    m2_a = st.number_input("Total M² (Aplicação)", step=0.01, key="m2_a")

    col_b1, col_b2 = st.columns(2)
    
    if col_b1.button("💾 GERAR E SALVAR"):
        texto_relatorio = f"RELATÓRIO DIÁRIO\n\nDATA: {data_obra.strftime('%d.%m.%Y')}\nOBRA: {obra.upper()}\nCLIMA: {clima}\n\n---\nEQUIPE DE APOIO\n"
        for i, func in enumerate(presenca, 1):
            texto_relatorio += f"\n{i}. {func}"
        
        if check_fresagem:
            texto_relatorio += f"\n\n---\nProdução de Fresagem:\n● {loc_f}\nESPESSURA {esp_f}\nTOTAL= {m2_f:,.2f}M²"
            
        texto_relatorio += f"\n\n---\nProdução de Aplicação:\n● {loc_a}\n{faixa_a}\nESPESSURA {esp_a}\n\nTOTAL= {m2_a:,.2f}M²\nTONELADAS= {total_ton:,.2f}ton\nVIAGENS: {len(st.session_state.viagens)}"
        
        texto_relatorio += "\n\n---\nEQUIPAMENTOS:"
        for m in frota:
            texto_relatorio += f"\n- {m}"
        
        st.session_state.historico.append({"data": data_obra.strftime('%d/%m/%Y'), "obra": obra, "texto": texto_relatorio})
        st.subheader("✅ Relatório Gerado!")
        st.code(texto_relatorio, language="markdown")

    if col_b2.button("♻️ NOVO DIA (LIMPAR)"):
        resetar_formulario()
