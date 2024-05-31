"""SQLAlchemy models for LottoChecker."""

from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
import requests

db = SQLAlchemy()
dbx = db.session.execute


BASE_URL = "https://www.calottery.com/draw-games/"


class Game(db.Model):
    __tablename__ = "lotto-game"

    name = db.mapped_column(
        db.String(25),
        primary_key=True
    )

    total_ball_count = db.mapped_column(
        db.Integer,
        nullable=False
    )

    max_ball_value = db.mapped_column(
        db.Integer,
        nullable=False
    )

    may_repeat = db.mapped_column(
        db.Boolean,
        nullable=False
    )

    has_mega = db.mapped_column(
        db.Boolean,
        nullable=False
    )

    max_mega_value = db.mapped_column(
        db.Integer
    )

    @classmethod
    def get_game_data(cls, game):
        """Scrape information from web for new draw data"""

        data = requests.get(f"{BASE_URL}#section-content-2-3", "utf-8")

        parsed_data = BeautifulSoup(data.text, 'html.parser')
        print(parsed_data)


class Drawing(db.Model):
    __tablename__ = "lotto-drawings"

    id = db.mapped_column(
        db.Integer,
        primary_key=True
    )

    ball_1 = db.mapped_column(  # do I move this out of the way?
        db.Integer,
        nullable=False
    )

    ball_2 = db.mapped_column(
        db.Integer,
        nullable=False
    )

    ball_3 = db.mapped_column(
        db.Integer,
        nullable=False
    )

    ball_4 = db.mapped_column(
        db.Integer,
        nullable=False
    )

    ball_5 = db.mapped_column(
        db.Integer,
        nullable=False
    )

    mega_ball = db.mapped_column(
        db.Integer,
    )


# CALottoGame:
# CALottoGame {
#   game_name: 'PowerBall',
#   total_ball_count: 6,
#   non_mega_ball_count: 5,
#   has_mega: true,
#   may_repeat: false,
#   max_ball_value: 69,
#   max_mega_value: 26,
#   odds: 292201338,
#   mega_prizes: [ 2, 4, 10, 50, 100, -100 ],
#   non_mega_prizes: [ 0, 0, 0, 10, 100, -0.1 ],
#   ca_url_game_number: 15
# }
