from flask import Blueprint, render_template


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    page = "404 Error"
    return render_template("errors/404.html", page=page), 404


# TODO: Make Handling 403 and 500 Errors Page