import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import json
import faiss
from sentence_transformers import SentenceTransformer
from utils.model_utils import get_sentence_transformer
import logging
from utils.file_utils import load_yokatlas_data
from utils.process_utils import preprocess
from utils.formatter import short_format
import config
logging.basicConfig(level=logging.WARNING)

class indexBuilder:
    def __init__(self, model_name="model"):
        self.model = get_sentence_transformer()
        self.index = None
        logging.info("Model yüklendi")
        
    def build(self, documents):
        embeddings = self.model.encode(documents, convert_to_numpy=True, batch_size=64, num_workers=4, show_progress_bar=True)
        logging.info('embedding kuruldu...')
        dim = embeddings.shape[1]
        #embeddings = np.array(embeddings, dtype='float32')
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def save(self, download_path=config.INDEX_PATH):
        try:
            faiss.write_index(self.index, download_path)
        except Exception as e:
            logging.error(f"Index kaydedilemedi: {e}")

if __name__ == '__main__':
    data = load_yokatlas_data(config.DATA_PATH)
    documents = short_format(data=data)
    
    builder = indexBuilder()
    builder.build(documents=documents)
    builder.save()