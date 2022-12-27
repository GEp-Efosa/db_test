from .extensions import db

class DbTest(db.Model):
    __tablename__ = "db_test"

    id = db.Column(db.Integer, primary_key=True)
    float_field = db.Column(db.Float, nullable=True)
    string_field = db.Column(db.String(120), nullable=True)
    integer_field = db.Column(db.Integer, nullable=True)

    # Create an index on the name column in descending order
    __table_args__ = (
        db.Index('idx_id', id),
    )
    

    def save(self):
        db.session.add(self)
        db.session.commit()
        