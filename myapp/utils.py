
from google import genai
from django.conf import settings

# import requests
# from decouple import config


def ask_llm(question):
    print("API_KEY: ", settings.API_KEY)
    client = genai.Client(api_key=settings.API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=question
    )
    return(response.text)
