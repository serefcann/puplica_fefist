import numpy as np
import pandas as pd
import json
import re
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

with open('yokatlas_data.json', 'r',encoding='utf-8') as f:
    data = json.load(f)
print('dokumanlar indirildi ...')

index = faiss.read_index("yokatlas_index.faiss")

def preprocess(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v2')

print('embedding kuruldu...')

query = "Bilgisayar"
query_emb = model.encode([preprocess(query)], convert_to_numpy=True)
D, I = index.search(query_emb, 5)
for idx in I[0]:
    print(data[idx])
