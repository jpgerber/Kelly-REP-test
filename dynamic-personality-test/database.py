from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

engine = create_engine(DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

#Session = sessionmaker(bind=engine)
#db = SQLAlchemy()

def init_db():
    # import models modules here
    import models
    Base.metadata.create_all(bind=engine)



#def add_data_to_record(pairs_list**):
#    '''This function takes variable inputs and outputs and then updates the selected database
#    fields for the current user. Data should be entered as strings of form SurveyData.'''
    # Retrieve the current user

    # Update with new fields

#        user_data_odd1 = SurveyData(oddgoose01=form.oddoneout.data)
#        db_session.add(user_data_odd1)
#        db_session.commit()
