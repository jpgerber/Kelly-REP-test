from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime

# Here I set a dictionary to make it easier to create the repeating variables

class SurveyData(Base):
    __tablename__ = 'SurveyData'
    id = Column(Integer,primary_key = True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    role01 = Column(Text)
    role02 = Column(Text)
    role03 = Column(Text)
    role04 = Column(Text)
    role05 = Column(Text)
    role06 = Column(Text)
    role07 = Column(Text)
    role08 = Column(Text)
    role09 = Column(Text)
    role10 = Column(Text)
    role11 = Column(Text)
    role12 = Column(Text)
    role13 = Column(Text)
    role14 = Column(Text)
    role15 = Column(Text)
    oddgoose01 = Column(Integer)
    construct1pos = Column(Text)
    construct1neg = Column(Text)
    oddgoose02 = Column(Integer)
    construct2pos = Column(Text)
    construct2neg = Column(Text)
    oddgoose03 = Column(Integer)
    construct3pos = Column(Text)
    construct3neg = Column(Text)
    oddgoose04 = Column(Integer)
    construct4pos = Column(Text)
    construct4neg = Column(Text)
    oddgoose05 = Column(Integer)
    construct5pos = Column(Text)
    construct5neg = Column(Text)
    oddgoose06 = Column(Integer)
    construct6pos = Column(Text)
    construct6neg = Column(Text)
    oddgoose07 = Column(Integer)
    construct7pos = Column(Text)
    construct7neg = Column(Text)
    oddgoose08 = Column(Integer)
    construct8pos = Column(Text)
    construct8neg = Column(Text)
    oddgoose09 = Column(Integer)
    construct9pos = Column(Text)
    construct9neg = Column(Text)
    oddgoose10 = Column(Integer)
    construct10pos = Column(Text)
    construct10neg = Column(Text)
    oddgoose11 = Column(Integer)
    construct11pos = Column(Text)
    construct11neg = Column(Text)
    oddgoose12 = Column(Integer)
    construct12pos = Column(Text)
    construct12neg = Column(Text)
    oddgoose13 = Column(Integer)
    construct13pos = Column(Text)
    construct13neg = Column(Text)
    oddgoose14 = Column(Integer)
    construct14pos = Column(Text)
    construct14neg = Column(Text)
    oddgoose15 = Column(Integer)
    construct15pos = Column(Text)
    construct15neg = Column(Text)
    rating_p1_const1 = Column(Integer)
    rating_p1_const2 = Column(Integer)
    rating_p1_const3 = Column(Integer)
    rating_p1_const4 = Column(Integer)
    rating_p1_const5 = Column(Integer)
    rating_p1_const6 = Column(Integer)
    rating_p1_const7 = Column(Integer)
    rating_p1_const8 = Column(Integer)
    rating_p1_const9 = Column(Integer)
    rating_p1_const10 = Column(Integer)
    rating_p1_const11 = Column(Integer)
    rating_p1_const12 = Column(Integer)
    rating_p1_const13 = Column(Integer)
    rating_p1_const14 = Column(Integer)
    rating_p1_const15 = Column(Integer)
    rating_p2_const1 = Column(Integer)
    rating_p2_const2 = Column(Integer)
    rating_p2_const3 = Column(Integer)
    rating_p2_const4 = Column(Integer)
    rating_p2_const5 = Column(Integer)
    rating_p2_const6 = Column(Integer)
    rating_p2_const7 = Column(Integer)
    rating_p2_const8 = Column(Integer)
    rating_p2_const9 = Column(Integer)
    rating_p2_const10 = Column(Integer)
    rating_p2_const11 = Column(Integer)
    rating_p2_const12 = Column(Integer)
    rating_p2_const13 = Column(Integer)
    rating_p2_const14 = Column(Integer)
    rating_p2_const15 = Column(Integer)
    rating_p3_const1 = Column(Integer)
    rating_p3_const2 = Column(Integer)
    rating_p3_const3 = Column(Integer)
    rating_p3_const4 = Column(Integer)
    rating_p3_const5 = Column(Integer)
    rating_p3_const6 = Column(Integer)
    rating_p3_const7 = Column(Integer)
    rating_p3_const8 = Column(Integer)
    rating_p3_const9 = Column(Integer)
    rating_p3_const10 = Column(Integer)
    rating_p3_const11 = Column(Integer)
    rating_p3_const12 = Column(Integer)
    rating_p3_const13 = Column(Integer)
    rating_p3_const14 = Column(Integer)
    rating_p3_const15 = Column(Integer)
    rating_p4_const1 = Column(Integer)
    rating_p4_const2 = Column(Integer)
    rating_p4_const3 = Column(Integer)
    rating_p4_const4 = Column(Integer)
    rating_p4_const5 = Column(Integer)
    rating_p4_const6 = Column(Integer)
    rating_p4_const7 = Column(Integer)
    rating_p4_const8 = Column(Integer)
    rating_p4_const9 = Column(Integer)
    rating_p4_const10 = Column(Integer)
    rating_p4_const11 = Column(Integer)
    rating_p4_const12 = Column(Integer)
    rating_p4_const13 = Column(Integer)
    rating_p4_const14 = Column(Integer)
    rating_p4_const15 = Column(Integer)
    rating_p5_const1 = Column(Integer)
    rating_p5_const2 = Column(Integer)
    rating_p5_const3 = Column(Integer)
    rating_p5_const4 = Column(Integer)
    rating_p5_const5 = Column(Integer)
    rating_p5_const6 = Column(Integer)
    rating_p5_const7 = Column(Integer)
    rating_p5_const8 = Column(Integer)
    rating_p5_const9 = Column(Integer)
    rating_p5_const10 = Column(Integer)
    rating_p5_const11 = Column(Integer)
    rating_p5_const12 = Column(Integer)
    rating_p5_const13 = Column(Integer)
    rating_p5_const14 = Column(Integer)
    rating_p5_const15 = Column(Integer)
    rating_p6_const1 = Column(Integer)
    rating_p6_const2 = Column(Integer)
    rating_p6_const3 = Column(Integer)
    rating_p6_const4 = Column(Integer)
    rating_p6_const5 = Column(Integer)
    rating_p6_const6 = Column(Integer)
    rating_p6_const7 = Column(Integer)
    rating_p6_const8 = Column(Integer)
    rating_p6_const9 = Column(Integer)
    rating_p6_const10 = Column(Integer)
    rating_p6_const11 = Column(Integer)
    rating_p6_const12 = Column(Integer)
    rating_p6_const13 = Column(Integer)
    rating_p6_const14 = Column(Integer)
    rating_p6_const15 = Column(Integer)
    rating_p7_const1 = Column(Integer)
    rating_p7_const2 = Column(Integer)
    rating_p7_const3 = Column(Integer)
    rating_p7_const4 = Column(Integer)
    rating_p7_const5 = Column(Integer)
    rating_p7_const6 = Column(Integer)
    rating_p7_const7 = Column(Integer)
    rating_p7_const8 = Column(Integer)
    rating_p7_const9 = Column(Integer)
    rating_p7_const10 = Column(Integer)
    rating_p7_const11 = Column(Integer)
    rating_p7_const12 = Column(Integer)
    rating_p7_const13 = Column(Integer)
    rating_p7_const14 = Column(Integer)
    rating_p7_const15 = Column(Integer)
    rating_p8_const1 = Column(Integer)
    rating_p8_const2 = Column(Integer)
    rating_p8_const3 = Column(Integer)
    rating_p8_const4 = Column(Integer)
    rating_p8_const5 = Column(Integer)
    rating_p8_const6 = Column(Integer)
    rating_p8_const7 = Column(Integer)
    rating_p8_const8 = Column(Integer)
    rating_p8_const9 = Column(Integer)
    rating_p8_const10 = Column(Integer)
    rating_p8_const11 = Column(Integer)
    rating_p8_const12 = Column(Integer)
    rating_p8_const13 = Column(Integer)
    rating_p8_const14 = Column(Integer)
    rating_p8_const15 = Column(Integer)
    rating_p9_const1 = Column(Integer)
    rating_p9_const2 = Column(Integer)
    rating_p9_const3 = Column(Integer)
    rating_p9_const4 = Column(Integer)
    rating_p9_const5 = Column(Integer)
    rating_p9_const6 = Column(Integer)
    rating_p9_const7 = Column(Integer)
    rating_p9_const8 = Column(Integer)
    rating_p9_const9 = Column(Integer)
    rating_p9_const10 = Column(Integer)
    rating_p9_const11 = Column(Integer)
    rating_p9_const12 = Column(Integer)
    rating_p9_const13 = Column(Integer)
    rating_p9_const14 = Column(Integer)
    rating_p9_const15 = Column(Integer)
    rating_p10_const1 = Column(Integer)
    rating_p10_const2 = Column(Integer)
    rating_p10_const3 = Column(Integer)
    rating_p10_const4 = Column(Integer)
    rating_p10_const5 = Column(Integer)
    rating_p10_const6 = Column(Integer)
    rating_p10_const7 = Column(Integer)
    rating_p10_const8 = Column(Integer)
    rating_p10_const9 = Column(Integer)
    rating_p10_const10 = Column(Integer)
    rating_p10_const11 = Column(Integer)
    rating_p10_const12 = Column(Integer)
    rating_p10_const13 = Column(Integer)
    rating_p10_const14 = Column(Integer)
    rating_p10_const15 = Column(Integer)
    rating_p11_const1 = Column(Integer)
    rating_p11_const2 = Column(Integer)
    rating_p11_const3 = Column(Integer)
    rating_p11_const4 = Column(Integer)
    rating_p11_const5 = Column(Integer)
    rating_p11_const6 = Column(Integer)
    rating_p11_const7 = Column(Integer)
    rating_p11_const8 = Column(Integer)
    rating_p11_const9 = Column(Integer)
    rating_p11_const10 = Column(Integer)
    rating_p11_const11 = Column(Integer)
    rating_p11_const12 = Column(Integer)
    rating_p11_const13 = Column(Integer)
    rating_p11_const14 = Column(Integer)
    rating_p11_const15 = Column(Integer)
    rating_p12_const1 = Column(Integer)
    rating_p12_const2 = Column(Integer)
    rating_p12_const3 = Column(Integer)
    rating_p12_const4 = Column(Integer)
    rating_p12_const5 = Column(Integer)
    rating_p12_const6 = Column(Integer)
    rating_p12_const7 = Column(Integer)
    rating_p12_const8 = Column(Integer)
    rating_p12_const9 = Column(Integer)
    rating_p12_const10 = Column(Integer)
    rating_p12_const11 = Column(Integer)
    rating_p12_const12 = Column(Integer)
    rating_p12_const13 = Column(Integer)
    rating_p12_const14 = Column(Integer)
    rating_p12_const15 = Column(Integer)
    rating_p13_const1 = Column(Integer)
    rating_p13_const2 = Column(Integer)
    rating_p13_const3 = Column(Integer)
    rating_p13_const4 = Column(Integer)
    rating_p13_const5 = Column(Integer)
    rating_p13_const6 = Column(Integer)
    rating_p13_const7 = Column(Integer)
    rating_p13_const8 = Column(Integer)
    rating_p13_const9 = Column(Integer)
    rating_p13_const10 = Column(Integer)
    rating_p13_const11 = Column(Integer)
    rating_p13_const12 = Column(Integer)
    rating_p13_const13 = Column(Integer)
    rating_p13_const14 = Column(Integer)
    rating_p13_const15 = Column(Integer)
    rating_p14_const1 = Column(Integer)
    rating_p14_const2 = Column(Integer)
    rating_p14_const3 = Column(Integer)
    rating_p14_const4 = Column(Integer)
    rating_p14_const5 = Column(Integer)
    rating_p14_const6 = Column(Integer)
    rating_p14_const7 = Column(Integer)
    rating_p14_const8 = Column(Integer)
    rating_p14_const9 = Column(Integer)
    rating_p14_const10 = Column(Integer)
    rating_p14_const11 = Column(Integer)
    rating_p14_const12 = Column(Integer)
    rating_p14_const13 = Column(Integer)
    rating_p14_const14 = Column(Integer)
    rating_p14_const15 = Column(Integer)
    rating_p15_const1 = Column(Integer)
    rating_p15_const2 = Column(Integer)
    rating_p15_const3 = Column(Integer)
    rating_p15_const4 = Column(Integer)
    rating_p15_const5 = Column(Integer)
    rating_p15_const6 = Column(Integer)
    rating_p15_const7 = Column(Integer)
    rating_p15_const8 = Column(Integer)
    rating_p15_const9 = Column(Integer)
    rating_p15_const10 = Column(Integer)
    rating_p15_const11 = Column(Integer)
    rating_p15_const12 = Column(Integer)
    rating_p15_const13 = Column(Integer)
    rating_p15_const14 = Column(Integer)
    rating_p15_const15 = Column(Integer)
    rating_p16_const1 = Column(Integer)
    rating_p16_const2 = Column(Integer)
    rating_p16_const3 = Column(Integer)
    rating_p16_const4 = Column(Integer)
    rating_p16_const5 = Column(Integer)
    rating_p16_const6 = Column(Integer)
    rating_p16_const7 = Column(Integer)
    rating_p16_const8 = Column(Integer)
    rating_p16_const9 = Column(Integer)
    rating_p16_const10 = Column(Integer)
    rating_p16_const11 = Column(Integer)
    rating_p16_const12 = Column(Integer)
    rating_p16_const13 = Column(Integer)
    rating_p16_const14 = Column(Integer)
    rating_p16_const15 = Column(Integer)
#    rating_p2_const1 = Column(Integer)
#    rating_p2_const2 = Column(Integer)
    # Then I use the dictionary to make the repeated variables
#    rating_var_names = {'self.rating_p{}_const{}'.format(i+1, j+1) : ' rating_p{}_const{}'.format(i+1, j+1) for i in range(15) for j in range(15)}
#    for val in rating_var_names:
#        rating_var_names[val] = Column(Integer)

# Initialize all the variables on creation of the user
#    var_list = 'self, timestamp, role01, role02, role03, role04, role05, role06, role07, role08, role09, role10, role11, role12, role13, role14, role15, oddgoose01, construct1pos, construct1neg, oddgoose02, construct2pos, construct2neg, oddgoose03, construct3pos, construct3neg, oddgoose04, construct4pos, construct4neg, oddgoose05, construct5pos, construct5neg, oddgoose06, construct6pos, construct6neg, oddgoose07, construct7pos, construct7neg, oddgoose08, construct8pos, construct8neg, #oddgoose09, construct9pos, construct9neg, oddgoose10, construct10pos, construct10neg, oddgoose11, construct11pos, construct11neg, oddgoose12, construct12pos, construct12neg, oddgoose13, construct13pos, construct13neg, oddgoose14, construct14pos, construct14neg, oddgoose15, construct15pos, construct15neg, rating_p1_const1, rating_p1_const2, rating_p2_const1, rating_p2_const2'

    def __init__(self, **kwargs):
            super(SurveyData, self).__init__(**kwargs)
    def __repr__(self):
        return '<User {}>'.format(self.role01)


#    def __init__(self, timestamp, role01, role02, role03, role04, role05, role06, role07, role08, role09, role10, role11, role12, role13, role14, role15, oddgoose01, construct1pos, construct1neg, oddgoose02, construct2pos, construct2neg, oddgoose03, construct3pos, construct3neg, oddgoose04, construct4pos, construct4neg, oddgoose05, construct5pos, construct5neg, oddgoose06, construct6pos, construct6neg, oddgoose07, construct7pos, construct7neg, oddgoose08, construct8pos, construct8neg, oddgoose09, construct9pos, construct9neg, oddgoose10, construct10pos, construct10neg, oddgoose11, construct11pos, construct11neg, oddgoose12, construct12pos, construct12neg, oddgoose13, construct13pos, construct13neg, oddgoose14, construct14pos, construct14neg, oddgoose15, construct15pos, construct15neg, rating_p1_const1, rating_p1_const2, rating_p2_const1, rating_p2_const2):
#        self.timestamp = timestamp
#        self.role01 = role01
#        self.role02 = role02
#        self.role03 = role03
#        self.role04 = role04
#        self.role05 = role05
#        self.role06 = role06
#        self.role07 = role07
'''        self.role08 = role08
        self.role09 = role09
        self.role10 = role10
        self.role11 = role11
        self.role12 = role12
        self.role13 = role13
        self.role14 = role14
        self.role15 = role15
        self.oddgoose01 = oddgoose01
        self.construct1pos = construct1pos
        self.construct1neg = construct1neg
        self.oddgoose02 = oddgoose02
        self.construct2pos = construct2pos
        self.construct2neg = construct2neg
        self.oddgoose03 = oddgoose03
        self.construct3pos = construct4pos
        self.construct3neg = construct4neg
        self.oddgoose04 = oddgoose04
        self.construct4pos = construct4pos
        self.construct4neg = construct4neg
        self.oddgoose05 = oddgoose05
        self.construct5pos = construct5pos
        self.construct5neg = construct5neg
        self.oddgoose06 = oddgoose06
        self.construct6pos = construct6pos
        self.construct6neg = construct6neg
        self.oddgoose07 = oddgoose07
        self.construct7pos = construct7pos
        self.construct7neg = construct7neg
        self.oddgoose08 = oddgoose08
        self.construct8pos = construct8pos
        self.construct8neg = construct8neg
        self.oddgoose09 = oddgoose09
        self.construct9pos = construct9pos
        self.construct9neg = construct9neg
        self.oddgoose10 = oddgoose10
        self.construct10pos = construct10pos
        self.construct10neg = construct10neg
        self.oddgoose11 = oddgoose11
        self.construct11pos = construct11pos
        self.construct11neg = construct11neg
        self.oddgoose12 = oddgoose12
        self.construct12pos = construct12pos
        self.construct12neg = construct12neg
        self.oddgoose13 = oddgoose13
        self.construct13pos = construct13pos
        self.construct13neg = construct13neg
        self.oddgoose14 = oddgoose14
        self.construct14pos = construct14pos
        self.construct14neg = construct14neg
        self.oddgoose15 = oddgoose15
        self.construct15pos = construct15pos
        self.construct15neg = construct15neg
#        for val in rating_var_names:
#            val = rating_var_names[val]
#        self.rating_p1_const1 = rating_p1_const1
#        self.rating_p1_const2 = rating_p1_const2
#        self.rating_p2_const1 = rating_p2_const1
#        self.rating_p2_const2 = rating_p2_const2'''
