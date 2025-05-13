import os
from pinecone import Pinecone, ServerlessSpec

api_key = os.getenv("PINECONE_API_KEY")

if not api_key:
    raise ValueError("PINECONE_API_KEY environment variable is not set.")

pc = Pinecone(api_key=api_key)

index_name = "my-index"  # ✅ valid name with hyphen

if index_name not in pc.list_indexes().get("indexes", []):
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="euclidean",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

retriever = pc.Index(index_name)
