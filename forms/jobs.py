from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Job Title', validators=[DataRequired()])
    team_leader = StringField('Team Leader id', validators=[DataRequired()])
    work_size = StringField("Work Size", validators=[DataRequired()])
    collaborators = StringField('Collaborators')
    is_finished = BooleanField("Is job finished?")
    submit = SubmitField('Submit')
