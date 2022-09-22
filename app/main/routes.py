from app import db
from flask import render_template, request, flash, redirect, url_for, Blueprint
from app.models import ShortUrls
from app.main.utils import generate_short_id

main = Blueprint('main', __name__)

@main.route('/', methods=['GET','POST'])
def index():
    page = 'home'

    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['custom_id']

        if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
            flash('Silahkan gunakan custom name yang lain', 'red')
            return redirect(url_for('main.index'))

        if not url:
            flash('URL wajib dilengkapi!', 'red')
            return redirect(url_for('main.index'))
        
        if not short_id:
            short_id = generate_short_id(5)
        
        new_link = ShortUrls(original_url=url, short_id=short_id)
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id
        return redirect(url_for('main.url_details', short_id=short_id))
    return render_template('index.html', page=page)


# @main.route('/info/<short_id>')
# def url_details(short_id):
#     return render_template('url_details.html')

@main.route('/info')
def url_details():
    page = 'Info URL'
    short_id = request.args['short_id']
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        return render_template('url_details.html', page=page, link=link)
    else:
        flash('URL tidak Valid!', 'red')
        return redirect(url_for('main.index'))
        
@main.route('/<short_id>')
def url_redirect(short_id):
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        original_url = link.original_url
        link.clicks = link.clicks+1
        db.session.commit()
        return redirect(original_url)
    else:
        flash('URL tidak Valid!', 'red')
        return redirect(url_for('main.index'))


# TODO: Buat Halaman Handling Error