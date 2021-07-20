from flask_wtf import FlaskForm
from wtforms.validators import *
from wtforms import *


class TodoForm(FlaskForm):
    id = TextAreaField("id", validators=[DataRequired()])
    name = TextAreaField("nazwa", validators=[DataRequired()])
    date = TextAreaField("start_date", validators=[DataRequired()])
    end_date = TextAreaField("end_date", validators=[DataRequired()])