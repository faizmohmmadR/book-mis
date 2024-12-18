# app/forms.py

from django import forms
from app.models.data.models import Author, Publisher, Genre, Book, Review

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (optional)'}),
        }

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'website']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Publisher Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website URL'}),
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre Name'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'published_date', 'isbn', 'page_count', 'cover_image', 'language', 'genres']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'publisher': forms.Select(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN Number'}),
            'page_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Pages'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating', 'comment']
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'reviewer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }