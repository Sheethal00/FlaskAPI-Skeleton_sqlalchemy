from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Get_Post(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    status = db.Column(db.String(20))
    success = db.Column(db.Integer)
    data_key = db.Column(db.String(20))
    data_value = db.Column(db.String(20))
    return_code = db.Column(db.Integer)

    def __repr__(self):
        return ("({},{},{},{},{},{})".format(self.ID,self.status,self.success,self.data_key,self.data_value,self.return_code))

db.create_all()
obj = Get_Post(status = "success",success = 1,data_key = "Hello",data_value = "Hello Bro",return_code = 200)
db.session.add(obj)
db.session.commit()
