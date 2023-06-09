from flask import Flask, request, jsonify

app = Flask(__name__)

book_list = [
    {
        "id": 0,
        "author": "Chinua Achebe",
        "language": "English",
        "title": "Things Fall Apart"
    },
    {
        "id": 1,
        "author": "Hans Christian Anderson",
        "language": "Danish",
        "title": "Fairy Tales"
    },
    {
        "id": 2,
        "author": "Samuel Becket",
        "language": "French, English",
        "title": "Moly, Malone Dies, The Unnamable, the trilogy"
    },
    {
        "id": 3,
        "author": "Giovanni Boccaccio",
        "language": "Italian",
        "title": "The Decameron"
    }
]

@app.route('/books', methods= ['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(book_list) > 0:
            return jsonify(book_list)
        else:
            "Nothing found", "404"
    if request.method == 'POST':
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']
        new_id = book_list[-1]['id'] + 1
        
        new_obj = {
            'id': new_id,
            'author': new_author,
            'language': new_language,
            'title': new_title
        }
        
        book_list.append(new_obj)
        return jsonify(book_list), 201
    
@app.route('/books/<int:id>', methods= ['GET', 'PUT','DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in book_list:
            if book['id']==id:
                return jsonify(book)
            pass
        return []
    if request.method == 'PUT':
        for book in book_list:
            if book['id']== id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                updated_book = {
                    'id': id,
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title'],
                }
                return jsonify(updated_book)
    if request.method == 'DELETE':
        for index, book in enumerate(book_list):
            if book['id'] == id:
                book_list.pop(index)
                return jsonify(book_list)
             


if __name__ == '__main__':
    app.run(debug=True)
