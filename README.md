# 🔳 Gerador de QR Code Único com Lista de Seriais

Este projeto permite gerar um **único QR Code** contendo uma lista de seriais ou endereços, inseridos manualmente ou importados de uma planilha Excel.
 A aplicação foi construída com [Streamlit](https://streamlit.io/) para garantir simplicidade, leveza e um visual agradável.

Repositório oficial: [BEROMEIRO/Gerador_de_QR_Code](https://github.com/BEROMEIRO/Gerador_de_QR_Code)

---

## 🚀 Funcionalidades

- ✅ Inserção manual de seriais ou textos (um por linha)
- ✅ Upload de planilhas Excel (.xlsx) com coluna de seriais
- ✅ Combinação automática dos dados (sem duplicatas)
- ✅ Escolha de separador entre os dados no QR Code (`\n`, `,`, `;`)
- ✅ Geração de QR Code leve e eficiente
- ✅ Download da imagem gerada (.png)

---

## 🖼️ Visual do App

> ⚙️ O app foi estilizado com CSS embutido para deixar a experiência mais agradável, mantendo o foco na clareza e acessibilidade visual.

---

## 🛠️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/BEROMEIRO/Gerador_de_QR_Code.git
cd Gerador_de_QR_Code

### 2. Crie o venv
python -m venv venv

### 3 Ativação:
# Windows:
venv\\Scripts\\activate

# macOS/Linux:
source venv/bin/activate

### 4 Instale as dependências:
pip install -r requirements.txt

### 5 Execute a aplicação
streamlit run geradorqr.py 

