from django.contrib import admin

# Register your models here.
from shortener.models import ShortenedURL

admin.site.register(ShortenedURL)