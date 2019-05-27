## Jinja2 Homework
Make Top IMDb site from templates.

### Workflow
Pull code to your computer, make new virtual environment with Python3 and install requirements from `requirements.txt`.

To run Flask use this command in command line from the root of the project:
```shell
python run.py
```

Connect `layout.html` as parent template to all other child templates. Make sure that you have navigation bar on every page.

Render proper title inside `<title></title>` tag on every page from views functions in `run.py`.

`home` page is just home parking page with button link to the list of movies. Put your name in the footer.
`movies` page is the page with the main content where you should show all the movies from `movies.json` dataset in a `for` loop and left only movies not older than 2010 year by filtering them with the `if` statement.
`movie` page is the page of concrete movie, when you click on it on the `movies` page.
You should replace all mocked data on `movies` and `movie` pages with data from `movies.json`, this data is already available in the templates, look into views functions in `run.py`.

Make links in navigation bar active according to chosen page. Write your own macros for this feature. Put it in the `templates/macros.html`.