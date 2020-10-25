from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from books.api.serializers import BookSerializer, UserRatingSerializer
from books.models import Book, UserRating


# Book API VIEW for specific Item | Working Fine
@api_view(['GET', 'PUT', 'DELETE'])
def api_book_detail_view(request, item_id):
    try:
        book = Book.objects.get(pk=item_id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BookSerializer(Book, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update Successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        operation = Book.delete()
        data = {}
        if operation:
            data["success"] = "Delete Successful"
        else:
            data["success"] = "Delete Failed"
        return Response(data=data)


# Working Fine
@api_view(['POST'])
def api_book_post_view(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Working Fine
@api_view(['GET'])
def api_book_get_view(request):
    if request.method == 'GET':
            book = Book.objects.all()
            serializer = BookSerializer(book, many=True)
            return Response(data=serializer.data)


# USER RATINGS VIEW
# Working Fine
@api_view(['POST'])
def api_rating_post(request):
    if request.method == 'POST':
        serializer = UserRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Working Fine
@api_view(['GET', 'PUT', "DELETE"])
def api_ratings_id(request, item_id):
    try:
        ratings = UserRating.objects.get(pk=item_id)
    except UserRating.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserRatingSerializer(ratings)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UserRatingSerializer(ratings, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update Successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        if request.method == "DELETE":
            operation = ratings.delete()
            data = {}
            if operation:
                data["success"] = "Delete Successful"
            else:
                data["success"] = "Delete Failed"
            return Response(data=data)

# Working Fine
@api_view(['GET'])
def api_ratings_get(request):
    if request.method == 'GET':
            ratings = UserRating.objects.all()
            serializer = UserRatingSerializer(ratings, many=True)
            return Response(data=serializer.data)
