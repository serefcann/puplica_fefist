from functools import lru_cache
from sentence_transformers import SentenceTransformer

@lru_cache(maxsize=1)
def get_sentence_transformer():
    """SentenceTransformer modelini cache'leyerek yükler."""
    return SentenceTransformer("sentence-transformers/distiluse-base-multilingual-cased-v2")