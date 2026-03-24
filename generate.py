import anthropic
import chromadb
import os
from sentence_transformers import SentenceTransformer

question = input("Enter your question: ")

model = SentenceTransformer('all-MiniLM-L6-v2')
embedded = model.encode(question)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
folder_name = "Athena"
athena_path = os.path.join(desktop_path, folder_name)

client = chromadb.PersistentClient(path=athena_path)
collection = client.get_or_create_collection(name="athena")
chroma_results = collection.query(query_embeddings=embedded, n_results=5)
documents_list = (chroma_results["documents"][0])
prompt = f"Context:\n{' '.join(documents_list)}\n\nQuestion:\n{question}"

client_ai = anthropic.Anthropic()
response = client_ai.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": prompt}
    ]
)
print(response.content[0].text)