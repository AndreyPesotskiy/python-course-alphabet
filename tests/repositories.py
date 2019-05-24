import psycopg2
from psycopg2.extras import RealDictCursor

from config import DATABASE


class CategoryRepository:

    def __init__(self):
        self.__con = psycopg2.connect(**DATABASE)

    def add_category(self, category_name, description):
        with self.__con.cursor() as cursor:
            cursor.execute(
                "INSERT INTO categories (categoryname, description) values (%(category_name)s, %(description)s)",
                {
                    'category_name': category_name,
                    'description': description
                }
            )
        self.__con.commit()

    def get_category_by_name(self, category_name):
        with self.__con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM categories where categoryname = %(category_name)s",
                           {"category_name": category_name})
            res = cursor.fetchone()
            return dict(res) if res else res


if __name__ == "__main__":
    catRepo = CategoryRepository()
    catRepo.add_category("Python", "For python")

    category = catRepo.get_category_by_name("Python")
    print(category)
