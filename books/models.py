from django.db import models
from uuid import uuid4

# Create your models here.

class Book(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "book"
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return self.title
