import time
from fastapi import HTTPException
from utils.formatter import format_rag_results
user_last_queries = {}

def question_isspam(user_id, WINDOW: int, LIMIT: int):
    user_id = "ip"
    now = time.time()
    history = user_last_queries.get(user_id, [])

    history = [t for t in history if now - t < WINDOW]

    history.append(now)
    user_last_queries[user_id] = history
    user_last_queries
    if len(user_last_queries.get(user_id, [])) > LIMIT:
        raise HTTPException(status_code=429, detail="Çok fazla istek, lütfen biraz bekleyin")

def question_isproper(question: str, MAX_LEN: int):
    if not question:
        raise HTTPException(status_code=500, detail='Soru boş olamaz')
    
    if len(question) > MAX_LEN:
        raise HTTPException(status_code=400, detail=f"Soru çok uzun (max {MAX_LEN} karakter)!")
    
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