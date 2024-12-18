from django.db import models
from app.models.data.base import DataRoot

class Author(DataRoot):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Publisher(DataRoot):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Genre(DataRoot):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(DataRoot):
    LANGUAGES = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('zh', 'Chinese'),
        ('fs', 'Farsi'),
    ]

    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Review(DataRoot):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=1)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title} by {self.reviewer_name}"