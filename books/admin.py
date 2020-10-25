from django.contrib import admin
from .models import Book, UserRating


class BookDetail(admin.ModelAdmin):
    list_display = ('bookTitle', 'bookAuthor')
    search_fields = ('bookTitle', 'bookAuthor', 'ISBN')


class UserRatingDetail(admin.ModelAdmin):
    list_display = ['user', 'book', 'rating']
    search_fields = ('user__username', 'book__bookTitle')

    def save_model(self, request, obj, form, change):
        user = request.user
        instance = form.save(commit=False)
        # if not change or not instance.created_by:
        #     instance.created_by = user
        # instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(Book, BookDetail)
admin.site.register(UserRating, UserRatingDetail)
