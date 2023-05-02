from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = "users"

    username = db.Column(db.String, primary_key=True)

    reservations = db.relationship("Reservation", back_populates="user")

    def __repr__(self):
        return f"<User username={self.username}>"


class Reservation(db.Model):

    __tablename__ = "reservations"

    reservation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, db.ForeignKey("users.username"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)

    user = db.relationship("User", back_populates="reservations")

    def __repr__(self):
        return f"<Reservation date={self.date} start_time={self.start_time}>"

def connect_to_db(flask_app, db_uri="postgresql:///melon", echo=False):
    """Connect to database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)