from website import app
from website import db
from website.models.thread import Thread
from datetime import datetime
from flask import request


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/threads/<thread_name>', methods=['POST', 'GET'])
def create_new_thread(thread_name):
    thread = Thread(subject=thread_name, created_date=datetime.now())
    query = Thread.query.filter(Thread.subject == thread_name)
    if query.count() != 0:
        return "%s exists" % thread_name
    else:
        db.session.query()
        db.session.add(thread)
        db.session.commit()
        return "%s has been created" % thread_name


@app.route('/list_threads', methods=['GET'])
def list_threads():
    threads = Thread.query.all()
    return ', '.join(map(lambda x: x.subject, threads))


