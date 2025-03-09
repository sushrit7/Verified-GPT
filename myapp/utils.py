
from google import genai
from django.conf import settings

# import requests
# from decouple import config


def ask_llm(question):
    question = f"{question} Give me a short answer."
    print("API_KEY: ", settings.API_KEY)
    client = genai.Client(api_key=settings.API_KEY)
    client.max_output_tokens = 10
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=question
    )
    return(response.text)
