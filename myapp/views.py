from django.shortcuts import render, HttpResponse
from .utils import ask_llm

# Create your views here.

def home(request):
    return render(request, "base.html")

def test_view(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        # Process the input (you can modify this logic)
        result = ask_llm(user_input)

    return render(request, 'test.html', {'result': result})

