from app import app, db
from models import Note, Comment

# Sample data to seed
notes = [
    {
        "title": "Introduction to HTML",
        "subtopics": "What is HTML?",
        "content": "HTML (Hypertext Markup Language) is the foundational language of the web. It is the standard markup language used to create the structure of web pages and web applications. Through HTML, developers can define elements such as headings, paragraphs, links, images, and multimedia, which make up the content of a webpage. HTML plays a critical role in search engine optimization (SEO) and web accessibility, ensuring that web content is structured in a way that is both user-friendly and search engine-friendly.",
        "module": "HTML",
        "category": "Basics"
    },
  
    {
        "title": "Python Basics",
        "subtopics": "What is Python?",
        "content": "Python is one of the most popular and versatile programming languages used in a variety of domains, from web development to data science, machine learning, automation, and more. Known for its readability and simplicity, Python has become the language of choice for both beginners and professionals alike. Python boasts a rich ecosystem of libraries and frameworks, such as Django for web development and TensorFlow for machine learning.",
        "module": "Python",
        "category": "Basics"
    },
    
    {
        "title": "React Basics",
        "subtopics": "What is React?",
        "content": "React is a JavaScript library for building user interfaces, particularly for single-page applications (SPAs) where the content dynamically updates without reloading the page. React allows developers to build reusable UI components and manage the state of these components efficiently. React uses a virtual DOM to optimize performance by updating only the parts of the web page that change.",
        "module": "React",
        "category": "Basics"
    },
 
    {
        "title": "Introduction to JavaScript",
        "subtopics": "What is JavaScript?",
        "content": "JavaScript is a versatile and essential programming language that powers the interactivity of websites and web applications. JavaScript enables developers to create interactive features like form validation, animations, and real-time updates. As a core technology alongside HTML and CSS, JavaScript is essential for front-end web development. Over the years, JavaScript has evolved into a powerful tool for full-stack development, enabling server-side capabilities with Node.js.",
        "module": "JavaScript",
        "category": "Basics"
    },

    {
        "title": "Introduction to Flask",
        "subtopics": "What is Flask?",
        "content": "Flask is a lightweight and flexible web framework for Python that allows developers to quickly build web applications. Flask is designed to be simple and easy to use, providing the essentials for web development without additional overhead. Despite its simplicity, Flask is highly extensible with a rich ecosystem of extensions for things like authentication and database integration. Flask is ideal for small to medium-sized applications, APIs, or microservices, and is great for rapid prototyping.",
        "module": "Flask",
        "category": "Back-End"
    },
]



# Sample comments for each note
comments = [
    {
        "note_id": 1,
        "content": "Great introduction to HTML!"
    },
    {
        "note_id": 1,
        "content": "I really liked the examples you used."
    },
    {
        "note_id": 2,
        "content": "Python is awesome, great explanation!"
    },
    {
        "note_id": 3,
        "content": "React is so fun to work with. Thanks for this guide!"
    }
]

def seed_data():
    with app.app_context():
        # Drop all tables (if any) and recreate them
        db.drop_all()
        db.create_all()

        # Insert sample data for notes
        for note_data in notes:
            note = Note(**note_data)
            db.session.add(note)
        
        db.session.commit()
        print("Notes data seeded successfully!")

        # Insert sample comments for each note
        for comment_data in comments:
            comment = Comment(**comment_data)
            db.session.add(comment)

        db.session.commit()
        print("Comments data seeded successfully!")

if __name__ == "__main__":
    seed_data()
