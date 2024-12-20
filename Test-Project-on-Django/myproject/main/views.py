from django.shortcuts import render


data = {
    "title": "Main Page",
}

def index(request):
    return render(request, "main/index.html", data)

def about(request):
    return render(request, "main/about.html")