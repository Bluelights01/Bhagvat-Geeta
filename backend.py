# --- PATCH for ChromaDB and SQLite3 ---
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# --- Regular imports after patch ---
import chromadb
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import os

# --- ChromaDB persistent client ---
client = chromadb.PersistentClient(path="app1")

# --- Gemini client setup ---
# Set your Gemini API key properly
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Now use genai client without passing the key to Client()
gemini_client = genai

def promptans(prompt):
    res = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return res

# --- Setup ChromaDB collection ---
client.list_collections()
collection = client.get_or_create_collection("geeta_collection")

# --- Load SentenceTransformer model ---
model = SentenceTransformer("all-MpNet-Base-v2")

def getans(text):
    embed = model.encode([text])
    res = collection.query(
        query_embeddings=embed,
        n_results=1
    )
    return res
