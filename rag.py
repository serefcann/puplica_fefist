import numpy as np
import pandas as pd
import json
import re
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

def search_rag(query, model, index, data, topk=5):
    rag_results = []
    query_emb = model.encode([preprocess(query)], convert_to_numpy=True)
    D, I = index.search(query_emb, topk)
    for idx in I[0]:
        rag_results.append(data[idx])
    return rag_results        
if __name__ == "__main__":
    search_rag("marmara istatistik bölümü istiyorum puanı kaç")