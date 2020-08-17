import os
from flask_sqlalchemy import SQLAlchemy

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


class DatabaseItem():
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Question(db.Model, DatabaseItem):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=False)
    user = db.Column(db.String(), nullable=True)     # TODO: implement user functionality
    unique_id = db.Column(db.String(32), unique=True, nullable=False,
        default=str(uuid.uuid4().hex))
    answers = db.relationship('Answer', backref='question', lazy=True, cascade='all, delete-orphan')


class Answer(db.Model, DatabaseItem):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=False)
    question_id = db.Column(db.String(32), db.ForeignKey('questions.unique_id'), nullable=False)
    answer_id = db.Column(db.String(32), unique=True, nullable=False,
        default=str(uuid.uuid4().hex))
    count = db.Column(db.Integer, nullable=False, default=0)