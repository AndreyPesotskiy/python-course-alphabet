from repositories import CategoryRepository
from utils import fill_categories

if __name__ == "__main__":
    categories = [
        {
            'category_name': "Python2.7",
            'description': "Old version"
        },
        {
            'category_name': "Py",
            'description': "Some bad data"
        },
    ]
    cat_repo = CategoryRepository()
    fill_categories(cat_repo, categories)

