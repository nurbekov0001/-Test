from django import forms
from webapp.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'email', 'description')


class BookDeleteForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Введите имя, чтобы удалить её')
