from extensions import db

class Faculty(db.Model):
    __tablename__ = 'faculty'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    department = db.Column(db.String(100))
    position = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<Faculty {self.id}>'