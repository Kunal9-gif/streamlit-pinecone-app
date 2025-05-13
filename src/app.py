import streamlit as st
import json
from retriever import retriever

st.title("🔍 Pinecone + Streamlit App")

with open("data/sample.json", "r") as f:
    data = json.load(f)

st.write("✅ Loaded Data:", data)

st.write("📦 Pinecone Index Stats:", retriever.describe_index_stats())