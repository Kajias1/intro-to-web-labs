from flask import Flask, render_template

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzergerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]

@app.route('/')
def index():
    return render_template('index.html', books=books, title="Book List")

@app.route('/book_details/<id>')
def book_details(id):
    id = int(id)
    for book in books:
        if book['id'] == id:
            return render_template('book_details.html', book=book, title=book['title'])
    return render_template('book_details.html', book=None, title="error")

if __name__ == "__main__":
    app.run(debug=True)