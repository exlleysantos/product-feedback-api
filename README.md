# Product Feedback API

Uma API RESTful construída com **FastAPI** que permite aos usuários enviarem feedbacks sobre produtos. Esses feedbacks são armazenados, analisados com uma avaliação básica de sentimento (a definir), categorizados e podem ser consultados de forma inteligente por tipo, produto e data.

## ✨ Funcionalidades

- 📩 Recebimento de feedbacks de usuários sobre produtos
- 💾 Armazenamento estruturado dos feedbacks no Supabase
- 😊 Processamento e análise básica de sentimento (em definição)
- 🗂️ Categorização automática de feedbacks
- 🔎 Consulta e busca inteligente por:
  - Tipo de feedback
  - Produto relacionado
  - Data de envio

## 🚀 Tecnologias Utilizadas

- **FastAPI** para construção da API
- **Supabase** como backend de banco de dados
- Ferramentas de NLP para análise de sentimento (a definir)
- **Docker** para futura containerização
- **Pytest** para testes automatizados

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/exlleysantos/product-feedback-api.git
cd product-feedback-api

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
uvicorn app.main:app --reload
