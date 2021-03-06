from django import forms
from webapp.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'email', 'description')
