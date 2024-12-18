import os
import django

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # Change 'your_project_name' to your actual project name

# Initialize Django
django.setup()

from app.models.data.models import Author, Publisher, Genre, Book, Review
from datetime import date

# Create Authors
authors = [
    Author(first_name='John', last_name='Doe', email='john.doe@example.com'),
    Author(first_name='Jane', last_name='Smith', email='jane.smith@example.com'),
    Author(first_name='Emily', last_name='Johnson', email='emily.johnson@example.com'),
    Author(first_name='Michael', last_name='Brown', email='michael.brown@example.com'),
    Author(first_name='Sarah', last_name='Davis', email='sarah.davis@example.com'),
]

for author in authors:
    author.save()

# Create Publishers
publishers = [
    Publisher(name='Penguin Random House', address='1745 Broadway, New York, NY 10019', website='https://www.penguinrandomhouse.com'),
    Publisher(name='HarperCollins', address='195 Broadway, New York, NY 10007', website='https://www.harpercollins.com'),
    Publisher(name='Simon & Schuster', address='1230 Avenue of the Americas, New York, NY 10020', website='https://www.simonandschuster.com'),
    Publisher(name='Hachette Book Group', address='1290 Avenue of the Americas, New York, NY 10104', website='https://www.hachettebookgroup.com'),
    Publisher(name='Macmillan', address='120 Broadway, New York, NY 10271', website='https://us.macmillan.com'),
]

for publisher in publishers:
    publisher.save()

# Create Genres
genres = [
    Genre(name='Fiction'),
    Genre(name='Non-Fiction'),
    Genre(name='Science Fiction'),
    Genre(name='Fantasy'),
    Genre(name='Mystery'),
]

for genre in genres:
    genre.save()

# Create Books
books = [
    Book(title='The Great Gatsby', 
         publisher=publishers[0], 
         published_date=date(1925, 4, 10), 
         isbn='9780743273565', 
         page_count=180, 
         language='en'),
    
    Book(title='1984', 
         publisher=publishers[1], 
         published_date=date(1949, 6, 8), 
         isbn='9780451524935', 
         page_count=328, 
         language='en'),
    
    Book(title='To Kill a Mockingbird', 
         publisher=publishers[2], 
         published_date=date(1960, 7, 11), 
         isbn='9780060935467', 
         page_count=336, 
         language='en'),
    
    Book(title='The Hobbit', 
         publisher=publishers[3], 
         published_date=date(1937, 9, 21), 
         isbn='9780547928227', 
         page_count=310, 
         language='en'),
    
    Book(title='Murder on the Orient Express', 
         publisher=publishers[4], 
         published_date=date(1934, 1, 1), 
         isbn='9780062693662', 
         page_count=256, 
         language='en'),
]

for book in books:
    book.save()
    book.authors.add(authors[0], authors[1])  # Add first two authors to each book
    book.genres.add(genres[0], genres[2])  # Add Fiction and Science Fiction genres

# Create Reviews
reviews = [
    Review(book=books[0], reviewer_name='Alice', rating=5, comment='A masterpiece of 20th-century literature.'),
    Review(book=books[1], reviewer_name='Bob', rating=4, comment='A chilling depiction of a dystopian future.'),
    Review(book=books[2], reviewer_name='Charlie', rating=5, comment='A profound and moving novel.'),
    Review(book=books[3], reviewer_name='Diana', rating=4, comment='A wonderful adventure story.'),
    Review(book=books[4], reviewer_name='Eve', rating=3, comment='A classic mystery but a bit slow in parts.'),
]

for review in reviews:
    review.save()