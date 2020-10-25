import django
import joblib
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BRS.settings')
django.setup()


def correlation():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    test_rating_path = os.path.join(BASE_DIR, 'ml/test_rating.joblib')
    test_rating = joblib.load(test_rating_path)
    print("This may take a few minute...Please wait...")
    item_similarity_df = test_rating.corr(method='pearson')
    print("Finished creating correlation")
    print("Creating joblib file")
    joblib.dump(item_similarity_df, "ml/item_similarity.joblib", compress=True)
    print("Finished Creating joblib file...")


if __name__ == '__main__':
    print("Starting correlation script...")
    correlation()
    print("Completed")
