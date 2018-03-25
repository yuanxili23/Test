from flask import abort


def validate_login(user):
    if user is None:
        return abort(401)
