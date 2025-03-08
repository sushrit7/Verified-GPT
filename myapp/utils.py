
from google import genai



# import requests
# from decouple import config
# API_KEY = config('LLM_API_KEY')

def ask_llm(question):
    client = genai.Client(api_key="")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=question
    )
    return(response.text)
