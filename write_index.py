import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import json
import faiss
from sentence_transformers import SentenceTransformer
import logging
from utils.model_utils import get_sentence_transformer
logging.basicConfig(level=logging.INFO)


def reformat_json(data):
    documents = [
        ' | '.join(f'{k}: {v if v.strip() != "" else "null"}' for k, v in item.items())
    for item in data
    ]
    return documents

def create_index_sentence_transformer(documents, download_path="yokatlas_index.faiss"):
    model = get_sentence_transformer()
    logging.info("Model yüklendi")
    embeddings = model.encode(documents, convert_to_numpy=True, batch_size=64, num_workers=4, show_progress_bar=True)
    logging.info('embedding kuruldu...')
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    try:
        faiss.write_index(index, download_path)
    except Exception as e:
        logging.error(f"Index kaydedilemedi: {e}")

