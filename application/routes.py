import ast
from flask import Blueprint, render_template, request, redirect, url_for
from application.data_layer.models import RealEstate
from .main import db

main = Blueprint('main', __name__)
filter_data = Blueprint('filter_data', __name__, url_prefix='/filter')

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

@filter_data.route('/', methods=('GET', 'POST'))
def filter():
    if request.method == 'POST':
        results = {
            'type': request.form.get('type'),
            'min': request.form['min'],
            'max': request.form['max'],
            'parking': request.form.get('parking')
        }
        return redirect(url_for('filter_data.get_filter_data', results=results))

    return render_template('filter.html')

@filter_data.route('/<results>')
def get_filter_data(results):
    results_dict = ast.literal_eval(results)
    filters = []

    query = db.session.query(RealEstate)

    if results_dict['type'] is not None:
        query = query.\
            filter(RealEstate.type == results_dict['type'])

    if results_dict['min'] != '':
        query = query. \
            filter(RealEstate.quadrature > float(results_dict['min']))

    if results_dict['max'] != '':
        query = query. \
            filter(RealEstate.quadrature < float(results_dict['max']))

    if results_dict['parking'] is not None:
        query = query. \
            filter(RealEstate.parking == 'Da')
    else:
        query = query. \
            filter(RealEstate.parking.in_(['Ne', None]))

    model_list = query.all()
    real_estates = []

    # for i in range(len(model_list)):
    #     real_estates.append(model_list[i].__dict__)
    #     del real_estates[i]['_sa_instance_state']

    return render_template('list_real_estate.html', real_estates=model_list)
