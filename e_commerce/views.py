from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    context = {
        "title": "Página principal"
        "Content": "Bem-vindo a página principal"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Página sobre"
        "Content": "Bem-vindo a página sobre"
    }
    return render(request, "about_page.html", context)

def contact_page(request):
    context = {
        "title": "Página contato"
        "Content": "Bem-vindo a página de contato"
    }
    return render(request, "contact_page.html", context)