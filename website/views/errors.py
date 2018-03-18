from website import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404

