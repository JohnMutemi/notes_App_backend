from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize SQLAlchemy first
db = SQLAlchemy()

# Metadata convention
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# Define the metadata after db initialization
metadata = db.MetaData(naming_convention=convention)

# Now initialize SQLAlchemy with the metadata
db = SQLAlchemy(metadata=metadata)


class Note(db.Model, SerializerMixin):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    module = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=True)

    # Bidirectional relationship with Comment
    comments = db.relationship(
        'Comment',
        back_populates='note',
        lazy=True,
        cascade="all, delete-orphan"
    )

    serialize_only = ('id', 'title', 'content', 'module', 'category', 'comments')


class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    # Reference back to Note
    note = db.relationship('Note', back_populates='comments')

    serialize_only = ('id', 'content', 'timestamp', 'note_id')
