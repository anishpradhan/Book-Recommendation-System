from operator import attrgetter

from django.shortcuts import render, redirect, HttpResponse
from .models import Book, UserRating
from ml.CF_algo import ItemBased
from .forms import RatingForm
from django.db.models import Case, Value, When, IntegerField, Q
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from books.api.serializers import BookSerializer, UserRatingSerializer


class BookList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        user = request.user.id
        if user:
            user_rating = UserRating.objects.filter(user_id=user)
            rating_pair = []
            if user_rating:
                for i in user_rating:
                    duo = (i.book.ISBN, i.rating)
                    rating_pair.append(duo)
                item_based = ItemBased()
                books = item_based.similar_items(rating_pair)
                # for filtering the books by preserving its order
                cases = [When(ISBN=isbn, then=Value(i)) for i, isbn in enumerate(books)]
                case = Case(*cases, output_field=IntegerField())
                queryset = Book.objects.filter(ISBN__in=books)
                queryset = queryset.annotate(my_order=case).order_by('my_order')
                item = []
                for i in books:
                    item.append(item_based.get_book_title(i))

                context = {'recommended': queryset, 'rated': user_rating, }
            else:
                context = {'rated': user_rating}
        else:
            context = {}
        return Response(context)


def book_detail(request, item_id):
    book = Book.objects.get(pk=item_id)
    form = RatingForm()
    context = {'book': book, 'form': form}
    return render(request, 'book_detail.html', context)


def rating_form(request, item_id):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = UserRating()
            rating.user = request.user
            rating.rating = form.cleaned_data['rating']
            rating.feedback = form.cleaned_data['feedback']
            rating.book_id = item_id
            rating.save()
            return redirect('home_api')


# Search Query
def get_book_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        books = Book.objects.filter(
            Q(bookTitle__icontains=q) |
            Q(bookAuthor__icontains=q)
        ).distinct()
        for book in books:
            queryset.append(book)

    return list(set(queryset))


def search_area(request):
    query = ""
    if request.method == 'GET':
        query = request.GET.get('q')
    books = sorted(get_book_queryset(query), key=attrgetter('bookTitle'), reverse=True)

    if query == "":
        books = []

    context = {'query': str(query), 'books': books}
    return render(request, 'search.html', context)
