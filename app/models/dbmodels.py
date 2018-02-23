from .. import db

class Funds(db.Model):
    __tablename__ = 'funds'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), index=True) 
    quote = db.Column(db.Float)
    quote_date = db.Column(db.Date)

    def to_dict(self):
        return {
                'id': self.id,
                'code': self.code
                }
