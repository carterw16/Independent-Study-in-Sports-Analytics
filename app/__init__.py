from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rangers'

from app import routes