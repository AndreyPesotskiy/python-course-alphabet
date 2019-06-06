from flask import Flask, url_for, render_template
from flask_lesson_1.homework.main.routes import main
from flask_lesson_1.homework.fruits.routes import fruits
from flask_lesson_1.homework.vegetables.routes import vegetables
from werkzeug.utils import redirect

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(fruits)
app.register_blueprint(vegetables)


@app.route("/redirect")
def one_redirect():
    return redirect(url_for("main.main_page"))


@app.errorhandler(404)
def error_404_handler(error):
    return render_template("error_404.html", error=error)


if __name__ == '__main__':
    app.run(debug=True)
