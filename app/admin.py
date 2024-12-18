from django.contrib import admin

# Register your models here.
from app.models.data.models import Author,Publisher,Genre,Book,Review


admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Review)
