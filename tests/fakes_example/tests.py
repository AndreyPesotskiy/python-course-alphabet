import unittest

from fakes_example.fakes import FakeCategoryRepository
from fakes_example.main import fill_categories


class TestCategoriesInterfaceWithFakes(unittest.TestCase):

    def setUp(self) -> None:
        self.cat_repo = FakeCategoryRepository()

    def test_fill_categories(self):
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
        fill_categories(self.cat_repo, categories)
        self.assertEqual(len(self.cat_repo.records), 1)

        category = self.cat_repo.records[0]

        self.assertIn(categories[0]['category_name'], category.values())


if __name__ == "__main__":
    unittest.main()
