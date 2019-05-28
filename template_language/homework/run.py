import json

from flask import Flask, render_template

app = Flask(__name__)

with open('movies.json') as f:
    MOVIES = json.load(f)

max_year = 2010

@app.route('/')
def home_page():
    return render_template('home.html', title='Home', name='Andrew Pesotskiy')


@app.route('/movies')
def movies_page():
    return render_template(
        'movies.html',
        title='Movies list',
        movies=MOVIES,
        max_year=max_year
    )


@app.route('/<id>')
def movie_page(id):
    """
    I decided to use the ID in the link.
    Because there are spaces in the title that do not look beautiful in the
    link :)
    """
    for i, movie in enumerate(MOVIES):
        if MOVIES[i].get('id') == id:
            return render_template(
                'movie.html',
                title=MOVIES[i].get('title'),
                movie=MOVIES[i]
            )
    return render_template(
        'movies.html',
        title='Movies list',
        movies=MOVIES,
        max_year=max_year
    )


if __name__ == '__main__':
    app.run(debug=True)
