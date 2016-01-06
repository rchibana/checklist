__author__ = 'rchibana'

from app import app
from flask import render_template, redirect, url_for, request
from app.forms.task import TaskForm

@app.route('/new-task')
def new():
    form = TaskForm()
    # if request.method == 'get':
    return render_template('task/new.html',
                           form=form)


@app.route('/edit-task')
def edit():
    pass


@app.route('/delete-task')
def delete():
    pass