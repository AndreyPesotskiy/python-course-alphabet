from flask import Flask

from app_blueprint.tree import trees

app = Flask(__name__)
app.register_blueprint(trees)

if __name__ == "__main__":
    app.run(debug=True)
