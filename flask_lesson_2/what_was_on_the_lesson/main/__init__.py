from flask import Blueprint, current_app

main = Blueprint('main', __name__)


@main.route("/")
def hell_from_main():
    print(current_app.config)
    return current_app.config.get("TEST_DB_CONNECTION")
