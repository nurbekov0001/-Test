from django import forms
from webapp.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'email', 'description', 'status', 'created_at', 'updated_at')


class BookDeleteForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Введите название задачи, чтобы удалить её')
