from sqlalchemy import Column, Integer, String, Date
from website import db


class Thread(db.Model):
    id = Column(Integer, unique=True, primary_key=True)
    subject = Column(String(255), unique=True, nullable=False)
    body = Column(String(255))
    created_by = Column(String(255))
    created_date = Column(Date, nullable=False)
    last_modified_date = Column(Date)

    def __repr__(self):
        return '<Thread: %s>' % self.subject
