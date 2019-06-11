from flask import Blueprint, render_template, request
import uuid

fruits = Blueprint('fruits', __name__, template_folder='templates')

fruits_data = {
    str(uuid.uuid4()): 'Apple',
    str(uuid.uuid4()): 'Banana',
    str(uuid.uuid4()): 'Grapes',
}


@fruits.route("/fruits", methods=["GET", "POST", "DELETE"])
def fruits_page():
    if request.method == "POST" and request.form['_method'] == "POST":
        create_fruit()
    elif request.method == "POST" and request.form['_method'] == "DELETE":
        remove_fruit()

    return render_template(
        'fruits_list.html',
        title='Fruits',
        fruits_data=fruits_data
    )


def create_fruit():
    title = request.form['title']
    if title:
        fruits_data[str(uuid.uuid4())] = title


def remove_fruit():
    fruit_id = request.form['id']
    if fruit_id and fruit_id in fruits_data:
        del fruits_data[fruit_id]
