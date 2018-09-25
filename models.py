from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class MasukanRate(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key = True)

    cur_From = db.Column(db.String, nullable = False)
    cur_To = db.Column(db.String, nullable = False)
    cur_Rate = db.Column(db.Float, nullable = False)

    cur_Date = db.Column(db.DateTime, nullable = False, default = datetime.strftime(datetime.today(), "%b %d %Y"))

    def __init__(self,cur_From,cur_To,cur_Date,cur_Rate):
        self.cur_From = cur_From
        self.cur_To = cur_To
        self.cur_Date = cur_Date
        self.cur_Rate =cur_Rate

    def __repr__(self):
        return '%s%s%s%s' %(self.cur_From,self.cur_To,self.cur_Date,self.cur_Rate)

    

class ExchangeRate(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key = True)

    cur_From = db.Column(db.String, nullable = False)
    cur_To = db.Column(db.String, nullable = False)
    cur_Rate = db.Column(db.Float, nullable = False)
    cur_avg_Rate = db.Column(db.Float, nullable = False)
    cur_Date = db.Column(db.DateTime, nullable = False, default = datetime.strftime(datetime.today(), "%b %d %Y"))

    def __init__(self,cur_From,cur_To,cur_Date,cur_avg_Rate,cur_Rate):
        self.cur_From = cur_From
        self.cur_To = cur_To
        self.cur_Date = cur_Date
        self.cur_avg_Rate = cur_avg_Rate
        self.cur_Rate =cur_Rate
        
    def __repr__(self):
        return '<From %r>' % self.cur_From

