Some useful commands


# Create an empty data migration file:
  python manage.py makemigrations article --empty  (article - is a name of app)

# Example for the management command here: "mysite/article/management/commands/update_article_titles.py"

  python manage.py update_article_titles 1 (where 1 is article id)