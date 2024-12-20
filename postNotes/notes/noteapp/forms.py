from django import forms
from django.forms import ModelForm
from .models import Tag, Note 
from django.forms import CharField, TextInput


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']

class NoteForm(ModelForm):

    name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Note
        fields = ['name', 'description']
        exclude = ['tags']
        
Note.objects.create(name='Example Note', description='This is a description of the example note.', done=False, user_id=1)
