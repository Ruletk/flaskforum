from app.src.utils.decorators.database import clear_session, rollback_session
from app.src.extensions import db


class Base(db.Model):
    __abstract__ = True
    json_attributes = ()

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    @rollback_session
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **attributes):
        for key, value in attributes.items():
            setattr(self, key, value)
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_json(self):
        return {key: getattr(self, key) for key in self.json_attributes}

    def change_value(self, column, value=1):
        self.update({column: getattr(self, column, 0) + value})


from .user import User
