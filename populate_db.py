import django
import joblib
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BRS.settings')
django.setup()

from books.models import Book


def delete_db():
    print('truncate db')
    books_count = Book.objects.all().count()
    if books_count >= 1:
        Book.objects.all().delete()
    print('finished truncate db')


def populate():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    books_path = os.path.join(BASE_DIR, 'ml/books.joblib')
    books = joblib.load(books_path)
    print("Populating Database. Please Wait...")
    for row in books.head(6668).itertuples():
        objs = [
            Book(
                ISBN=row[1],
                bookTitle=row[2],
                bookAuthor=row[3],
                yearOfPublication=row[4],
                publisher=row[5],
                imageUrlS=row[6],
                imageUrlM=row[7],
                imageUrlL=row[8],
            )
        ]
        Book.objects.bulk_create(objs)


if __name__ == '__main__':
    print("Starting Database Populating Script...")
    delete_db()
    populate()
    print("Finished Populating Database.")
