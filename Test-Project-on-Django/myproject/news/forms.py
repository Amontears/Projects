from django.forms import ModelForm, TextInput, DateTimeInput, FileInput, Textarea
from .models import Articles

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'text', 'image', 'date']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Text'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload Image'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date: YYYY-MM-DD'}),
        }
