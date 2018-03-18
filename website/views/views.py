from website import app
from flask import render_template
from website.lib.threads import Threads
import datetime


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/threads/<thread>')
def create_new_thread(thread):
    threads = Threads()
    threads.create_new_thread(thread, datetime.datetime.now())
    return thread


