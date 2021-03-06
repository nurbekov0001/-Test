from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.models import Book, STATUS_CHOICES
from webapp.forms import BookForm, BookDeleteForm


def index_view(request):
    books = Book.objects.all().filter(status="active").order_by("-created_at")
    return render(request, 'index.html', context={'books': books})


def book_create_view(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, 'book_create.html', {'stat': STATUS_CHOICES})
    elif request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = Book.objects.create(
                name=form.cleaned_data.get("name"),
                email=form.cleaned_data.get("email"),
                description=form.cleaned_data.get("description"),
            )

            return redirect('book_list')
        return render(request, 'book_create.html', context={'form': form})


def book_update_view(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == 'GET':

        form = BookForm(initial={
            'name': book.name,
            'email': book.email,
            'description': book.description,
        })
        return render(request, 'book_update.html', context={'form': form, 'book': book})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.name = form.cleaned_data.get("name")
            book.email = form.cleaned_data.get("email")
            book.description = form.cleaned_data.get("description")
            book.save()
            return redirect('book_list')
        return render(request, 'book_update.html', context={'form': form, 'book': book})


def book_delete_view(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'GET':
        form = BookDeleteForm()
        return render(request, 'book_delete.html', context={'book': book, 'form': form})
    elif request.method == 'POST':
        form = BookDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['name'] != book.name:
                form.errors['name'] = ['Названия статей не совпадают']
                return render(request, 'book_delete.html', context={'book': book, 'form': form})
            book.delete()
            return redirect('book_list')
        return render(request, 'book_delete.html', context={'book': book, 'form': form})

