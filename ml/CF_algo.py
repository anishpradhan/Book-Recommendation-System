import pandas as pd
import joblib
import os

BASE_DIR1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

filename = os.path.join(BASE_DIR1, 'ml/item_similarity.joblib')
filename2 = os.path.join(BASE_DIR1, 'ml/test_rating.joblib')
books_path = os.path.join(BASE_DIR1, 'ml/books.joblib')
pivot = joblib.load(filename)
ratings = joblib.load(filename2)
books = joblib.load(books_path)


class ItemBased:
    def __init__(self):
        self.itembased = pivot

    def get_similar_items(self, item_id, test_rating):
        similar_score = pivot[item_id] * (test_rating - 2.5)
        similar_score = similar_score.sort_values(ascending=False)
        return similar_score

    def get_book_title(self, isbn):
        title = books.loc[books.ISBN == isbn, 'bookTitle']
        return title.values[0]

    def similar_items(self, book_lover):
        similar_items = pd.DataFrame()
        rated_item = []
        for item, rating in book_lover:
            rated_item.append(item)
            similar_items = similar_items.append(self.get_similar_items(item, rating), ignore_index=True)

        recommended = similar_items.sum().sort_values(ascending=False)

        rec_10 = []
        for i in recommended[:20].index:
            if i in rated_item:
                continue
            else:
                rec_10.append(i)
        count = 20
        while len(rec_10) < 20:
            rec_10.append(recommended.index[count])
            count += 1
        return rec_10
