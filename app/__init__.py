from flask import Flask
from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = '27c1e660-1192-4233-a7ed-3dddfe119242'

from app import routes