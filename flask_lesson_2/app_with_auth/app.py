from datetime import timedelta

from flask import Flask

from config import run_config
from main import main
from auth import auth

app = Flask(__name__)
app.config.from_object(run_config())
app.permanent_session_lifetime = timedelta(minutes=20)  # add session expire time

app.register_blueprint(main)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug=True)
