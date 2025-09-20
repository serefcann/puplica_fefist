from contextlib import asynccontextmanager, contextmanager
from utils.file_utils import load_yokatlas_data 
from utils.model_utils import get_sentence_transformer
from gemini import Gemini
import faiss
from google.genai import types
import config
from rag import Retriever
from fastapi import FastAPI, HTTPException, Request
import logging
import uvicorn
from pydantic import BaseModel
from utils.input_utils import question_isproper, question_isspam, create_yokatlas_prompt, starter_prompt, user_last_queries

from fastapi.middleware.cors import CORSMiddleware
logging.basicConfig(level=logging.INFO)


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
# allow React (http://localhost:5173 by default with Vite)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def anasayfa():
    return {
        "message":"YÖK Atlas RAG Bot API Çalışıyor",
        "endpoints":{
            "POST /ask":"Soru sorup yanıt almak için kullanılır"
        }
    }

#ALLOWED_IPS = ["192.168.1.5", "123.45.67.89", "127.0.0.1"]
@app.post("/ask")
async def yokatlas_bot(question_request: QuestionRequest, fastapi_request: Request): 
    user_id = fastapi_request.client.host
    print(user_id)
    #if user_id not in ALLOWED_IPS:
    #    raise HTTPException(status_code=403, detail="Bu IP erişemez")
    
    question = question_request.question.strip()
    question_isproper(question=question, MAX_LEN=200)
    question_isspam(user_id=user_id, WINDOW=60, LIMIT=6)
    
    try:
        rag_results = retriever.hybrid_search(question, topk = 300, return_k = 50)
        print(rag_results)
        prompt = create_yokatlas_prompt(rag_results, question)
        answer = gemini.ask(prompt)
        print(answer)
        return {"question":question, "answer":answer}
    except Exception as e:
        logging.error(f"HATA {e}")
        raise HTTPException(status_code=500, detail="Bot yanıt verirken hata oluştu!")


if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)



