"""SQLAlchemy models for LottoChecker."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
dbx = db.session.execute


BASE_URL = "https://www.calottery.com/draw-games/"


class Game(db.Model):
    __tablename__ = "lotto_game"

    id = db.mapped_column(
        db.Integer,
        db.Identity(),
        primary_key=True
    )

    name = db.mapped_column(
        db.String(25),
        nullable=False
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

    has_jackpot = db.mapped_column(
        db.Boolean,
    )

    drawings = db.relationship(
        'Drawing', back_populates='game', cascade="all, delete-orphan")


class Drawing(db.Model):
    __tablename__ = "lotto_drawings"

    id = db.mapped_column(
        db.Integer,
        db.Identity(),
        primary_key=True
    )

    draw_date = db.mapped_column(
        db.DateTime,
        nullable=False
    )

    draw_number = db.mapped_column(
        db.Integer
    )

    jackpot_amount = db.mapped_column(
        db.Integer
    )

    drawing_balls = db.mapped_column(
        db.JSONB,
        nullable=False
    )

    mega_ball = db.mapped_column(
        db.Integer,
    )

    game_id = db.mapped_column(
        db.Integer,
        db.ForeignKey('lotto_game.game_id',
                      ondelete="CASCADE", onupdate="CASCADE")
    )

    game = db.relationship(
        'Game',
        back_populates='drawings'
    )
