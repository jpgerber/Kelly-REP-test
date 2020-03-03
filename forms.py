from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, InputRequired

''' This document houses all the forms used in the program '''

class FieldsRequiredForm(FlaskForm):
    """Require all fields to have content. This works around the bug that WTForms radio
    fields don't honor the `DataRequired` or `InputRequired` validators.
    """

    class Meta:
        def render_field(self, field, render_kw):
            render_kw.setdefault('required', True)
            return super().render_field(field, render_kw)

class HomeForm(FlaskForm):
    submit = SubmitField('Click here to continue')
    name = StringField('Type in an ID in case you want to recover results later', validators=[DataRequired()])

class RolesForm(FieldsRequiredForm):
    role01 = StringField('Your mother or the person who has played the part of a mother in your life:')
    role02 = StringField('Your father or the person who has played the part of a father in your life:', validators=[DataRequired()])
    role03 = StringField('Your brother nearest your age: (If you have no brother, the person who is most like one)', validators=[DataRequired()])
    role04 = StringField('Your sister nearest your age. If you have no sister, the person who is most like one.', validators=[DataRequired()])
    role05 = StringField('A teacher you liked or the teacher of a subject you liked:', validators=[DataRequired()])
    role06 = StringField('A teacher you disliked or the teacher of a subject you disliked:', validators=[DataRequired()])
    role07 = StringField('Your closest romantic partner immediately before you started going with your current romantic partner:', validators=[DataRequired()])
    role08 = StringField('Your current romantic partner:', validators=[DataRequired()])
    role09 = StringField('An employer, supervisor, or officer under whom you served during a period of great stress:', validators=[DataRequired()])
    role10 = StringField('A person with whom you have been closely associated, who for some unexplainable reason, appeared to dislike you:', validators=[DataRequired()])
    role11 = StringField('The person whom you have met within the past six months whom you would most like to know better:', validators=[DataRequired()])
    role12 = StringField('The person whom you would most like to be of help to, or whom you feel most sorry for:', validators=[DataRequired()])
    role13 = StringField('The most intelligent person whom you know personally:', validators=[DataRequired()])
    role14 = StringField('The most successful person whom you know personally:', validators=[DataRequired()])
    role15 = StringField('The most interesting person whom you know personally.', validators=[DataRequired()])
    submit = SubmitField('Submit names')

class ComparisonForm(FieldsRequiredForm):

    id = IntegerField('Person ID')
    submit = SubmitField('Submit')
    oddoneout = RadioField('Which of the following three people is least like the other two?',
    choices=[('Bob','Bob'),('Jane','Jane')], coerce=int)

class ConstructForm_Pos(FlaskForm):

    id = IntegerField('Person ID')
    submit = SubmitField('Submit')
    positive_construct_pole = StringField('In what important way are the two similar people alike?')

class ConstructForm_Neg(FlaskForm):
    id = IntegerField('Person ID')
    submit = SubmitField('Submit')
    negative_construct_pole = StringField('What is the opposite of the positive construct?')


class Pass(FlaskForm):
    pass

class RatingForm(FieldsRequiredForm):
    rating_const1 = RadioField(u'construct1', choices=[('2','Positive'),('1','Both'),('0','Negative')])
    rating_const2 = RadioField(u'construct2', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const3 = RadioField(u'construct3', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const4 = RadioField(u'construct4', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const5 = RadioField(u'construct5', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const6 = RadioField(u'construct6', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const7 = RadioField(u'construct7', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const8 = RadioField(u'construct8', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const9 = RadioField(u'construct9', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const10 = RadioField(u'construct10', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const11 = RadioField(u'construct11', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const12 = RadioField(u'construct12', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const13 = RadioField(u'construct13', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const14 = RadioField(u'construct14', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    rating_const15 = RadioField(u'construct15', choices=[('1','Positive'),('0','Both'),('-1','Negative')])
    id = IntegerField('Person ID')
    submit = SubmitField('Submit')
''' Finally, for Phase 4, please rate each of the 25 roles (0-24), or rather the person who exemplified each role, on each of the 25 constructs. In other words, rate
the degree to which each of the 25 constructs elicited in Phase 2 describes each of the 25 role-exemplar elicited in Phase 1.'''
