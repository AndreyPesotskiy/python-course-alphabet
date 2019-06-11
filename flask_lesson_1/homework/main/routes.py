from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')


@main.route("/")
def main_page():
    return render_template('home.html', title='Main')
