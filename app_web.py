"""
Remédio na Hora Certa — versão web (Streamlit)
Deploy: Streamlit Community Cloud
"""
import streamlit as st
from src.models import Medicamento
from src.drug_info import buscar_info_medicamento

st.set_page_config(
    page_title="Remédio na Hora Certa",
    page_icon="💊",
    layout="centered",
)

# ── Estado da sessão ──────────────────────────────────────────────────────────

if "medicamentos" not in st.session_state:
    st.session_state.medicamentos = []


def adicionar(nome: str, horario: str):
    st.session_state.medicamentos.append(Medicamento(nome, horario))


def marcar_tomado(idx: int):
    st.session_state.medicamentos[idx].tomado = True


def remover(idx: int):
    st.session_state.medicamentos.pop(idx)


# ── Cabeçalho ─────────────────────────────────────────────────────────────────

st.title("💊 Remédio na Hora Certa")
st.caption("Sistema de apoio para idosos e cuidadores")
st.divider()

# ── Abas ──────────────────────────────────────────────────────────────────────

aba_lista, aba_adicionar, aba_busca = st.tabs([
    "📋 Meus Medicamentos",
    "➕ Adicionar",
    "🔍 Buscar Informações (API)",
])

# ── Aba 1: Lista ──────────────────────────────────────────────────────────────

with aba_lista:
    meds = st.session_state.medicamentos
    if not meds:
        st.info("Nenhum medicamento cadastrado ainda. Use a aba **Adicionar**!")
    else:
        for idx, med in enumerate(meds):
            col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
            with col1:
                st.write(f"**{med.nome}**")
            with col2:
                st.write(f"🕐 {med.horario}")
            with col3:
                if med.tomado:
                    st.success("✓ Tomado")
                else:
                    st.warning("⏳ Pendente")
            with col4:
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if not med.tomado:
                        if st.button("✓", key=f"tomar_{idx}", help="Marcar como tomado"):
                            marcar_tomado(idx)
                            st.rerun()
                with col_btn2:
                    if st.button("🗑", key=f"remover_{idx}", help="Remover"):
                        remover(idx)
                        st.rerun()

# ── Aba 2: Adicionar ──────────────────────────────────────────────────────────

with aba_adicionar:
    st.subheader("Novo Medicamento")
    with st.form("form_adicionar"):
        nome = st.text_input("Nome do remédio", placeholder="Ex: Paracetamol")
        horario = st.text_input("Horário", placeholder="Ex: 08:00")
        submitted = st.form_submit_button("Adicionar 💊", type="primary")

    if submitted:
        if nome and horario:
            adicionar(nome, horario)
            st.success(f"✅ '{nome}' adicionado com sucesso!")
            st.rerun()
        else:
            st.error("Preencha o nome e o horário.")

# ── Aba 3: Busca via API ──────────────────────────────────────────────────────

with aba_busca:
    st.subheader("Buscar Informações do Medicamento")
    st.caption("Consulta a API pública **OpenFDA** em tempo real.")

    nome_busca = st.text_input(
        "Nome do medicamento",
        placeholder="Ex: paracetamol, ibuprofen, amoxicillin",
    )

    if st.button("🔍 Buscar", type="primary"):
        if not nome_busca:
            st.warning("Digite o nome do medicamento.")
        else:
            with st.spinner("Consultando API OpenFDA..."):
                info = buscar_info_medicamento(nome_busca)

            if info is None:
                st.warning(
                    "Nenhuma informação encontrada. "
                    "Tente o nome genérico em inglês (ex: paracetamol, ibuprofen)."
                )
            else:
                st.success("Informações encontradas!")
                st.markdown(f"**Nome Genérico:** {info['nome_generico']}")
                st.markdown(f"**Fabricante:** {info['fabricante']}")
                st.markdown(f"**Finalidade:** {info['finalidade']}")
                st.markdown(f"**Advertências:** {info['advertencias']}")
                st.caption("Fonte: OpenFDA — dados públicos do governo dos EUA (api.fda.gov)")

st.divider()
st.caption("Remédio na Hora Certa v2.0 · Arthur Amaral dos Santos")
