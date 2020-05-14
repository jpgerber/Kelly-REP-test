import os
from flask import Flask, render_template, url_for, redirect, request, session
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
from sklearn.datasets import load_breast_cancer
import seaborn as sns
import numpy as np
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.pyplot import switch_backend
from factor_analyzer import FactorAnalyzer
from kneed import KneeLocator
from io import BytesIO
import base64
from matplotlib.transforms import Bbox, TransformedBbox, Affine2D
from matplotlib import  tight_bbox

np.set_printoptions(precision=3, linewidth=100, suppress=True)

###################### Basic initialization of the app ###########################################
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecret4key'

# Configuring the database path
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing a connection to the engine (to which we then make queries via our db_session)
def get_test_data():
    from database import init_db
    init_db()
    complete_users_data = pd.read_sql("SELECT * FROM SurveyData WHERE id = 1", db_session.bind)
    complete_users_data.to_csv('test_data.csv')
    print(complete_users_data.head())

####################################################################################################################
################## This section sets up the various files needed for analysis ######################################
####################################################################################################################

# List of positive constructs
def get_pos_handles():
    '''Returns a list of positive handles
    '''
    return [session['construct1pos'], session['construct2pos'], session['construct3pos'],
            session['construct4pos'], session['construct5pos'], session['construct6pos'], session['construct7pos'],
            session['construct8pos'], session['construct9pos'], session['construct10pos'], session['construct11pos'],
            session['construct12pos'], session['construct13pos'], session['construct14pos'], session['construct15pos']
            ]

# List of negative constructs
def get_neg_handles():
    '''Returns a list of the negative handles
    '''
    return [session['construct1neg'], session['construct2neg'], session['construct3neg'],
            session['construct4neg'], session['construct5neg'], session['construct6neg'], session['construct7neg'],
            session['construct8neg'], session['construct9neg'], session['construct10neg'], session['construct11neg'],
            session['construct12neg'], session['construct13neg'], session['construct14neg'], session['construct15neg']
            ]

# List of combined constructs
def get_construct_names():
    '''Returns a list of combined construct names
    '''
    pos_hands = get_pos_handles()
    #[session['construct1pos'], session['construct2pos'], session['construct3pos'],
    #            session['construct4pos'], session['construct5pos'], session['construct6pos'], session['construct7pos'],
    #            session['construct8pos'], session['construct9pos'], session['construct10pos'], session['construct11pos'],
    #            session['construct12pos'], session['construct13pos'], session['construct14pos'], session['construct15pos']]
    neg_hands = [session['construct1neg'], session['construct2neg'], session['construct3neg'],
    session['construct4neg'], session['construct5neg'], session['construct6neg'], session['construct7neg'],
    session['construct8neg'], session['construct9neg'], session['construct10neg'], session['construct11neg'],
    session['construct12neg'], session['construct13neg'], session['construct14neg'], session['construct15neg']]
    return [i + ' - ' + j for i, j in zip(pos_hands, neg_hands)]

# Names for each role
def get_people_names():
    '''Returns a list of the person names for each role minus any duplicates'''
    list_of_names = [session['role01'], session['role02'], session['role03'], session['role04'], session['role05'],
    session['role06'], session['role07'], session['role08'], session['role09'], session['role10'],
    session['role11'], session['role12'], session['role13'], session['role14'], session['role15']]
    #list_of_names = pd.Series([session['role01'], session['role02'], session['role03'], session['role04'], session['role05'],
    #session['role06'], session['role07'], session['role08'], session['role09'], session['role10'],
    #session['role11'], session['role12'], session['role13'], session['role14'], session['role15']])
    #print("BAM!")
    #print(list_of_names)
    #rev_list = list_of_names.loc[~duplicates_series].to_list()
    #print(duplicates_series.values)
    #print('BOOO!')
    #print(rev_list)
    #return rev_list
    return list_of_names

# Df (and wrangling) of main ratings matrix
def get_ratings_matrix():
    '''Returns a dataframe of ratings for use in the analysis (in integers). Columns named c1-c15'''
    ratings_mat = pd.DataFrame(np.array([ [ session['rating_p1_const1'], session['rating_p1_const2'],
    session['rating_p1_const3'], session['rating_p1_const4'], session['rating_p1_const5'],
    session['rating_p1_const6'], session['rating_p1_const7'], session['rating_p1_const8'],
    session['rating_p1_const9'], session['rating_p1_const10'], session['rating_p1_const11'],
    session['rating_p1_const12'], session['rating_p1_const13'], session['rating_p1_const14'],
    session['rating_p1_const15'] ],
    [session['rating_p2_const1'], session['rating_p2_const2'], session['rating_p2_const3'],
    session['rating_p2_const4'], session['rating_p2_const5'], session['rating_p2_const6'],
    session['rating_p2_const7'], session['rating_p2_const8'], session['rating_p2_const9'],
    session['rating_p2_const10'], session['rating_p2_const11'], session['rating_p2_const12'],
    session['rating_p2_const13'], session['rating_p2_const14'], session['rating_p2_const15'] ],
    [session['rating_p3_const1'], session['rating_p3_const2'], session['rating_p3_const3'],
    session['rating_p3_const4'], session['rating_p3_const5'], session['rating_p3_const6'],
    session['rating_p3_const7'], session['rating_p3_const8'], session['rating_p3_const9'],
    session['rating_p3_const10'], session['rating_p3_const11'], session['rating_p3_const12'],
    session['rating_p3_const13'], session['rating_p3_const14'], session['rating_p3_const15'] ],
    [session['rating_p4_const1'], session['rating_p4_const2'], session['rating_p4_const3'],
    session['rating_p4_const4'], session['rating_p4_const5'], session['rating_p4_const6'],
    session['rating_p4_const7'], session['rating_p4_const8'], session['rating_p4_const9'],
    session['rating_p4_const10'], session['rating_p4_const11'], session['rating_p4_const12'],
    session['rating_p4_const13'], session['rating_p4_const14'], session['rating_p4_const15'] ],
    [session['rating_p5_const1'], session['rating_p5_const2'], session['rating_p5_const3'],
    session['rating_p5_const4'], session['rating_p5_const5'], session['rating_p5_const6'],
    session['rating_p5_const7'], session['rating_p5_const8'], session['rating_p5_const9'],
    session['rating_p5_const10'], session['rating_p5_const11'], session['rating_p5_const12'],
    session['rating_p5_const13'], session['rating_p5_const14'], session['rating_p5_const15'] ],
    [session['rating_p6_const1'], session['rating_p6_const2'], session['rating_p6_const3'],
    session['rating_p6_const4'], session['rating_p6_const5'], session['rating_p6_const6'],
    session['rating_p6_const7'], session['rating_p6_const8'], session['rating_p6_const9'],
    session['rating_p6_const10'], session['rating_p6_const11'], session['rating_p6_const12'],
    session['rating_p6_const13'], session['rating_p6_const14'], session['rating_p6_const15'] ],
    [session['rating_p7_const1'], session['rating_p7_const2'], session['rating_p7_const3'],
    session['rating_p7_const4'], session['rating_p7_const5'], session['rating_p7_const6'],
    session['rating_p7_const7'], session['rating_p7_const8'], session['rating_p7_const9'],
    session['rating_p7_const10'], session['rating_p7_const11'], session['rating_p7_const12'],
    session['rating_p7_const13'], session['rating_p7_const14'], session['rating_p7_const15'] ],
    [session['rating_p8_const1'], session['rating_p8_const2'], session['rating_p8_const3'],
    session['rating_p8_const4'], session['rating_p8_const5'], session['rating_p8_const6'],
    session['rating_p8_const7'], session['rating_p8_const8'], session['rating_p8_const9'],
    session['rating_p8_const10'], session['rating_p8_const11'], session['rating_p8_const12'],
    session['rating_p8_const13'], session['rating_p8_const14'], session['rating_p8_const15'] ],
    [session['rating_p9_const1'], session['rating_p9_const2'], session['rating_p9_const3'],
    session['rating_p9_const4'], session['rating_p9_const5'], session['rating_p9_const6'],
    session['rating_p9_const7'], session['rating_p9_const8'], session['rating_p9_const9'],
    session['rating_p9_const10'], session['rating_p9_const11'], session['rating_p9_const12'],
    session['rating_p9_const13'], session['rating_p9_const14'], session['rating_p9_const15'] ],
    [session['rating_p10_const1'], session['rating_p10_const2'], session['rating_p10_const3'],
    session['rating_p10_const4'], session['rating_p10_const5'], session['rating_p10_const6'],
    session['rating_p10_const7'], session['rating_p10_const8'], session['rating_p10_const9'],
    session['rating_p10_const10'], session['rating_p10_const11'], session['rating_p10_const12'],
    session['rating_p10_const13'], session['rating_p10_const14'], session['rating_p10_const15'] ],
    [session['rating_p11_const1'], session['rating_p11_const2'], session['rating_p11_const3'],
    session['rating_p11_const4'], session['rating_p11_const5'], session['rating_p11_const6'],
    session['rating_p11_const7'], session['rating_p11_const8'], session['rating_p11_const9'],
    session['rating_p11_const10'], session['rating_p11_const11'], session['rating_p11_const12'],
    session['rating_p11_const13'], session['rating_p11_const14'], session['rating_p11_const15'] ],
    [session['rating_p12_const1'], session['rating_p12_const2'], session['rating_p12_const3'],
    session['rating_p12_const4'], session['rating_p12_const5'], session['rating_p12_const6'],
    session['rating_p12_const7'], session['rating_p12_const8'], session['rating_p12_const9'],
    session['rating_p12_const10'], session['rating_p12_const11'], session['rating_p12_const12'],
    session['rating_p12_const13'], session['rating_p12_const14'], session['rating_p12_const15'] ],
    [session['rating_p13_const1'], session['rating_p13_const2'], session['rating_p13_const3'],
    session['rating_p13_const4'], session['rating_p13_const5'], session['rating_p13_const6'],
    session['rating_p13_const7'], session['rating_p13_const8'], session['rating_p13_const9'],
    session['rating_p13_const10'], session['rating_p13_const11'], session['rating_p13_const12'],
    session['rating_p13_const13'], session['rating_p13_const14'], session['rating_p13_const15'] ],
    [session['rating_p14_const1'], session['rating_p14_const2'], session['rating_p14_const3'],
    session['rating_p14_const4'], session['rating_p14_const5'], session['rating_p14_const6'],
    session['rating_p14_const7'], session['rating_p14_const8'], session['rating_p14_const9'],
    session['rating_p14_const10'], session['rating_p14_const11'], session['rating_p14_const12'],
    session['rating_p14_const13'], session['rating_p14_const14'], session['rating_p14_const15'] ],
    [session['rating_p15_const1'], session['rating_p15_const2'], session['rating_p15_const3'],
    session['rating_p15_const4'], session['rating_p15_const5'], session['rating_p15_const6'],
    session['rating_p15_const7'], session['rating_p15_const8'], session['rating_p15_const9'],
    session['rating_p15_const10'], session['rating_p15_const11'], session['rating_p15_const12'],
    session['rating_p15_const13'], session['rating_p15_const14'], session['rating_p15_const15'] ] ])).astype(float)
    ratings_mat.columns = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15']
    return ratings_mat

def get_self_ratings():
    '''Returns a list of self-ratings as integers'''
    return [int(x) for x in [session['rating_p16_const1'], session['rating_p16_const2'], session['rating_p16_const3'],
    session['rating_p16_const4'], session['rating_p16_const5'], session['rating_p16_const6'],
    session['rating_p16_const7'], session['rating_p16_const8'], session['rating_p16_const9'],
    session['rating_p16_const10'], session['rating_p16_const11'], session['rating_p16_const12'],
    session['rating_p16_const13'], session['rating_p16_const14'], session['rating_p16_const15'] ]]


#############################################################################################################
###########         Analysis written as functions                                   #########################
#############################################################################################################

# Calculate the factor analysis (plus kneed version), return the loadings matrix df
def make_loadings_matrix(rating_m):
    '''Takes a rating matrix and returns the loading matrix. Optimized for number of components
    using the knee, with a oblimin rotation for interpretability
    '''
    # Fit the initial factor analysis
    fa = FactorAnalyzer(n_factors=10, rotation='oblimin')
    fa.fit(rating_m)
    x = list(range(1,16))
    fa_eigens = fa.get_eigenvalues()[1]
    fa_matrix_knee = KneeLocator(x, fa_eigens, S=1.0, curve='convex', direction='decreasing')
    fa_knee = fa_matrix_knee.knee
    fa_kneed = FactorAnalyzer(n_factors=fa_knee, rotation='varimax').fit(rating_m)
    loadings_m = pd.DataFrame(fa_kneed.loadings_.round(2))
    loadings_m.index = get_construct_names()
    loadings_m.index = loadings_m.index.rename(name='Construct')
    loadings_m.columns = ['Factor {} ({:.0f}%)'.format(i+1, fa_kneed.get_factor_variance()[1][i]*100) for i in loadings_m.columns]
    return loadings_m

# Make a people matrix(return a df labelled by person)
def make_targets_matrix(ratings_matrix_name, factor_loadings_matrix):
    '''Fill in
    '''
    target_scores = pd.DataFrame(np.dot(ratings_matrix_name, factor_loadings_matrix))
    target_scores.index = get_people_names()                # Give the correct indices
    target_scores.columns = factor_loadings_matrix.columns  # Label the columns
    return target_scores

# Define some functions for returning top 3 positive and negative poles and top and bottom exemplars on a dimension
def get_top_pos_handles(df, col_idx):
    '''For a dataframe, gives the handles for the top three loadings on the positive pole for that column.
    Important: the dataframe index must be an integer.
    '''
    # Make the top three
    neg_handles = get_neg_handles()
    pos_handles = get_pos_handles()
    top3_mask = df.iloc[:,col_idx].abs().nlargest(3).index
    top3_constructs = df.loc[top3_mask]
    pos_top3 = [] # Make a return list
    for i in range(0,3):     # Then get the handles for the top three constructs
        if top3_constructs.iloc[i,col_idx] > 0: # for positive loadings
            pos_top3.append(pos_handles[top3_constructs.index[i]])
        elif top3_constructs.iloc[i,col_idx] < 0: # for negative loadings
            pos_top3.append(neg_handles[top3_constructs.index[i]])
    return pos_top3     # Return a list

def get_top_neg_handles(df, col_idx):
    '''For a dataframe, gives the handles for the top three loadings on the negative pole for that column.
    Important: the dataframe index must be an integer.
    '''
    neg_handles = get_neg_handles()
    pos_handles = get_pos_handles()
    # Find the top 3 rows
    top3_mask = df.iloc[:,col_idx].abs().nlargest(3).index
    top3_constructs = df.loc[top3_mask]
    pos_top3 = []              # Make a return list
    for i in range(0,3):     # Then get the handles for the top three constructs
        if top3_constructs.iloc[i,col_idx] < 0: # for negative loadings
            pos_top3.append(pos_handles[top3_constructs.index[i]])
        elif top3_constructs.iloc[i,col_idx] > 0: # for positive loadings
            pos_top3.append(neg_handles[top3_constructs.index[i]])
    return pos_top3     # Return a list

def find_max_scorer(targets_matrix, col_idx):
    '''This function returns the name of the most positive exemplar of a component'''
    return targets_matrix.iloc[targets_matrix.iloc[:,col_idx].argsort()].index[-1]

def find_min_scorer(targets_matrix, col_idx):
    '''This function returns the name of the most negative exemplar of a component'''
    return targets_matrix.iloc[targets_matrix.iloc[:,col_idx].argsort()].index[0]

# Make the prose description (return a paragraph)
def loadings_describer(loadings_matrix, targets_matrix):
    ''' This function describes the loadings matrix in prose. It first defines some functions to take the top and bottom values.
    '''
    fa_top3 = loadings_matrix.reset_index() # Make a version of the table with an integer index for use in future functions
    neg_hands=get_neg_handles()
    pos_hands=get_pos_handles()
    # Here is the prose interpreter
    position=['first', 'second','third','fourth','fifth','sixth','seventh','eighth']
    paragraph=[]
    paragraph.append('You assess people you know using {} different factors.'.format(loadings_matrix.shape[1]))
    paragraph.append('')
    for j in range(1, loadings_matrix.shape[1]+1):
        pos_3 = get_top_pos_handles(fa_top3, j)
        neg_3 = get_top_neg_handles(fa_top3, j)
        pos_exemplar = find_max_scorer(targets_matrix, j-1)
        neg_exemplar = find_min_scorer(targets_matrix, j-1)
#        print('Factor {} ({} vs {}), {:.2f}% of ratings'.format(j, pos_3, neg_3, fa_kneed.get_factor_variance()[1][j-1]*100))
        paragraph.append('Factor {}'.format(j))
        paragraph.append('One end of the {} way you think about people is how much they are {}, {} and {}. You think {} is most like this.'.
        format(position[j-1], pos_3[0], pos_3[1], pos_3[2], pos_exemplar))
        paragraph.append('The other end of this factor is how much a person is {}, {} and {}. You think {} is most like this.'.
         format(neg_3[0], neg_3[1], neg_3[2], neg_exemplar))
        paragraph.append('')

    return paragraph

# calculate the factor graphs for each dimension (return five images)
def draw_standing_charts(t_m):
    ''' This is not perfect, there were some issues with formatting it for the bytesIO stream
    As a result, some of it is handdrawn later on.
    '''
    # Some prelim info calls to construct the charts
    self_rat = get_self_ratings()
    self_scores = np.dot(self_rat, make_loadings_matrix(get_ratings_matrix()))
    fa_top3 = make_loadings_matrix(get_ratings_matrix()).reset_index()
    people = get_people_names()
    pos_hands=get_pos_handles()
    neg_hands=get_neg_handles()

    # Do the graphing
    switch_backend('Agg')
    fig, axs = plt.subplots(nrows=self_scores.shape[0], ncols=1, figsize=(14,9))
#    fig.suptitle('How you thought every person fit on each factor')
    sns.set(style="white")
    for i in range(0,self_scores.shape[0]):
        x = t_m.iloc[:,i]
        sns.swarmplot(x=x, linewidth=0, ax=axs[i])
        axs[i].set_title('Factor {}'.format(i+1), loc='left', pad=45)
        axs[i].set_xlabel('')
        axs[i].set_xticks([])
        sns.despine(top=True, left=True)
        # Then label the points
        for person in range(0,x.shape[0]):
            axs[i].text(x[person], 0, people[person], horizontalalignment='left', rotation=45, size='medium', color='black')
        # Add self dot in different color
        axs[i].plot(self_scores[i], 0 , 'rD', color='red', )
        axs[i].text(self_scores[i], 0, 'Me', rotation=45, weight='bold')
        # Label the two axes
        axs[i].annotate(get_top_neg_handles(fa_top3, i+1), xy=(0,-20), xycoords="axes pixels", ha='left')
        axs[i].annotate(get_top_pos_handles(fa_top3, i+1), xy=(1090,-20), xycoords="axes pixels", ha='right')
        plt.subplots_adjust(hspace=20)
    # Exporting as a bytes stream
    pngImage = BytesIO()
    FigureCanvas(fig).print_png(pngImage)
        # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    plt.close()

    return pngImageB64String

# Calculate the seaborn version of the loadings matrix (return bytes feed)
def draw_loadings_heatmap(fa_loadings):
    switch_backend('Agg')
    fig = Figure(figsize=(6,8))
    axis = fig.add_subplot(1, 1, 1)
    fig.subplots_adjust(bottom=0.2, left=0.54)
    sns.heatmap(fa_loadings, annot=True, vmin=-1, vmax=1, center=0, cmap='coolwarm', ax=axis)
    axis.set_title('Factor loadings')
    axis.set_xticklabels(axis.get_xticklabels(),rotation=90)
    axis.set_yticklabels(axis.get_yticklabels(),rotation=0)
    plt.tight_layout()
    # From here is image conversion
    pngImage = BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    plt.close()

    return pngImageB64String

# Calculate the seaborn version of the targets matrix (return bytes feed)
def draw_targets_heatmap(target_loadings):
    switch_backend('Agg')
    fig = Figure(figsize=(6,8))
    axis = fig.add_subplot(1, 1, 1)
    fig.subplots_adjust(bottom=0.2, left=0.3)
    sns.heatmap(target_loadings, annot=True, center=0, cmap='coolwarm', ax=axis)
    axis.set_title('Target scores')
    axis.set_xticklabels(axis.get_xticklabels(),rotation=90)
    axis.set_yticklabels(axis.get_yticklabels(),rotation=0)
    # From here is image conversion
    plt.tight_layout()
    pngImage = BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    plt.close()

    return pngImageB64String

# Calculate the dendogram (return image)
def dendogram(rating_matrix):
    ''' This doesn't work yet.
    '''
    names_for_dendo = [session['role01'], session['role02'], session['role03'], session['role04'], session['role05'],
    session['role06'], session['role07'], session['role08'], session['role09'], session['role10'],
    session['role11'], session['role12'], session['role13'], session['role14'], session['role15']]
    Z = hierarchy.linkage(rating_matrix, 'average')
    fig = Figure(figsize=(7,7))
    axis = fig.add_subplot(1, 1, 1)
#    fig.subplots_adjust(bottom=0.5, left=0.5)
    hierarchy.dendrogram(Z, labels=names_for_dendo, leaf_rotation=90)
#    axis.set_xticklabels(axis.get_xticklabels(),rotation=90)
#    axis.set_yticklabels(axis.get_yticklabels(),rotation=0)
    # From here is image conversion
#    plt.show()
    pngImage = BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String
