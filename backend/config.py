from flask import Flask
import sqlalchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Point to a local SQLite database file (stored in backend/).
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = sqlalchemy(app)

#todo
# uninstall immediately cors
# keep Flask-Cors
# more code review

