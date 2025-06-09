import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="QR Code Único", layout="centered")
st.title("🔳 Gerador de QR Code Único com Lista de Seriais")
st.markdown("Cole seriais ou endereços no campo abaixo **e/ou** envie um Excel com uma coluna de dados. Será gerado **um único QR Code** com toda a lista combinada.")

# Estilo personalizado
st.markdown("""
<style>
/* Ocultar menu e rodapé */
#MainMenu, header, footer {
    visibility: hidden;
    height: 0;
}

/* Estilo geral */
.stApp {
    background: linear-gradient(135deg, #B0E0E6, #2a5298, #90EE90);
    background-attachment: fixed;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Títulos */
h1, h2, h3, h4 {
    color: white;
    text-shadow: 1px 1px 5px rgba(0,0,0,0.7);
}

/* Caixas internas */
.css-18e3th9, .css-1d391kg {
    background-color: rgba(255, 255, 255, 0.08) !important;
    border-radius: 12px;
    padding: 16px;
    color: #4F4F4F;
}

/* Campos de entrada */
textarea, input, .stTextInput input, .stTextArea textarea {
    background-color: #f0f0f0 !important;
    color: #333333 !important;
    border-radius: 8px;
    padding: 8px;
    border: 1px solid #cccccc;
}

/* Labels */
label, .stSelectbox label, .stFileUploader label {
    color: white !important;
    font-weight: bold;
}

/* Botões */
.stButton>button {
    background-color: #00a389;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
    transition: background 0.3s ease;
}
.stButton>button:hover {
    background-color: #009077;
    cursor: pointer;
}

/* Botão de download */
.stDownloadButton>button {
    background-color: #1f8eca;
    color: white;
    border-radius: 8px;
    padding: 8px 16px;
}
.stDownloadButton>button:hover {
    background-color: #186fa7;
}

/* Mensagens */
.stAlert, .stSuccess, .stWarning, .stInfo {
    background-color: rgba(255, 255, 255, 0.15) !important;
    border-left: 6px solid #00d1b2;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Função para gerar o QR Code
def gerar_qrcode_unico(texto_total):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=2
    )
    qr.add_data(texto_total)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# Entrada de texto
texto = st.text_area("📜 Texto com serial", height=150)
dados_texto = [linha.strip() for linha in texto.splitlines() if linha.strip()] if texto else []

# Upload de Excel
arquivo = st.file_uploader("📁 Ou envie um arquivo Excel (.xlsx)", type=["xlsx"])
dados_excel = []
if arquivo:
    coluna = st.text_input("Nome da coluna com os dados:", value="serial")
    try:
        df = pd.read_excel(arquivo)
        if coluna in df.columns:
            dados_excel = df[coluna].dropna().astype(str).tolist()
            st.success(f"✅ {len(dados_excel)} registros carregados do Excel.")
        else:
            st.warning("⚠️ Coluna não encontrada na planilha.")
    except Exception as e:
        st.error(f"❌ Erro ao ler o arquivo: {e}")

# Combina os dois
# remove duplicatas mantendo ordem
dados_combinados = list(dict.fromkeys(dados_texto + dados_excel))  

if dados_combinados:
    separador = st.selectbox("Separar os dados dentro do QR Code por:", ["\\n (quebra de linha)", ", (vírgula)", "; (ponto e vírgula)"])
    sep = {"\\n (quebra de linha)": "\n", ", (vírgula)": ",", "; (ponto e vírgula)": ";"}[separador]
    texto_final = sep.join(dados_combinados)

    if st.button("🚀 Gerar QR Code Único"):
        img_buffer = gerar_qrcode_unico(texto_final)
        st.image(img_buffer, caption="✅ QR Code Gerado", width=200)
        st.download_button("📥 Baixar QR Code", data=img_buffer, file_name="qrcode_unico.png", mime="image/png")
else:
    st.info("ℹ️ Insira dados no campo de texto ou envie um arquivo Excel.")
