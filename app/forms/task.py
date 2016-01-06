__author__ = 'rchibana'

from flask.ext.wtf import Form
from wtforms import StringField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired
from app import app


class TaskForm(Form):
    created = DateField('Created at')
    name = StringField('Task name', validators=[DataRequired()])
    priority = SelectField('Priority', choices=app.config['PRIORITYS'], validators=[DataRequired()])
    status = BooleanField('Status')
