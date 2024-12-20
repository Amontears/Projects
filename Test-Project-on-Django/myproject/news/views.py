# news/views.py
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.utils import translation
from django.views.generic import DeleteView, UpdateView

def news_home(request):
    news = Articles.objects.order_by('-date')  
    return render(request, 'news/news_home.html', {'news': news})  

class NewsDetailView(DeleteView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    with translation.override('en'):
        if request.method == 'POST':
            form = ArticlesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                error = 'Form is not valid'

    form = ArticlesForm()
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'news/create.html', data)
