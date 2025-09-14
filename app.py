from utils.file_utils import load_yokatlas_data
from utils.model_utils import get_sentence_transformer
from rag import search_rag
from gemini import load_gemini_client, ask_gemini
import faiss


data = load_yokatlas_data('yokatlas_data/yokatlas_data.json')
index = faiss.read_index('yokatlas_data/yokatlas_index.faiss')
model = get_sentence_transformer()
gemini_client = load_gemini_client()


query = input('yks tercih chatbotu için soru giriniz: ')
rag_results = search_rag(query, model=model, index=index, data = data, topk=5)

prompt = f"""
{rag_results}

Kullanıcının sorusu: '{query}'

Bu bilgilere dayanarak, soruyu en iyi şekilde yanıtla. Eğer bilgi yoksa, "bilgi yok" de. Cevap kısa ve anlaşılır olsun. Sayısal veri istiyorsa elindeki en uygun veriye göre cevapla.
"""

answer = ask_gemini(gemini_client, prompt= prompt)
print(answer)


