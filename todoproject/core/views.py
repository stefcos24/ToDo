from flask import render_template, request, Blueprint

from todoproject.models import Todos

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    todo = Todos.query.order_by(Todos.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', todo=todo)


@core.route('/info')
def info():
    return render_template('info.html')