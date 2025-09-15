from utils.file_utils import load_yokatlas_data
from utils.model_utils import get_sentence_transformer
from utils.formatter import format_rag_results
from gemini import Gemini
import faiss
from google.genai import types
import config
from rag import Retriever

gemini = Gemini()
retriever = Retriever()

def yokatlas_bot(data, index, model, gemini_client):
    chat_history = []

    # Konuşma döngüsü başlar
    while True:
        # Kullanıcıdan girdi al
        user_input = input("Sormak istediğiniz bir şey var mı? (Çıkmak için 'dur' yazın) >> ")
        if user_input.lower() in ["dur", "çıkış", "iptal"]:
            print("Görüşmek üzere!")
            break 
        
        rag_results = retriever.search_rag(user_input, topk=20) 
        prompt = create_yokatlas_prompt(rag_results=rag_results, user_input=user_input)

        chat_history.append(types.Content(role='user', parts=[types.Part(text=prompt)]))
        
        try:
            model_response = gemini.ask_gemini(contents=chat_history)
            chat_history.append(types.Content(role="model", parts=[types.Part(text=model_response)]))
            print(f"Bot: {model_response}")

        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            
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

def yokatlas_bot_2(retriever, gemini, starter_prompt):
    gemini.start_chat(starter_prompt)
    
    while True:
        user_input = input("Sormak istediğiniz bir şey var mı? (Çıkmak için 'dur' yazın) >> ")
        if user_input.lower() in ["dur", "çıkış", "iptal"]:
            print("Görüşmek üzere!")
            break 

        # RAG ile ilgili veriyi al
        rag_results = retriever.search_rag(user_input, topk=100) 
        prompt = create_yokatlas_prompt(rag_results, user_input)
        print(prompt)
        
        try:
            gemini.ask(prompt)

        except Exception as e:
            print(f"Bir hata oluştu: {e}")


if __name__ == '__main__':
    retriever = Retriever()
    gemini = Gemini()
    #yokatlas_bot(data, index, model, gemini_client)
    yokatlas_bot_2(retriever, gemini, starter_prompt)



