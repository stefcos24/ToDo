from flask import render_template, redirect, url_for, Blueprint, abort, request, flash
from flask_login import login_required, current_user
from todoproject import db
from todoproject.models import Todos
from todoproject.todos.forms import TodosForm

todos = Blueprint('todos', __name__)

# CREATE
@todos.route('/create', methods=['GET', 'POST'])
@login_required
def create_todo():

    form = TodosForm()

    if form.validate_on_submit():

        todos = Todos(text=form.text.data,
        user_id=current_user.id)

        db.session.add(todos)
        db.session.commit()
        flash('Todos Created')

        return redirect(url_for('core.index'))
    
    return render_template('create_todo.html', form=form)


# READ
@todos.route('/<int:todos_id>')
def todo(todos_id):

    todo = Todos.query.get_or_404(todos_id)
    return render_template('todos.html', text=todo.text, date=todo.date, todo=todo)


# UPDATE
@todos.route('/<int:todos_id>/update', methods=['GET', 'POST'])
@login_required
def update_todo(todos_id):

    todo = Todos.query.get_or_404(todos_id)

    form = TodosForm()

    if form.validate_on_submit():

        todo.text = form.text.data

        db.session.commit()
        flash('Todo Updated')

        return redirect(url_for('todos.todo', todos_id=todo.id))

    elif request.method == 'GET':
        form.text.data = todo.text
    
    return render_template('create_todo.html', text='Updating', form=form)

# DELETE
@todos.route('/<int:todos_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_todo(todos_id):

    todo = Todos.query.get_or_404(todos_id)
    
    db.session.delete(todo)
    db.session.commit()
    flash('Blog Post Deleted')

    return redirect(url_for('core.index'))
