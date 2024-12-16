from django import forms
from app.models.data.models import Author, Publisher, Genre, Book, Review

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'website']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'published_date', 'isbn', 'page_count', 'cover_image', 'language', 'genres']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating', 'comment']