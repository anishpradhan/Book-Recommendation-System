from django.urls import path, include
from books.api.views import api_book_detail_view, \
    api_book_post_view, api_rating_post, api_ratings_id, api_book_get_view, api_ratings_get

app_name = 'books'

urlpatterns = [
    path('<item_id>/books', api_book_detail_view, name='get'),
    path('post_book/', api_book_post_view, name='create'),
    path('get_books/', api_book_get_view, name='get'),

    # URL for Ratings
    path('post_rating/', api_rating_post, name='ratings_api'),
    path('get_ratings/', api_ratings_get, name='get_all_ratings'),
    path('<item_id>/ratings', api_ratings_id, name='get_ratings_id'),
    ]
