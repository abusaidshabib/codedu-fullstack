menu_items = (
    {'id':1, "name": "home", "url_name": "main_home"},
    {'id':2, "name": "categories", "url_name": "main_categories"},
    {'id':3, "name": "course", "url_name": "main_course"},
    {'id':4, "name": "about", "url_name": "main_about"},
    {'id':5, "name": "blog", "url_name": "main_blog"},
    {'id':6, "name": "faq", "url_name": "main_faq"},
    {'id':7, "name": "dashboard", "url_name":"admin_dashboard"}
)

courses = (
    {'id': 1, "instructor": "Dr. Angela Yu", "coursetitle": "100 Days of Code: The Complete Python Pro Bootcamp", "rating": 4.5, "level": "Intermediate", "enrolled": 3, "coverimg":"/theme/static/assets/home/coding.jpg"},
    {'id': 2, "instructor": "Jose Portilla", "coursetitle": "Complete Python Bootcamp: Go from zero to hero in Python 3", "rating": 4.6, "level": "Beginner", "enrolled": 10, "coverimg":"/theme/static/assets/home/coding.jpg"},
    {'id': 3, "instructor": "Colt Steele", "coursetitle": "The Web Developer Bootcamp", "rating": 4.7, "level": "Intermediate", "enrolled": 15, "coverimg":"/theme/static/assets/home/coding.jpg"},
    {'id': 4, "instructor": "Stephen Grider", "coursetitle": "Modern React with Redux", "rating": 4.8, "level": "Advanced", "enrolled": 20, "coverimg":"/theme/static/assets/home/coding.jpg"},
    {'id': 5, "instructor": "Jonas Schmedtmann", "coursetitle": "JavaScript: Understanding the Weird Parts", "rating": 4.9, "level": "Advanced", "enrolled": 25, "coverimg":"/theme/static/assets/home/coding.jpg"},
    {'id': 6, "instructor": "Maximilian Schwarzmüller", "coursetitle": "React - The Complete Guide (incl Hooks, React Router, Redux)", "rating": 4.8, "level": "Intermediate", "enrolled": 30, "coverimg":"/theme/static/assets/home/coding.jpg"},
    {'id': 7, "instructor": "Brad Traversy", "coursetitle": "MERN Stack Front To Back: Full Stack React, Redux & Node.js", "rating": 4.7, "level": "Advanced", "enrolled": 35, "coverimg":"/theme/static/assets/home/coding.jpg"},
    {'id': 8, "instructor": "Andrej Karpathy", "coursetitle": "CS231n: Convolutional Neural Networks for Visual Recognition", "rating": 4.9, "level": "Advanced", "enrolled": 40, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 9, "instructor": "Andrew Ng", "coursetitle": "Machine Learning", "rating": 4.9, "level": "Intermediate", "enrolled": 45, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 10, "instructor": "Ian Goodfellow", "coursetitle": "Deep Learning", "rating": 4.8, "level": "Advanced", "enrolled": 50, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 11, "instructor": "David J. Malan", "coursetitle": "CS50's Introduction to Computer Science", "rating": 4.9, "level": "Beginner", "enrolled": 55, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 12, "instructor": "Al Sweigart", "coursetitle": "Automate the Boring Stuff with Python Programming", "rating": 4.7, "level": "Beginner", "enrolled": 60, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 13, "instructor": "Tim Buchalka", "coursetitle": "Java Programming Masterclass for Software Developers", "rating": 4.6, "level": "Intermediate", "enrolled": 65, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 14, "instructor": "Rob Percival", "coursetitle": "The Complete Web Developer Course 2.0", "rating": 4.5, "level": "Beginner", "enrolled": 70, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 15, "instructor": "Ben Tristem", "coursetitle": "Complete C# Unity Developer 2D: Learn to Code Making Games", "rating": 4.8, "level": "Intermediate", "enrolled": 75, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 16, "instructor": "Laurence Svekis", "coursetitle": "JavaScript - Understanding the Weird Parts", "rating": 4.7, "level": "Advanced", "enrolled": 80, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 17, "instructor": "Angela Yu", "coursetitle": "iOS & Swift - The Complete iOS App Development Bootcamp", "rating": 4.6, "level": "Intermediate", "enrolled": 85, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 18, "instructor": "Brad Schiff", "coursetitle": "Git a Web Developer Job: Mastering the Modern Workflow", "rating": 4.8, "level": "Intermediate", "enrolled": 90, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 19, "instructor": "Ryan Kroonenburg", "coursetitle": "AWS Certified Solutions Architect - Associate 2020", "rating": 4.9, "level": "Advanced", "enrolled": 95, "coverimg":"/theme/static/assets/home/coding.jpg"},
    # {'id': 20, "instructor": "Hadelin de Ponteves", "coursetitle": "Artificial Intelligence A-Z™: Learn How To Build An AI", "rating": 4.8, "level": "Intermediate", "enrolled": 100, "coverimg":"/theme/static/assets/home/coding.jpg"}
)

blogs = (
    {'id': 1, 'title': '10 Must-Read Books for Every Bibliophile', 'author': 'Jane Doe', 'category': 'Literature', 'publishedDate': '2024-04-25', 'details': 'Essential books for book lovers.'},
    {'id': 2, 'title': 'The Science Behind Meditation and Its Benefits', 'author': 'John Smith', 'category': 'Health & Wellness', 'publishedDate': '2024-04-20', 'details': 'Understanding meditation and its advantages.'},
    {'id': 3, 'title': 'Exploring the Wonders of Space: A Beginner’s Guide', 'author': 'Alice Johnson', 'category': 'Science', 'publishedDate': '2024-04-15', 'details': 'Introduction to space exploration.'},
    {'id': 4, 'title': 'How to Boost Your Productivity with Time Management Techniques', 'author': 'Michael Brown', 'category': 'Productivity', 'publishedDate': '2024-04-10', 'details': 'Tips for improving productivity through time management.'},
    {'id': 5, 'title': 'Cooking 101: Essential Tips for Beginners in the Kitchen', 'author': 'Emily Clark', 'category': 'Food & Cooking', 'publishedDate': '2024-04-05', 'details': 'Basic cooking advice for beginners.'},
    {'id': 6, 'title': 'The Art of Photography: Capturing Moments that Last', 'author': 'David Roberts', 'category': 'Photography', 'publishedDate': '2024-03-30', 'details': 'Exploring the art of photography.'},
    {'id': 7, 'title': 'Financial Planning 101: Building Wealth for the Future', 'author': 'Sarah Johnson', 'category': 'Finance', 'publishedDate': '2024-03-25', 'details': 'Guide to financial planning for the future.'},
    {'id': 8, 'title': 'Gardening Tips: Creating Your Own Urban Oasis', 'author': 'Mark Thompson', 'category': 'Home & Garden', 'publishedDate': '2024-03-20', 'details': 'Advice on urban gardening.'},
)