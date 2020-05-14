# This module contains some functions that helped me test my app.

# Database tests.

def check_contents_of_database(*field_to_display):
    '''This function returns the current contents of specified fields in the database'''
    print(field_to_display)
    fields_list = ['u.'+field for field in field_to_display]
#    print(fields_list)
#    print(u for u in fields_list)
    test_get = SurveyData.query.all()
    for u in test_get:
        for field in fields_list:
            print(field)


#check_contents_of_database('ace', 'base')

def field_updater(dictionary_of_databasefields_and_formfields):
    ''' This function takes a dictionary of database and form  key-value pairs
    and uses them to update the most recent user's values in the database. For example,
    inputting {'oddgoose01':'role01'} would update the database field oddgoose01 with the
    field role01 from the HTML form.'''
        user_to_update = db_session.query(SurveyData).order_by(SurveyData.id.desc()).first()
# For each key-value pair, we go
        for pair in dictionary_of_databasefields_and_formfields:
            user_to_update.pair = session.get(str(pair[i])
        # Add + commit the new data
        db_session.add(user_to_update)
        db_session.commit()


# Checking the last updated values
user_updated = db_session.query(SurveyData).order_by(SurveyData.id.desc()).first()
        print(user_updated.construct1pos)
#
