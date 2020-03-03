import os
from forms import  HomeForm, RolesForm, ComparisonForm, ConstructForm_Pos, ConstructForm_Neg, RatingForm
from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecret4key'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db, SurveyData

############################################
        # VIEWS WITH FORMS
##########################################

''' This survey follows a pre-defined format in three phases.
Phase 1 - people list 15 people who have played significant roles in their life.
Phase 2 - people generate constructs after comparing triads of the fifteen roles. Each construct is generated as a text item.
Phase 3 - each person (role) is rated on all fifteen of the constructs.

Following the survey, the results are calculated.

Below is a list of survey pages in order. The main idea is that the data from each page
is stored in a session dictionary and called for subsequent pages. The questions are somewhat repetitive in structure
so the same template is rendered with new input data. This could probably be refactored in future iterations.
We then save all the results to a database after the last input page.

Results are presented after computation in a separate module using PCA, the elbow technique, and some basic interpretive rules.'''

@app.route('/', methods=['GET','POST'])
def index():
    session.clear()
    form = HomeForm()
    if request.method == 'POST':
        session['id'] = form.name.data
        return redirect(url_for('roles'))
    return render_template('index.html', form=form)

############ Phase I - Role enumeration ############################################
@app.route('/roles', methods=['GET', 'POST'])
def roles():
    form = RolesForm()
    if form.validate_on_submit():
        session['role01'] = form.role01.data
        session['role02'] = form.role02.data
        session['role03'] = form.role03.data
        session['role04'] = form.role04.data
        session['role05'] = form.role05.data
        session['role06'] = form.role06.data
        session['role07'] = form.role07.data
        session['role08'] = form.role08.data
        session['role09'] = form.role09.data
        session['role10'] = form.role10.data
        session['role11'] = form.role11.data
        session['role12'] = form.role12.data
        session['role13'] = form.role13.data
        session['role14'] = form.role14.data
        session['role15'] = form.role15.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison1'))
    return render_template('roles2.html', form=form)


############## Phase II - Construct Generation #################################################################
# 2.1 ###################### Comparison set 1 (roles 10, 11, 12) ########################################
@app.route('/comparison1', methods=['GET','POST'])
def comparison1():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role10')), ('2', session.get('role11')), ('3', session.get('role12'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose01'] = form.oddoneout.data
        print(type(session.get('oddgoose01')))
        print(form.validate_on_submit())
        return redirect(url_for('construct1_pos'))

    return render_template('comparisons.html', form=form)

@app.route('/construct1a', methods=['GET','POST'])
def construct1_pos():
    threeroles = [session.get('role10'), session.get('role11'), session.get('role12')]
    oddone = threeroles.pop(session.get('oddgoose01')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct1pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct1_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct1b', methods=['GET','POST'])
def construct1_neg():
    pos_construct_to_feed = session['construct1pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct1neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison2'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.2 ############ Comparison Set 2 (roles 6, 13, 14) #####################################################
@app.route('/comparison2', methods=['GET','POST'])
def comparison2():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role06')), ('2', session.get('role13')), ('3', session.get('role14'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose02'] = form.oddoneout.data
        print(type(session.get('oddgoose02')))
        print(form.validate_on_submit())
        return redirect(url_for('construct2_pos'))

    return render_template('comparisons.html', form=form)

@app.route('/construct2a', methods=['GET','POST'])
def construct2_pos():
    threeroles = [session.get('role06'), session.get('role13'), session.get('role14')]
    oddone = threeroles.pop(session.get('oddgoose02')-1)
    form = ConstructForm_Pos()
    if request.method == 'POST':
        session['construct2pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct2_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct2b', methods=['GET','POST'])
def construct2_neg():
    pos_construct_to_feed = session['construct2pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct2neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison3'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.3 ############ Comparison Set 3 (roles 6, 9, 12) #####################################################
@app.route('/comparison3', methods=['GET','POST'])
def comparison3():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role06')), ('2', session.get('role09')), ('3', session.get('role12'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose03'] = form.oddoneout.data
        print(type(session.get('oddgoose03')))
        print(form.validate_on_submit())
        return redirect(url_for('construct3_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct3a', methods=['GET','POST'])
def construct3_pos():
    threeroles = [session.get('role06'), session.get('role09'), session.get('role12')]
    oddone = threeroles.pop(session.get('oddgoose03')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct3pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct3_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct3b', methods=['GET','POST'])
def construct3_neg():
    pos_construct_to_feed = session['construct3pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct3neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison4'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.4 ############ Comparison Set 4 (roles 3, 14, 15) #####################################################
@app.route('/comparison4', methods=['GET','POST'])
def comparison4():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role03')), ('2', session.get('role14')), ('3', session.get('role15'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose04'] = form.oddoneout.data
        print(type(session.get('oddgoose04')))
        print(form.validate_on_submit())
        return redirect(url_for('construct4_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct4a', methods=['GET','POST'])
def construct4_pos():
    threeroles = [session.get('role03'), session.get('role14'), session.get('role15')]
    oddone = threeroles.pop(session.get('oddgoose04')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct4pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct4_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct4b', methods=['GET','POST'])
def construct4_neg():
    pos_construct_to_feed = session['construct4pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct4neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison5'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.5 ############ Comparison Set 5 (roles 4, 11, 13) #####################################################
@app.route('/comparison5', methods=['GET','POST'])
def comparison5():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role04')), ('2', session.get('role11')), ('3', session.get('role13'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose05'] = form.oddoneout.data
        print(type(session.get('oddgoose05')))
        print(form.validate_on_submit())
        return redirect(url_for('construct5_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct5a', methods=['GET','POST'])
def construct5_pos():
    threeroles = [session.get('role04'), session.get('role11'), session.get('role13')]
    oddone = threeroles.pop(session.get('oddgoose05')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct5pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct5_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct5b', methods=['GET','POST'])
def construct5_neg():
    pos_construct_to_feed = session['construct5pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct5neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison6'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.6 ############ Comparison Set 6 (roles 2, 9, 10) #####################################################
@app.route('/comparison6', methods=['GET','POST'])
def comparison6():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role02')), ('2', session.get('role09')), ('3', session.get('role10'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose06'] = form.oddoneout.data
        print(type(session.get('oddgoose06')))
        print(form.validate_on_submit())
        return redirect(url_for('construct6_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct6a', methods=['GET','POST'])
def construct6_pos():
    threeroles = [session.get('role02'), session.get('role09'), session.get('role10')]
    oddone = threeroles.pop(session.get('oddgoose06')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct6pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct6_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct6b', methods=['GET','POST'])
def construct6_neg():
    pos_construct_to_feed = session['construct6pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct6neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison7'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.7 ############ Comparison Set 7 (roles 5, 7, 8) #####################################################
@app.route('/comparison7', methods=['GET','POST'])
def comparison7():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role05')), ('2', session.get('role07')), ('3', session.get('role08'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose07'] = form.oddoneout.data
        print(type(session.get('oddgoose07')))
        print(form.validate_on_submit())
        return redirect(url_for('construct7_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct7a', methods=['GET','POST'])
def construct7_pos():
    threeroles = [session.get('role05'), session.get('role07'), session.get('role08')]
    oddone = threeroles.pop(session.get('oddgoose07')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct7pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct7_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct7b', methods=['GET','POST'])
def construct7_neg():
    pos_construct_to_feed = session['construct7pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct7neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison8'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.8 ############ Comparison Set 8 (roles 9, 11, 15) #####################################################
@app.route('/comparison8', methods=['GET','POST'])
def comparison8():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role09')), ('2', session.get('role11')), ('3', session.get('role15'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose08'] = form.oddoneout.data
        print(type(session.get('oddgoose08')))
        print(form.validate_on_submit())
        return redirect(url_for('construct8_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct8a', methods=['GET','POST'])
def construct8_pos():
    threeroles = [session.get('role09'), session.get('role11'), session.get('role15')]
    oddone = threeroles.pop(session.get('oddgoose08')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct8pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct8_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct8b', methods=['GET','POST'])
def construct8_neg():
    pos_construct_to_feed = session['construct8pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct8neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison9'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.9 ############ Comparison Set 9 (roles 1, 4, 7) #####################################################
@app.route('/comparison9', methods=['GET','POST'])
def comparison9():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role01')), ('2', session.get('role04')), ('3', session.get('role07'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose09'] = form.oddoneout.data
        print(type(session.get('oddgoose09')))
        print(form.validate_on_submit())
        return redirect(url_for('construct9_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct9a', methods=['GET','POST'])
def construct9_pos():
    threeroles = [session.get('role01'), session.get('role04'), session.get('role07')]
    oddone = threeroles.pop(session.get('oddgoose09')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct9pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct9_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct9b', methods=['GET','POST'])
def construct9_neg():
    pos_construct_to_feed = session['construct9pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct9neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison10'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.10 ############ Comparison Set 10 (roles 3, 5, 13) #####################################################
@app.route('/comparison10', methods=['GET','POST'])
def comparison10():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role03')), ('2', session.get('role05')), ('3', session.get('role13'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose10'] = form.oddoneout.data
        print(type(session.get('oddgoose10')))
        print(form.validate_on_submit())
        return redirect(url_for('construct10_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct10a', methods=['GET','POST'])
def construct10_pos():
    threeroles = [session.get('role03'), session.get('role05'), session.get('role13')]
    oddone = threeroles.pop(session.get('oddgoose10')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct10pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct10_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct10b', methods=['GET','POST'])
def construct10_neg():
    pos_construct_to_feed = session['construct10pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct10neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison11'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.11 ############ Comparison Set 11 (roles 8, 12, 14) #####################################################
@app.route('/comparison11', methods=['GET','POST'])
def comparison11():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role08')), ('2', session.get('role12')), ('3', session.get('role14'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose11'] = form.oddoneout.data
        print(type(session.get('oddgoose11')))
        print(form.validate_on_submit())
        return redirect(url_for('construct11_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct11a', methods=['GET','POST'])
def construct11_pos():
    threeroles = [session.get('role08'), session.get('role12'), session.get('role14')]
    oddone = threeroles.pop(session.get('oddgoose11')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct11pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct11_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct11b', methods=['GET','POST'])
def construct11_neg():
    pos_construct_to_feed = session['construct11pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct11neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison12'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.12 ############ Comparison Set 12 (roles 4, 5, 15) #####################################################
@app.route('/comparison12', methods=['GET','POST'])
def comparison12():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role04')), ('2', session.get('role05')), ('3', session.get('role15'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose12'] = form.oddoneout.data
        print(type(session.get('oddgoose12')))
        print(form.validate_on_submit())
        return redirect(url_for('construct12_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct12a', methods=['GET','POST'])
def construct12_pos():
    threeroles = [session.get('role04'), session.get('role05'), session.get('role15')]
    oddone = threeroles.pop(session.get('oddgoose12')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct12pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct12_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct12b', methods=['GET','POST'])
def construct12_neg():
    pos_construct_to_feed = session['construct12pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct12neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison13'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.13 ############ Comparison Set 13 (roles 1, 2, 8) #####################################################
@app.route('/comparison13', methods=['GET','POST'])
def comparison13():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role01')), ('2', session.get('role02')), ('3', session.get('role08'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose13'] = form.oddoneout.data
        print(type(session.get('oddgoose13')))
        print(form.validate_on_submit())
        return redirect(url_for('construct13_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct13a', methods=['GET','POST'])
def construct13_pos():
    threeroles = [session.get('role01'), session.get('role02'), session.get('role08')]
    oddone = threeroles.pop(session.get('oddgoose13')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct13pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct13_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct13b', methods=['GET','POST'])
def construct13_neg():
    pos_construct_to_feed = session['construct13pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct13neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison14'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.14 ############ Comparison Set 14 (roles 2, 3, 7) #####################################################
@app.route('/comparison14', methods=['GET','POST'])
def comparison14():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role02')), ('2', session.get('role03')), ('3', session.get('role07'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose14'] = form.oddoneout.data
        print(type(session.get('oddgoose14')))
        print(form.validate_on_submit())
        return redirect(url_for('construct14_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct14a', methods=['GET','POST'])
def construct14_pos():
    threeroles = [session.get('role02'), session.get('role03'), session.get('role07')]
    oddone = threeroles.pop(session.get('oddgoose14')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct14pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct14_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct14b', methods=['GET','POST'])
def construct14_neg():
    pos_construct_to_feed = session['construct14pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct14neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('comparison15'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 2.14 ############ Comparison Set 15 (roles 1, 6, 10) #####################################################
@app.route('/comparison15', methods=['GET','POST'])
def comparison15():
    form = ComparisonForm()
    form.oddoneout.choices = [('1',session.get('role01')), ('2', session.get('role06')), ('3', session.get('role10'))]
    if request.method == 'POST':    #validate_on_submit()
        session['oddgoose15'] = form.oddoneout.data
        print(type(session.get('oddgoose15')))
        print(form.validate_on_submit())
        return redirect(url_for('construct15_pos'))
    return render_template('comparisons.html', form=form)

@app.route('/construct15a', methods=['GET','POST'])
def construct15_pos():
    threeroles = [session.get('role01'), session.get('role06'), session.get('role10')]
    oddone = threeroles.pop(session.get('oddgoose15')-1)
    form = ConstructForm_Pos()
    if form.validate_on_submit():
        session['construct15pos'] = form.positive_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('construct15_neg'))
    return render_template('construct_pos.html', form=form, oddone=oddone, threeroles=threeroles)

@app.route('/construct15b', methods=['GET','POST'])
def construct15_neg():
    pos_construct_to_feed = session['construct15pos']
    form = ConstructForm_Neg()
    if request.method == 'POST':
        session['construct15neg'] = form.negative_construct_pole.data
        print(form.validate_on_submit())
        return redirect(url_for('rating_instructions'))
    return render_template('construct_neg.html', form=form, pos_construct_to_feed=pos_construct_to_feed)

# 3 ################## Phase 3 - Rating of roles on constructs ##################################################

@app.route('/ratings_instructions', methods=['GET', 'POST'])
def rating_instructions():
    form = HomeForm()
    if request.method == 'POST':
        session['rating_counter']=1
        return redirect('ratings/{}'.format(session.get('rating_counter')))
    return render_template('ratings_instructions.html', form=form)

@app.route('/ratings/<rating_counter>', methods=['GET', 'POST'])
def ratings1(rating_counter):
    print('The value of the rating counter at the beginning is ' + str(session['rating_counter'])) # checking the counter
    target = session.get('role{:02d}'.format(session.get('rating_counter'))) # getting the new role
    form = RatingForm()
    #print(form.validate_on_submit())
    if request.method == 'POST':
        if session.get('rating_counter') < 15:
            session['rating_p{}_const1'.format(rating_counter)] = form.rating_const1.data
            session['rating_p{}_const2'.format(rating_counter)] = form.rating_const2.data
            session['rating_p{}_const3'.format(rating_counter)] = form.rating_const3.data
            session['rating_p{}_const4'.format(rating_counter)] = form.rating_const4.data
            session['rating_p{}_const5'.format(rating_counter)] = form.rating_const5.data
            session['rating_p{}_const6'.format(rating_counter)] = form.rating_const6.data
            session['rating_p{}_const7'.format(rating_counter)] = form.rating_const7.data
            session['rating_p{}_const8'.format(rating_counter)] = form.rating_const8.data
            session['rating_p{}_const9'.format(rating_counter)] = form.rating_const9.data
            session['rating_p{}_const10'.format(rating_counter)] = form.rating_const10.data
            session['rating_p{}_const11'.format(rating_counter)] = form.rating_const11.data
            session['rating_p{}_const12'.format(rating_counter)] = form.rating_const12.data
            session['rating_p{}_const13'.format(rating_counter)] = form.rating_const13.data
            session['rating_p{}_const14'.format(rating_counter)] = form.rating_const14.data
            session['rating_p{}_const15'.format(rating_counter)] = form.rating_const15.data
# A few commands to check the values were correctly set
#            print('the updated rating counter value is {}'.format(session.get('rating_counter')))
#            print('the value of the rating of role {} is {}'.format(session.get('rating_counter'),
#            session.get('rating_p{}_const1'.format(str(rating_counter)))))
            session['rating_counter']=session.get('rating_counter')+1 # Update the counter
# Checking the rating_counter
#            print('the updated rating counter value is {}'.format(session.get('rating_counter')))
            return redirect('ratings/{}'.format(session.get('rating_counter')))
        else:
            return redirect(url_for('results'))
            ## create a table of all the data ##

    return render_template('ratings.html', form=form, target=target,
        construct1pos_toshow = session.get('construct1pos'), construct1neg_toshow = session.get('construct1neg'),
        construct2pos_toshow = session.get('construct2pos'),
        construct2neg_toshow = session.get('construct2neg'),
        construct3pos_toshow = session.get('construct3pos'),
        construct3neg_toshow = session.get('construct3neg'),
        construct4pos_toshow = session.get('construct4pos'),
        construct4neg_toshow = session.get('construct4neg'),
        construct5pos_toshow = session.get('construct5pos'),
        construct5neg_toshow = session.get('construct5neg'),
        construct6pos_toshow = session.get('construct6pos'),
        construct6neg_toshow = session.get('construct6neg'),
        construct7pos_toshow = session.get('construct7pos'),
        construct7neg_toshow = session.get('construct7neg'),
        construct8pos_toshow = session.get('construct8pos'),
        construct8neg_toshow = session.get('construct8neg'),
        construct9pos_toshow = session.get('construct9pos'),
        construct9neg_toshow = session.get('construct9neg'),
        construct10pos_toshow = session.get('construct10pos'),
        construct10neg_toshow = session.get('construct10neg'),
        construct11pos_toshow = session.get('construct11pos'),
        construct11neg_toshow = session.get('construct11neg'),
        construct12pos_toshow = session.get('construct12pos'),
        construct12neg_toshow = session.get('construct12neg'),
        construct13pos_toshow = session.get('construct13pos'),
        construct13neg_toshow = session.get('construct13neg'),
        construct14pos_toshow = session.get('construct14pos'),
        construct14neg_toshow = session.get('construct14neg'),
        construct15pos_toshow = session.get('construct15pos'),
        construct15neg_toshow = session.get('construct15neg'),    )


################# Phase IV - Results ###########################
'''These are largely computed in another module and then imported here. I guess I make a dataframe to input into the function.
Then, have the function return a bunch of objects that I can display.'''
@app.route('/results', methods=['GET','POST'])
def results():
    data_list=['nup',session.get('construct1pos'),'is bland',session.get('construct1neg')]
    data_name=session.get('role01')
    data_chr=data_list[int(session.get('rating_p1_const1'))]
    return render_template('results.html', data_name=data_name, data_chr=data_chr)


if __name__ == '__main__':
    app.run(debug=True)
