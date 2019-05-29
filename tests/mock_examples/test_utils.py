from fakes_example.fakes import FakeCategoryRepository
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
        # This should be rewrite its not valid to create connection object
        cat_repo = CategoryRepository()
        fill_categories(cat_repo, categories)
        print(mock_category)
        self.assertEqual(mock_category.call_count, 1)

    @patch('repositories.CategoryRepository.get_category_by_name', side_effect=[1, 2, 3])
    def test_get_category_by_name(self, mock_get_category):
        category = {
            'category_name': "Python2.7",
            'description': "Old version"
        }
        # If you want to see one return every time you call method
        # mock_get_category.return_value = category

        # If you want preferable returns
        # mock_get_category.side_effect = [category, category, 2]

        cat_repo = CategoryRepository()
        category = cat_repo.get_category_by_name("Python2.7")
        print(category)
        self.assertTrue(mock_get_category.called)


if __name__ == "__main__":
    unittest.main()
