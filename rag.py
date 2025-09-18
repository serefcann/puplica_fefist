import numpy as np
import pandas as pd
import json
import re
import numpy as np
import faiss
from utils.file_utils import load_yokatlas_data
from utils.model_utils import get_sentence_transformer
from utils.process_utils import preprocess
from utils.formatter import format_rag_results, normalize_university, clean_query
from constants.universities import university_abbrevations
import config
import logging
from rapidfuzz import process, fuzz

logging.basicConfig(level=logging.WARNING)


class Retriever:
    def __init__(self):
        self.data = load_yokatlas_data(config.DATA_PATH)
        self.index = faiss.read_index(config.INDEX_PATH)
        self.model = get_sentence_transformer()

    def search_rag(self, query, topk=5):
        rag_results = []
        query_processed = preprocess(query)
        query_processed = normalize_university(query_processed, university_abbrevations)
        query_processed = clean_query(query_processed)
        print(query_processed)
        query_emb = self.model.encode([query_processed], convert_to_numpy=True)
        #query_emb = np.array(query_emb, dtype='float32')
        D, I = self.index.search(query_emb, topk)
        for idx in I[0]:
            rag_results.append(self.data[idx])
        logging.info(f"retriever {len(rag_results)} sonuc buldu")
        return rag_results
    
    def hybrid_search(self, query, topk, return_k):
        candidates = self.search_rag(query, topk=topk)
        query_processed = preprocess(query)
        query_processed = normalize_university(query_processed, university_abbrevations)
        query_processed = clean_query(query_processed)
        STOPWORDS = {"ve", "ile", "için", "bir", "bu", "istiyorum", "kaç", "bölümü"}
        keywords = [w for w in query_processed.split() 
                    if w not in STOPWORDS]
        
        scored_results = []
        
        for c in candidates:
            text = (c.get("Üniversite", "") + " " + c.get("Bölüm Adı", "")).lower()
            
            # tüm anahtar kelimeleri kontrol et
            score_list = [fuzz.partial_ratio(k, text) for k in keywords]
            avg_score = sum(score_list) / len(score_list) if score_list else 0
            
            scored_results.append((c, avg_score))
        
        scored_results.sort(key=lambda x: x[1], reverse=True)
        return [c for c, score in scored_results[:return_k]]


if __name__ == "__main__":
    retriever = Retriever()
    #results = retriever.search_rag("marmara istatistik bölümü istiyorum puanı kaç", topk=5)
    results = retriever.hybrid_search("marmara istatistik bölümü istiyorum puanı kaç")
    print(results)
    
