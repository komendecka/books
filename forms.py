from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    read = BooleanField('read?', validators=[DataRequired()])
    country = StringField('country', validators=[DataRequired()])
    year = TextAreaField('year', validators=[DataRequired()])

