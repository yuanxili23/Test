from sqlalchemy import Column, Integer, String, Date
from website import db


class User(db.Model):
    id = Column(Integer, unique=True, primary_key=True)
    user = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_date = Column(Date, nullable=False)

    def __repr__(self):
        return '<User: %s>' % self.user
