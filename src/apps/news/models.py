from slugify import slugify

from src.extensions import db
from src.models import Base


class News(Base):
    __tablename__ = "news"

    title = db.Column(db.String(100), nullable=False, index=True)
    slug = db.Column(db.String(100), index=True)
    content = db.Column(db.Text)

    tags = db.relationship("Tag", backref="news", lazy=True)

    def __repr__(self):
        return f"<News {self.title}>"

    def set_slug(self):
        self.slug = slugify(self.title)

    def save(self):
        self.set_slug()
        return super().save()


class Tag(Base):
    __tablename__ = "tags"

    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    news = db.relationship("News", backref="tags", lazy=True)

    def __repr__(self):
        return f"<Tag {self.name}>"

    def set_slug(self):
        self.slug = slugify(self.name)

    def save(self):
        self.set_slug()
        return super().save()
