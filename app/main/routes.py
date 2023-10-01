from app import db
from flask import render_template, request, flash, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from app.models import Url
from app.main.utils import generate_short_id
import segno

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    page = "home"

    if request.method == "POST":
        url = request.form["url"]
        short_id = request.form["custom_id"]

        if short_id and Url.query.filter_by(short_id=short_id).first() is not None:
            flash("Silahkan gunakan custom name yang lain", "red")
            return redirect(url_for("main.index"))

        if not url:
            flash("URL wajib dilengkapi!", "red")
            return redirect(url_for("main.index"))

        if not short_id:
            short_id = generate_short_id(5)

        if not current_user.is_anonymous:
            new_link = Url(original_url=url, short_id=short_id, user_id=current_user.id)
        else:
            new_link = Url(original_url=url, short_id=short_id)

        db.session.add(new_link)
        db.session.commit()
        return redirect(url_for("main.url_details", short_id=short_id))
    return render_template("index.html", page=page)


@main.route("/info")
def url_details():
    page = "Info URL"

    short_id = request.args["short_id"]
    link = Url.query.filter_by(short_id=short_id).first()
    if link:
        short_url = request.host_url + short_id
        qrcode = segno.make(short_url)
        return render_template("url_details.html", page=page, link=link, qrcode=qrcode)
    else:
        flash("URL tidak Valid!", "red")
        return redirect(url_for("main.index"))


@main.route("/update/<short_id>", methods=["GET", "POST"])
@login_required
def url_update(short_id):
    page = "Update URL"

    link = Url.query.filter_by(short_id=short_id).first()
    if link in current_user.urls:
        if request.method == "POST":
            url = request.form["url"]
            if not url:
                flash("URL wajib dilengkapi!", "red")
                return redirect(url_for("main.url_update", short_id=short_id))

            link.original_url = url
            db.session.commit()
            return redirect(url_for("main.url_details", short_id=short_id))

        return render_template("url_update.html", page=page, link=link)
    else:
        flash("Anda tidak memiliki akses!", "red")
        return redirect(url_for("main.index"))


@main.route("/<short_id>")
def url_redirect(short_id):
    link = Url.query.filter_by(short_id=short_id).first()
    if link:
        original_url = link.original_url
        link.clicks = link.clicks + 1
        db.session.commit()
        return redirect(original_url)
    else:
        flash("URL tidak Valid!", "red")
        return redirect(url_for("main.index"))

