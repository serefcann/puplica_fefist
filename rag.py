import numpy as np
import pandas as pd
import json
import re
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from utils.file_utils import load_yokatlas_data
from utils.model_utils import get_sentence_transformer

def preprocess(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

data = load_yokatlas_data('yokatlas_data\yokatlas_data.json')
print('dokumanlar indirildi ...')

index = faiss.read_index("yokatlas_data\yokatlas_index.faiss")

model = get_sentence_transformer()
print('model yuklendi ...')

def user_query(query):
    query_emb = model.encode([preprocess(query)], convert_to_numpy=True)
    D, I = index.search(query_emb, 5)
    for idx in I[0]:
        print(data[idx])
        
if __name__ == "__main__":
    user_query("marmara istatistik bölümü")