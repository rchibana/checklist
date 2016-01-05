__author__ = 'rchibana'

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():

    tasks = [
        {'created': '04/02/2016',
         'name': 'task1',
         'priority': 'high',
         'status': 'WIP'},
        {'created': '03/02/2016',
         'name': 'task2',
         'priority': 'normal',
         'status': 'TODO'},
        {'created': '01/02/2016',
         'name': 'task3',
         'priority': 'normal',
         'status': 'DONE'}
    ]

    return render_template('index.html',
                           title='WTF',
                           tasks=tasks)
