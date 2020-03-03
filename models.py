from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
Migrate(app,db)

### Add the model / table #####
class SurveyData(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    role01 = db.Column(db.Text)
    role02 = db.Column(db.Text)
    role03 = db.Column(db.Text)
    oddgoose01 = db.Column(db.Integer)
    construct1pos = db.Column(db.Text)
    construct1neg = db.Column(db.Text)
    rating_p1_const1 = db.Column(db.Integer)

# Initialize all the variables on creation of the table
    def __init__(self,role01, role02, role03, oddgoose01, construct1pos, construct1neg, rating_p1_const1):
        self.role01 = role01
        self.role02 = role02
        self.role03 = role03
        self.oddgoose01 = oddgoose01
        self.construct1pos = construct1pos
        self.construct1neg = construct1neg
        self.rating_p1_const1 = rating_p1_const1

# And make some basic string representation
    def __repr__(self):
        return "<Id: {}>".format(self.id)
