from django.db import models
from account.models import Account
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(max_length=10, unique=True)
    bookTitle = models.CharField(max_length=100)
    bookAuthor = models.CharField(max_length=50)
    yearOfPublication = models.PositiveIntegerField()
    publisher = models.CharField(max_length=70)
    imageUrlS = models.URLField(blank=True)
    imageUrlM = models.URLField(blank=True)
    imageUrlL = models.URLField(blank=True)

    def __str__(self):
        return self.bookTitle + ", " + self.bookAuthor


class UserRating(models.Model):
    user = models.ForeignKey(Account, default=1, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=2000)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        unique_together = (('user', 'book'),)
        index_together = (('user', 'book'),)

    def __str__(self):
        return f'[{self.user},{self.rating}], {self.book}'
