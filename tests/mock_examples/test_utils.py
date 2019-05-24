from utils import fill_categories
from repositories import CategoryRepository

import unittest
from mock import patch


class TestFillCategoriesWithMock(unittest.TestCase):

    @patch('repositories.CategoryRepository.add_category')
    def test_fill_categories(self, mock_category):
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
        print(mock_category)
        self.assertEqual(mock_category.call_count, 1)


if __name__ == "__main__":
    unittest.main()