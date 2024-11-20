from app import app, db
from models import Note, Comment

# Sample data to seed
notes = [
    {
        "title": "Introduction to HTML",
        "content": "HTML (Hypertext Markup Language) is the foundational language of the web. It is the standard markup language used to create the structure of web pages and web applications. Through HTML, developers can define elements such as headings, paragraphs, links, images, and multimedia, which make up the content of a webpage. Understanding HTML is the first step toward becoming a web developer, as it forms the skeleton upon which the styling (CSS) and behavior (JavaScript) are built. HTML also plays a critical role in search engine optimization (SEO) and web accessibility, ensuring that web content is structured in a way that is both user-friendly and search engine-friendly. With HTML, the possibilities are endless, as it serves as the basis for everything we see and interact with on the web today.",
        "module": "HTML",
        "category": "Basics"
    },
    {
        "title": "Python Basics",
        "content": "Python is one of the most popular and versatile programming languages used in a variety of domains, from web development to data science, machine learning, automation, and more. Known for its readability and simplicity, Python has become the language of choice for both beginners and professionals alike. Its clear syntax allows developers to express concepts in fewer lines of code compared to other programming languages. Python also boasts a rich ecosystem of libraries and frameworks, such as Django for web development and TensorFlow for machine learning, that make it an excellent choice for rapid development and prototyping. Whether you're building complex applications or performing simple tasks, Python's vast community and resources ensure that it's an invaluable tool for anyone looking to dive into the world of programming.",
        "module": "Python",
        "category": "Basics"
    },
    {
        "title": "React Basics",
        "content": "React is a powerful JavaScript library for building user interfaces, particularly for single-page applications (SPAs) where the content dynamically updates without reloading the page. Developed by Facebook, React has revolutionized front-end development by allowing developers to build reusable UI components and manage the state of these components efficiently. With its virtual DOM (Document Object Model), React can update only the parts of the web page that change, improving performance and responsiveness. React's component-based architecture allows developers to break down complex interfaces into manageable, isolated pieces, which can be reused throughout the application. As the foundation for modern web development, React has become one of the most sought-after skills in the industry, powering the interfaces of popular websites and applications like Instagram, Airbnb, and Netflix. Whether you're building a simple blog or a complex enterprise-level application, React provides the tools and flexibility needed to create dynamic, high-performance user experiences.",
        "module": "React",
        "category": "Basics"
    },
    {
        "title": "Introduction to JavaScript",
        "content": "JavaScript is a versatile and essential programming language that powers the interactivity of websites and web applications. Originally developed to add dynamic behavior to web pages, JavaScript enables developers to create interactive features like form validation, animations, and real-time updates. As one of the core technologies of the web, along with HTML and CSS, JavaScript runs on the client-side in web browsers, making it an essential skill for front-end developers. With its ability to interact with HTML and CSS, JavaScript brings web pages to life, creating a more engaging user experience. Over the years, JavaScript has evolved into a powerful tool for full-stack development, with frameworks like Node.js enabling it to run on the server-side as well. Whether you are building a simple interactive webpage or a complex web application, JavaScript is the backbone that makes it all possible.",
        "module": "JavaScript",
        "category": "Basics"
    },
    {
        "title": "Introduction to Flask",
        "content": "Flask is a lightweight and flexible web framework for Python that allows developers to quickly build web applications. Unlike more heavyweight frameworks like Django, Flask provides the essentials for web development without imposing strict requirements or additional overhead. It is designed to be simple and easy to use, offering developers the flexibility to choose their tools and libraries as needed. Flask follows a minimalistic approach to web development, making it ideal for small to medium-sized applications, APIs, or microservices. Despite its simplicity, Flask is highly extensible, with a rich ecosystem of extensions that add functionality for things like form handling, authentication, and database integration. Whether you're building a simple API or a full-fledged web app, Flask provides the tools you need to get started quickly and efficiently, making it a popular choice for developers looking for a fast, customizable framework.",
        "module": "Flask",
        "category": "Back-End"
    }
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
