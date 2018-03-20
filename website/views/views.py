from hashlib import md5
from website import app
from website import db
from website.models.content import Content
from website.models.thread import Thread
from website.models.user import User
from datetime import datetime
from flask import request, render_template, abort, session, make_response, redirect, url_for
import json


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/user/login', methods=['POST'])
def user_login():
    user = request.form['user']
    password = md5(request.form['password']).hexdigest()
    username = User.query.filter(User.user == user).one_or_none()
    if username is None:
        return abort(400)
    if username.password != password:
        return abort(400)

    response = make_response(url_for('list_threads'))
    response.set_cookie('user', user)
    return response


@app.route('/user/register', methods=['POST'])
def user_register():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = request.form['user']
    password = md5(request.form['password']).hexdigest()
    username = User.query.filter(User.user == user).one_or_none()
    if username is not None:
        return abort(400)
    new_user = User(user=user, password=password, created_date=date)
    db.session.add(new_user)
    db.session.commit()

    response = make_response(url_for('list_threads'))
    response.set_cookie('user', user)
    return response


@app.route('/thread/post_content', methods=['POST'])
def post_content():
    user = request.cookies.get('user')
    if user is None:
        return abort(400)
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    thread_name = request.form['thread']
    thread = Thread.query.filter(Thread.subject == thread_name).one_or_none()
    if thread is None:
        return abort(400)
    thread_id = thread.id
    body = request.form['body']
    created_by = user
    content = Content(thread_id=thread_id, body=body, created_by=created_by, created_date=date,
                      last_modified_date=date)
    db.session.add(content)
    db.session.commit()
    response = {'body': body, 'created_by': created_by, 'created_date': date,
                'last_modified_date': date}
    return json.dumps(response)


@app.route('/threads/<thread_name>', methods=['POST', 'GET'])
def load_thread(thread_name):
    user = request.cookies.get('user')
    if user is None:
        return abort(400)
    query = Thread.query.filter(Thread.subject == thread_name)
    print(query.count())
    if query.count() != 0:
        thread = query.one_or_none()
        print(thread)
        contents = Content.query.filter(Content.thread_id == thread.id).order_by(Content.created_date.desc())
        return render_template('thread/thread.html', thread=thread, contents=contents)
    else:
        date = datetime.now().strftime("%Y-%m-%d-%H-%M")
        user = request.cookies.get('user')
        thread = Thread(subject=thread_name, created_by=user, created_date=date)
        db.session.add(thread)
        db.session.commit()
        return render_template('thread/thread.html', thread=thread)


@app.route('/list_threads', methods=['GET'])
def list_threads():
    threads = Thread.query.all()
    return render_template('thread/threads_preview.html', threads=threads)


@app.route('/test')
def test():
    return render_template('thread/thread.html')




