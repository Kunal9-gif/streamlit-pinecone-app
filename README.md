# Streamlit + Pinecone Minimal App

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run src/app.py
```

## 🐳 Run with Docker

```bash
docker build -t streamlit-pinecone-app .
docker run --env-file .env -p 8501:8501 streamlit-pinecone-app
```