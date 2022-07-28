from flask import Blueprint, render_template, request, redirect, url_for
from ..model import RealEstate

main = Blueprint('main', __name__)

@main.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        id = int(request.form['id'])
        return redirect(url_for('main.get_id', id=id))

    return render_template('index.html')

@main.route('/<int:id>')
def get_id(id):
    real_estate = RealEstate.query.get(id)
    if real_estate is not None:
        real_estate = real_estate.__dict__
        del real_estate['_sa_instance_state']
        return render_template('single_real_estate.html', real_estate=real_estate)

    return "Not found."
