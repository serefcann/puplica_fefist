import numpy as np
import pandas as pd
import json
import re
import numpy as np
import faiss
from utils.file_utils import load_yokatlas_data
from utils.model_utils import get_sentence_transformer
from utils.process_utils import preprocess
from utils.formatter import format_rag_results
import config
import logging
logging.basicConfig(level=logging.WARNING)


class Retriever:
    def __init__(self):
        self.data = load_yokatlas_data(config.DATA_PATH)
        self.index = faiss.read_index(config.INDEX_PATH)
        self.model = get_sentence_transformer()

    def search_rag(self,query, topk=5):
        rag_results = []
        query_emb = self.model.encode([preprocess(query)], convert_to_numpy=True)
        #query_emb = np.array(query_emb, dtype='float32')
        D, I = self.index.search(query_emb, topk)
        for idx in I[0]:
            rag_results.append(self.data[idx])
        logging.info(f"retriever {len(rag_results)} sonuc buldu")
        return rag_results


if __name__ == "__main__":
    retriever = Retriever()
    results = retriever.search_rag("marmara istatistik bölümü istiyorum puanı kaç", topk=5)
    print(results)
    
