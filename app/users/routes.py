import os, json
from urllib import request
from app import db, oauth
from app.models import Url, User
from flask import render_template, flash, redirect, url_for, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

users = Blueprint('users', __name__)

oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url=os.getenv("CONF_URL"),
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@users.route('/authorize')
def oauth_authorize():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    redirect_uri = url_for('users.oauth_callback', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@users.route('/authorize/callback')
def oauth_callback():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    token = oauth.google.authorize_access_token()
    user = token['userinfo']
    if not user['email_verified']:
        flash('Authentikasi gagal.')
        return redirect(url_for('main.index'))
    unique_id = user['sub']
    name = user['name']
    email = user['email']
    picture = user['picture']
    user = User.query.filter_by(unique_id=unique_id).first()
    if not user:
        user = User(unique_id=unique_id, name=name, email=email, picture=picture)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('main.index'))


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@users.route('/dashboard')
def dashboard():
    page = "Dashboard"

    urls = Url.query.filter_by(user_id=current_user.id)

    return render_template('dashboard.html', page=page, urls=urls)