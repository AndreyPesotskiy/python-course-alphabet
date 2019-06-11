from flask import Blueprint, render_template, url_for

messenger = Blueprint('messenger', __name__, template_folder='template')


@messenger.route("/messenger/home")
def go_home():
    return render_template("mess_home.html")
