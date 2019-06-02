import os

from flask import Flask, request, render_template, jsonify, make_response, abort, url_for, session
from werkzeug.utils import secure_filename, redirect

from .messenger.routes import messenger

app = Flask(__name__)

app.register_blueprint(messenger)


@app.route('/')
def hello_world():
    return 'Our first route'


@app.route('/name/<int:index>')
def get_name(index):
    names = ["John", "Kate", "Nikolas"]
    try:
        return f"My name is {names[index]}"
    except IndexError:
        return "You are out of range"


@app.route('/float/<float:num>')
def get_float_value(num):
    if isinstance(num, float):
        return f"I'm float value {num}"


@app.route('/int/<int:num>')
def get_int_value(num):
    if isinstance(num, int):
        return f"I'm int value {num}"


@app.route('/number/<num>')
def get_number(num):
    if isinstance(num, str):
        return "Yes I'm string"


@app.route('/path/<path:val>')
def get_path(val):
    return val


@app.route('/read_from_file/<path:val>')
def get_data_from_file(val):
    with open(val) as file:
        return file.read()


@app.route('/uuid/<uuid:val>')
def get_uuid(val):
    print(type(val))
    return f"I'm uuid {val}"


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/request_object')
def get_request_object():
    client_name = request.headers.get("client_name")
    args = request.args
    base_url = request.base_url

    response = dict()
    response["client_name"] = client_name
    response["args"] = args
    response["base_url"] = base_url
    return jsonify(response)


test_methods_dict = ["Value 1", "Value 2"]


@app.route('/test_methods')
@app.route('/test_methods/<string:value>', methods=['GET', 'POST', 'DELETE'])
def test_methods(value=None):
    if request.method == 'POST':
        do_post(value)
        return "Successfully added a new value"
    if request.method == 'DELETE':
        do_delete(value)
        return "Successfully deleted the value"
    else:
        return do_get()


def do_post(value):
    """
    This method will add value to the test_methods_dict
    :return:
    """
    return test_methods_dict.append(value)


def do_get():
    """
    Returns template with all test_methods_dict values
    :return:
    """
    return render_template('test_methods.html', values=test_methods_dict, name="a")


def do_delete(value):
    """
    Delete values from test_methods_dict
    :param value:
    :return:
    """
    for i, elem in enumerate(test_methods_dict):
        if elem == value:
            test_methods_dict.pop(i)


@app.route("/file", methods=["POST"])
def save_file():
    f = request.files['file']
    file_path = os.path.join("files", secure_filename(f.filename))
    f.save(file_path)

    with open(file_path) as file:
        return file.read()


@app.route('/get_cookie')
def get_cookie():
    return jsonify(request.cookies)


@app.route('/set_cookie', methods=["POST"])
def set_cookie():
    import json
    response = make_response()
    for key, value in json.loads(request.data).items():
        response.set_cookie(key, value)  # not more then one value
    return response


@app.route("/test_redirect")
def test_redirect():
    return redirect(url_for("home_page"))


@app.route("/test_abort")
def test_abort():
    abort(501, "Our program has an error")


@app.errorhandler(501)
def error_501_handler(error):
    return render_template("error_501.html")


@app.route("/search")
def google():
    search_query = request.args.get("query")

    if not search_query:
        abort(404)
    if search_query == "avengers endgame":
        # http://127.0.0.1:5000/search?query=avengers+endgame
        return redirect("https://en.wikipedia.org/wiki/Avengers:_Endgame")
    if search_query == "april joke":
        # http://127.0.0.1:5000/search?query=april+joke
        abort(418)
    else:
        return "Come on, google it"


@app.errorhandler(418)
def error_418_handler(error):
    return render_template("error_418.html", error=error)


app.secret_key = b'"\xaa;\x0b\x12\x8a\xa1V+\x16\xc5\x91\xfb,\xcb#'


@app.route("/test_session")
def test_session():
    app.logger.warning("this is warning")
    app.logger.error("This is error")
    session["key"] = "value"
    return "hello"


if __name__ == '__main__':
    app.run()
