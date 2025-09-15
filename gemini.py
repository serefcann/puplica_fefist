from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from os.path import join, dirname

class Gemini:
    def __init__(self):         
        dotenv_path = join(dirname(__file__), ".env")
        load_dotenv(dotenv_path)
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        if self.gemini_api_key is None:
            raise ValueError("API key not found! Check your .env file.")
        self.client = genai.Client(api_key = self.gemini_api_key)
        
        self.chat = self.client.chats.create(model="gemini-2.5-flash")
        
    def start_chat(self, starter_prompt):
        self.chat.send_message(starter_prompt)
        
    def ask(self, prompt):
        response = self.chat.send_message(prompt)
        print(f"Bot: {response.text}")

    def ask_gemini(self, contents: list, model = "gemini-2.5-flash"):
        response = self.client.models.generate_content(
            model = model,
            contents = contents,
            config = types.GenerateContentConfig(
                system_instruction="Sen, YÖK Atlas verileri ile donatılmış bir rehbersin. "
                                "Kullanıcı sorularına yalnızca sağlanan verilerle cevap ver."
            )
        )
        return response.text

    
if __name__ == "__main__":
    gemini = Gemini()

    gemini.ask_gemini(prompt='istatistik ')
    

