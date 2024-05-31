import os
from dotenv import load_dotenv

from flask import (Flask, request, session, g)
from flask_debugtoolbar import DebugToolbarExtension
from models import (db, dbx, Game)

from sqlalchemy.exc import IntegrityError

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///lotto')
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
toolbar = DebugToolbarExtension(app)

db.init_app(app)


Game.get_game_data('powerball')
