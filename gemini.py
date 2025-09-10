from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from os.path import join, dirname

def load_gemini_client():
    dotenv_path = join(dirname(__file__), ".env")
    load_dotenv(dotenv_path)
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if gemini_api_key is None:
        raise ValueError("API key not found! Check your .env file.")
    return genai.Client(api_key = gemini_api_key)


def ask_gemini_stream(client):
    response = client.models.generate_content_stream(
        model = "gemini-2.5-flash",
        contents = "Where is the Marmara University?",
        config = types.GenerateContentConfig(
            system_instruction = "you are a proffessional, marmara university's school assistant"
        )
    )
    for chunk in response:
        print(chunk.text)

def main():
    client = load_gemini_client()
    ask_gemini_stream(client)
    
if __name__ == "__main__":
    main()