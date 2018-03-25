from website import app
from flask import render_template


@app.errorhandler(409)
def conflict(e):
    return render_template('error/409.html'), 409


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('error/405.html'), 405


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


@app.errorhandler(403)
def bad_request(e):
    return render_template('error/403.html'), 403


@app.errorhandler(401)
def unauthorized(e):
    return render_template('error/401.html'), 401


@app.errorhandler(400)
def bad_request(e):
    return render_template('error/400.html'), 400
