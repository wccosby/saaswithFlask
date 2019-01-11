from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/') # attaching route to the blueprint, not the app itself
def home():
    return render_template('page/home.html')


@page.route('/terms')
def terms():
    return render_template('page/terms.html')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')
