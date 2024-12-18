from django.shortcuts import render, redirect, get_object_or_404
from app.models.data.models import Author, Publisher, Genre, Book, Review
from app.forms.forms import AuthorForm, PublisherForm, GenreForm, BookForm, ReviewForm



# Genre Views
def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'app/genre/genre_list.html', {'genres': genres})

def genre_create(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm()
    return render(request, 'app/genre/genre_form.html', {'form': form})

def genre_update(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'app/genre/genre_form.html', {'form': form})

def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        genre.delete()
        return redirect('genre_list')
    return render(request, 'app/genre/genre_confirm_delete.html', {'genre': genre})

# Book Views
def book_list(request):
    books = Book.objects.all()
    return render(request, 'app/book/book_list.html', {'books': books})



def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            print(form.errors)  # Debugging line to see any validation errors
    else:
        form = BookForm()
    
    return render(request, 'app/book/book_form.html', {'form': form})

    
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'app/book/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'app/book/book_confirm_delete.html', {'book': book})
