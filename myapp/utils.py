
from google import genai
from django.conf import settings
from django.http import StreamingHttpResponse
from .models import Question, Answer, Comment

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

# def ask_llm(question):
#     question = f"{question} Give me a short answer."
#     print("API_KEY: ", settings.API_KEY)
#     client = genai.Client(api_key=settings.API_KEY)
#     client.max_output_tokens = 10
#     def stream_ai_content():
#             answer_text = ""
#             # Generate content using the model
#             response = client.models.generate_content_stream(
#                 model="gemini-2.0-flash", contents=question
#             )

#             # Yield each chunk as it is received
#             for chunk in response:
#                 yield chunk.text
#                 answer_text += chunk.text 

#             question = Question.objects.create(text=question)
#             Answer.objects.create(question=question, text=answer_text)


#         # Create a StreamingHttpResponse to stream the content
#     return StreamingHttpResponse(stream_ai_content(), content_type="text/plain")