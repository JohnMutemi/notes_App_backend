from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import MetaData, Text

# Initialize SQLAlchemy with metadata convention for naming constraints
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

# Initialize SQLAlchemy with the custom metadata
db = SQLAlchemy(metadata=metadata)

# Define the Note model
class Note(db.Model, SerializerMixin):
    __tablename__ = 'note'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    module = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    subtopics = db.Column(JSON, nullable=True, default=[])  # JSON for storing structured data (e.g., list of subtopics)

    # Relationships
    comments = db.relationship(
        'Comment',
        back_populates='note',
        lazy='dynamic',  # Use 'dynamic' for query building
        cascade="all, delete-orphan"
    )

    # Serialization settings
    serialize_only = ('id', 'title', 'content', 'module', 'category', 'subtopics', 'comments')


# Define the Comment model
class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id', ondelete="CASCADE"), nullable=False)  # Add ondelete for cascade
    timestamp = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    # Relationships
    note = db.relationship('Note', back_populates='comments')

    # Serialization settings
    serialize_only = ('id', 'content', 'timestamp', 'note_id')
