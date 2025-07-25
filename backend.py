import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
import os

client = chromadb.PersistentClient(path="app1")
gemini_client=genai.Client(os.getenv("GEMINI_API_KEY"))

def promptans(prompt):
    res=gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return res
client.list_collections()
collection=client.get_or_create_collection("geeta_collection")
model=SentenceTransformer("all-MpNet-Base-v2")
def getans(text):
    embed=model.encode([text])
    res=collection.query(
    query_embeddings=embed,
    n_results=1
    )
    return res
