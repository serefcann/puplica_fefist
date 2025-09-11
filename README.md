# puplica_fefist
# Gemini API Kullanımı İçin Adımlar

Bu bölüm, Gemini API’yi kullanmak için gereken adımları açıklamaktadır.

---

## 1. `.env` Dosyası Oluştur

- Proje dizinine `.env` adında bir dosya ekleyin.  
- Bu dosya, gizli API anahtarınızı saklamak için kullanılır.

---

## 2. Google’dan API Key Al

1. [Google Cloud Console](https://console.cloud.google.com/) üzerinden bir proje oluşturun.  
2. Gemini API (GenAI) için API Key oluşturun.  
3. Bu API Key’i `.env` dosyasına ekleyin:

```env
GOOGLE_API_KEY=your_api_key_here
```
## 3. Gemini Client’ta API Key’i Kullan

Python kodunda `dotenv` ile `.env` dosyasını yükleyin:

```python
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()  # .env yüklenir
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)
```
## 4. Gemini API ile Sorgu Yap

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Where is Marmara University?"
)
print(response.text)
```
