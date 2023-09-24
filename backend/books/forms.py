from django import forms
from books.models import Books_catlog

class add_book_form(forms.ModelForm):
    class Meta:
        model = Books_catlog
        fields = ['title', 'author', 'genere', 'avialable_free', 'avialable_paid','description', 'additional']