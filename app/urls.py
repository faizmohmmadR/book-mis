from django.urls import path
from app.views.data import author,publisher,book,review

urlpatterns = [
    # Author URLs
    path('authors/', author.author_list, name='author_list'),
    path('authors/create/', author.author_create, name='author_create'),
    path('authors/update/<int:pk>/', author.author_update, name='author_update'),
    path('authors/delete/<int:pk>/', author.author_delete, name='author_delete'),

    # Publisher URLs
    path('publishers/', publisher.publisher_list, name='publisher_list'),
    path('publishers/create/', publisher.publisher_create, name='publisher_create'),
    path('publishers/update/<int:pk>/', publisher.publisher_update, name='publisher_update'),
    path('publishers/delete/<int:pk>/', publisher.publisher_delete, name='publisher_delete'),

    # Genre URLs
    path('genres/', book.genre_list, name='genre_list'),
    path('genres/create/', book.genre_create, name='genre_create'),
    path('genres/update/<int:pk>/', book.genre_update, name='genre_update'),
    path('genres/delete/<int:pk>/', book.genre_delete, name='genre_delete'),

    # Book URLs
    path('books/', book.book_list, name='book_list'),
    path('books/create/', book.book_create, name='book_create'),
    path('books/update/<int:pk>/', book.book_update, name='book_update'),
    path('books/delete/<int:pk>/', book.book_delete, name='book_delete'),

    # Review URLs
    path('reviews/', review.review_list, name='review_list'),
    path('reviews/create/', review.review_create, name='review_create'),
    path('reviews/update/<int:pk>/', review.review_update, name='review_update'),
    path('reviews/delete/<int:pk>/', review.review_delete, name='review_delete'),
]