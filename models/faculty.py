from extensions import db

class Faculty(db.Model):
    __tablename__ = 'faculty'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)  # Changed to match User tablename
    department = db.Column(db.String(100))
    position = db.Column(db.String(100))
    
    # Add relationship to User
    user = db.relationship('User', backref=db.backref('faculty', uselist=False))
    
    def __repr__(self):
        return f'<Faculty {self.id}>'