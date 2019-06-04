from flask import Blueprint, render_template, request
import uuid

vegetables = Blueprint('vegetables', __name__, template_folder='templates')

vegetables_data = {
    str(uuid.uuid4()): 'Potatoes',
    str(uuid.uuid4()): 'Tomatoes',
    str(uuid.uuid4()): 'Spinach',
}


@vegetables.route("/vegetables", methods=["GET", "POST", "DELETE"])
def vegetables_page():
    if request.method == "POST" and request.form['_method'] == "POST":
        create_vegetable()
    elif request.method == "POST" and request.form['_method'] == "DELETE":
        remove_vegetable()

    return render_template(
        'vegetables_list.html',
        title='Vegetables',
        vegetables_data=vegetables_data
    )


def create_vegetable():
    title = request.form['title']
    if title:
        vegetables_data[str(uuid.uuid4())] = title


def remove_vegetable():
    vegetable_id = request.form['id']
    if vegetable_id and vegetable_id in vegetables_data:
        del vegetables_data[vegetable_id]
