import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import json
import faiss
from sentence_transformers import SentenceTransformer

with open(r'C:\Users\şerefcanmemiş\Documents\projects_2\puplica\yokatlas_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

documents = [
    ' | '.join(f'{k}: {v if v.strip() != "" else "null"}' for k, v in item.items())
for item in data
]

model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v2')
print('model yuklendi ...')
embeddings = model.encode(documents, convert_to_numpy=True, batch_size=64, num_workers=4, show_progress_bar=True)
print('embedding kuruldu...')
print("Embedding shape:", embeddings.shape)  # (n_samples, 512)

dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

faiss.write_index(index, "yokatlas_index.faiss")

