import os
from dotenv import load_dotenv
from django.shortcuts import render
from openai import OpenAI
from django.http import JsonResponse
from .models import Chat
from utils.markdown_to_html import markdown_to_html


load_dotenv(
    dotenv_path='secrets/.env',
)

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=os.getenv(
        'OPENAI_API_BASE',
        'https://api.openai.com/v1/'
    ),
)

def index(request):
    """
    The main entry point of the chat interface. Simply renders the index.html template.
    """
    return render(request, 'index.html')


def response(request):
    """
    Handle a POST request from the chat interface, save the message and response in the database
    and return a JSON response with the response.

    If the request is not a POST request, return a JSON response with a 400 status and an error message.
    """
    if request.method == 'POST':
        message = request.POST.get('message', '')

        completion = client.chat.completions.create(
            model=os.getenv('OPENAI_AI_MODEL', 'gpt-4o'),
            messages=[
                {
                "role": "system",
                "content": "Você é um assistente muito útil e inteligente."
                },
                {
                "role": "user",
                "content": message
                }
            ]
        )
        response_raw = completion.choices[0].message.content.strip()
        response = markdown_to_html(response_raw)

        new_chat = Chat(message=message, response=response)
        new_chat.save()
        return JsonResponse({'response': response})

    return JsonResponse({'response': 'Invalid request'}, status=400)
