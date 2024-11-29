from flask import Blueprint, render_template, request, redirect, url_for
from .models import Todo
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@main.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.is_complete = not todo.is_complete
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.index'))
