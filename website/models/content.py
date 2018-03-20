from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from website import db


class Content(db.Model):
    id = Column(Integer, unique=True, primary_key=True)
    thread_id = Column(Integer, ForeignKey('thread.id'))
    body = Column(String(255), unique=True, nullable=False)
    created_by = Column(String(255))
    created_date = Column(Date, nullable=False)
    last_modified_date = Column(Date, nullable=False)

    def __repr__(self):
        return '<Content: %s>' % self.body
