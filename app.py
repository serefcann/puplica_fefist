from contextlib import asynccontextmanager, contextmanager
from utils.file_utils import load_yokatlas_data 
from utils.model_utils import get_sentence_transformer
from utils.formatter import format_rag_results
from gemini import Gemini
import faiss
from google.genai import types
import config
from rag import Retriever
from fastapi import FastAPI, HTTPException
import logging
import uvicorn
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)


            
starter_prompt = f"""
Sen, YÖK Atlas'tan alınmış güncel üniversite ve bölüm verileri ile donatılmış bir rehbersin.
Görevin, kullanıcının sorusunu, sağlanan RAG verilerini kullanarak detaylı, doğru ve anlaşılır şekilde cevaplamaktır.

Cevabını oluştururken kurallar:
1. Sadece sana sağlanan verileri kullan, tahmin veya ek bilgi ekleme.
2. Eğer soru çok genel ise, önce hangi puan türüne veya üniversiteye göre bilgi istediğini sor.
3. Cevaplarını kısa ve öz tut, gereksiz açıklamalardan kaçın.
4. Sayısal verileri veya sıralamaları varsa, net bir şekilde belirt.
5. Eğer sorunun cevabı verilerde yoksa, sadece "Bu konuda yeterli bilgiye sahip değilim." de.
6. Eğer sayısal değer döndürüyorsan daima sırala.
7. kullanıcı yönlendir. Örneğin merak ettiğin bölüm, üniversite sıralamaları var mı?
8. kullanıcı genel bilgi verirse en düşük sıralamalı olan SAY ve EA bölümlerini önce getir.
9. kullanıcı belirtmedikçe bölümleri veya üniversiteleri getirirken 10'dan fazla getirme genelde.
10. kullanıcı en iyi diyorsa bu sıralaması en düşük olanlar demektir.


Bundan sonra verilecek olan verilere göre cevap ver eğer bilgi eksik ise bilginin devamını iste:
"""

def create_yokatlas_prompt(rag_results: list, user_input: str) -> str:
    """
    user_input: Kullanıcının sorusu
    rag_results: search_rag'tan dönen liste/dict
    """
    formatted_rag = format_rag_results(rag_results)  # daha önce oluşturduğumuz format fonksiyonu
    prompt = f"""
    Aşağıdaki verileri kullanabilirsin:

    {formatted_rag}
    
    Kullanıcının sorusu: "{user_input}"
    """
    return prompt

retriever = None
gemini = None

class QuestionRequest(BaseModel):
    question: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    global retriever, gemini, starter_prompt
    logging.info("Retriever ve Gemini yükleniyor...")
    retriever = Retriever()
    gemini = Gemini()
    gemini.start_chat(starter_prompt)
    logging.info("Hazır!")
    yield
    logging.info("Shutdown işlemleri tamamlandı")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def anasayfa():
    return {
        "message":"YÖK Atlas RAG Bot API Çalışıyor",
        "endpoints":{
            "POST /ask":"Soru sorup yanıt almak için kullanılır"
        }
    }

@app.post("/ask")
async def yokatlas_bot(request: QuestionRequest):
    
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=500, detail='Soru boş olamaz')
    
    # RAG ile ilgili veriyi al
    #rag_results = retriever.search_rag(user_input, topk=100) 
    
    try:
        rag_results = retriever.hybrid_search(question, topk = 250, return_k = 50)
        prompt = create_yokatlas_prompt(rag_results, question)
        answer = gemini.ask(prompt)
        print(answer)
        return {"question":question, "answer":answer}
    except Exception as e:
        logging.error(f"HATA {e}")
        raise HTTPException(status_code=500, detail="Bot yanıt verirken hata oluştu!")


if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)



