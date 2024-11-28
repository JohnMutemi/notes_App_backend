from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db, Note, Comment
from config import Config
from flask_cors import CORS
import os

# Initialize the Flask application
app = Flask(__name__)

app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
CORS(app, resources={r"/*": {
    "origins": "*",  # Allows all origins
    "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    "allow_headers": "*"
}})


# Initialize the database and migration tool
from models import db, Note, Comment
db.init_app(app)
migrate = Migrate(app, db)

# Initialize the API
api = Api(app)

# Predefined list of allowed modules
ALLOWED_MODULES = ["HTML", "CSS", "JavaScript", "Python", "Flask", "React"]

class NotesResource(Resource):
    def post(self, module):
        """Create a new note with a specified module"""
        print(f"POST request received for module: {module}")

        # Ensure that the module is in the allowed modules list
        if module not in ALLOWED_MODULES:
            print(f"Invalid module: {module}. Allowed modules are {ALLOWED_MODULES}.")
            return {'message': f'Invalid module. Allowed modules are {ALLOWED_MODULES}.'}, 400

        data = None

        # Handle both JSON and FormData (multipart/form-data)
        if request.is_json:
            data = request.get_json()
            print(f"Received JSON data: {data}")
        elif request.form:
            data = request.form.to_dict()
            print(f"Received form data: {data}")
        else:
            print("Invalid data format. Expected JSON or FormData.")
            return {'message': 'Invalid data format. Expected JSON or FormData.'}, 400

        # Ensure only title and content are required
        title = data.get('title')
        content = data.get('content')
        subtopics = data.get('subtopics')

        if not title or not content or not subtopics:
            print("Missing title or content or subtopic.")
            return {'message': 'Title, Subtopic and content are required.'}, 400

        # Create new note with predefined module value from the URL parameter
        note = Note(title=title, subtopics=subtopics, content=content, module=module)
        print(f"New note created with title: {title}, subtopics:{subtopics},content: {content}, module: {module}")

        db.session.add(note)
        db.session.commit()
        print(f"Note with ID {note.id} saved to the database.")

        return note.to_dict(), 201

    def get(self, module):
        """Retrieve all notes for a specific module"""
        print(f"GET request received for module: {module}")

        if module not in ALLOWED_MODULES:
            print(f"Invalid module: {module}. Allowed modules are {ALLOWED_MODULES}.")
            return {'message': f'Invalid module. Allowed modules are {ALLOWED_MODULES}.'}, 400
        
        notes = Note.query.filter_by(module=module).all()
        print(f"Found {len(notes)} notes for module: {module}")
        return [note.to_dict() for note in notes], 200

    def patch(self, module, note_id):
        """Update an existing note"""
        print(f"PATCH request received for module: {module}, note_id: {note_id}")

        if module not in ALLOWED_MODULES:
            print(f"Invalid module: {module}. Allowed modules are {ALLOWED_MODULES}.")
            return {'message': f'Invalid module. Allowed modules are {ALLOWED_MODULES}.'}, 400

        data = None

        # Handle both JSON and FormData (multipart/form-data)
        if request.is_json:
            data = request.get_json()
            print(f"Received JSON data: {data}")
        elif request.form:
            data = request.form.to_dict()
            print(f"Received form data: {data}")
        else:
            print("Invalid data format. Expected JSON or FormData.")
            return {'message': 'Invalid data format. Expected JSON or FormData.'}, 400

        # Fetch the note by ID
        note = Note.query.get(note_id)
        if not note:
            print(f"Note with ID {note_id} not found.")
            return {'message': 'Note not found.'}, 404

        # Update the fields if they are present in the request
        title = data.get('title')
        content = data.get('content')
        subtopics = data.get('subtopics')

        if title:
            note.title = title
        if content:
            note.content = content
        if subtopics:
            note.subtopics = subtopics

        print(f"Updating note with ID {note_id}: title={note.title}, subtopics={note.subtopics}, content={note.content}")
        db.session.commit()
        print(f"Note with ID {note_id} updated successfully.")

        return note.to_dict(), 200


class SingleNoteResource(Resource):
    def get(self, note_id):
        """Get a single note by ID"""
        print(f"GET request received for note ID: {note_id}")  # Debugging print statement

        note = Note.query.get_or_404(note_id)
        print(f"Found note: {note.title}")  # Debugging print statement
        return note.to_dict(), 200

    def put(self, note_id):
        """Update a note by ID"""
        print(f"PUT request received for note ID: {note_id}")  # Debugging print statement
        note = Note.query.get_or_404(note_id)
        data = None

        # Handle both JSON and FormData (multipart/form-data)
        if request.is_json:
            data = request.get_json()
            print(f"Received JSON data: {data}")  # Debugging print statement
        elif request.form:
            data = request.form.to_dict()
            print(f"Received form data: {data}")  # Debugging print statement
        else:
            print("Invalid data format. Expected JSON or FormData.")  # Debugging print statement
            return {'message': 'Invalid data format. Expected JSON or FormData.'}, 400


        # Update only title,and content (module is predefined, category is not needed)
        note.title = data.get('title', note.title)
        note.subtopics = data.get('subtopics', note.subtopics)
        note.content = data.get('content', note.content)


        db.session.commit()
        print(f"Note with ID {note.id} updated.")  # Debugging print statement

        return note.to_dict(), 200

    def delete(self, note_id):
        """Delete a note by ID"""
        print(f"DELETE request received for note ID: {note_id}")  # Debugging print statement

        note = Note.query.get_or_404(note_id)
        db.session.delete(note)
        db.session.commit()
        print(f"Note with ID {note.id} deleted.")  # Debugging print statement

        return {"message": "Note deleted successfully"}, 204
    
class CommentResource(Resource):
    def post(self, note_id):
        """Create a new comment for a specific note"""
        print(f"POST request received for note ID: {note_id}")  # Debugging print statement

        # Ensure the note exists
        note = Note.query.get_or_404(note_id)

        # Handle both JSON and FormData (multipart/form-data)
        data = None
        if request.is_json:
            data = request.get_json()
            print(f"Received JSON data: {data}")  # Debugging print statement
        elif request.form:
            data = request.form.to_dict()
            print(f"Received form data: {data}")  # Debugging print statement
        else:
            print("Invalid data format. Expected JSON or FormData.")  # Debugging print statement
            return {'message': 'Invalid data format. Expected JSON or FormData.'}, 400

        # Ensure the comment content is provided
        content = data.get('content')
        if not content:
            print("Missing content for the comment.")  # Debugging print statement
            return {'message': 'Content is required for the comment.'}, 400

        # Create the new comment
        comment = Comment(content=content, note_id=note.id)
        print(f"New comment created for note ID {note_id} with content: {content}")  # Debugging print statement

        db.session.add(comment)
        db.session.commit()
        print(f"Comment with ID {comment.id} saved to the database.")  # Debugging print statement

        return comment.to_dict(), 201

    def get(self, note_id):
        """Get all comments for a specific note"""
        print(f"GET request received for note ID: {note_id}")  # Debugging print statement

        # Ensure the note exists
        note = Note.query.get_or_404(note_id)

        # Fetch all comments for the note
        comments = Comment.query.filter_by(note_id=note.id).all()

        # Return the comments as a list of dictionaries
        return [comment.to_dict() for comment in comments], 200

# Add the new resource to the API
api.add_resource(CommentResource, '/notes/<int:note_id>/comments')
api.add_resource(NotesResource, '/notes/<string:module>', '/notes/<string:module>/<int:note_id>')  # Handle notes by module and note_id
api.add_resource(SingleNoteResource, '/notes/<int:note_id>')  # For operations on a single note by ID

if __name__ == '__main__':
    app.run(port=5555, debug=True)
