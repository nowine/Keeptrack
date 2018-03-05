from .. import db

class Funds(db.Model):
    __tablename__ = 'funds'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), index=True) 
    quote = db.Column(db.Numeric(precision=4))
    absquote = db.Column(db.Numeric(precision=4))
    quote_date = db.Column(db.Date)
    rate = db.Column(db.Numeric(precision=4))
    name = db.Column(db.Unicode(30))

    def to_dict(self):
        return {
                'id': self.id,
                'code': self.code,
                'quote': self.quote,
                'quote_date': self.quote_date,
                'rate': self.rate,
                'name': self.name
                }


class FundPriceHistory(db.Model):
    __tablename__ = 'fund_price_hist'
    id = db.Column(db.Integer, primary_key=True)
    fund_id = db.Column(db.Integer, db.ForeignKey('funds.id'))
    fund = db.relationship('Funds')
    quote = db.Column(db.Numeric(precision=4))
    absquote = db.Column(db.Numeric(precision=4))
    rate = db.Column(db.Numeric(precision=4))
    quote_date = db.Column(db.Date)
    
    def to_dict(self):
        return {
                'fund': self.fund.code,
                'quote': self.quote,
                'absquote': self.absquote,
                'rate': self.rate,
                'quote_date': self.quote_date
                }


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(50), index=True)

    def to_dict(self):
        return {
                'name': self.name,
                }


class Holdings(db.Model):
    __tablename__ = 'holdings'
    id = db.Column(db.Integer, primary_key=True)
    fund_id = db.Column(db.Integer, db.ForeignKey('funds.id'))
    fund = db.relationship('Funds')
    quote = db.Column(db.Numeric(precision=4))
    
    def to_dict(self):
        return {
                'name': self.name,
                }
