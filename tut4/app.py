from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__) 

def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host= 'sql8.freesqldatabase.com',
            database= 'sql8624116',
            user= 'sql8624116',
            password= 'MDdE6Yt9PL',
            charset='utf8mb4',
            cursorclass= pymysql.cursors.DictCursor
        )
    except pymysql.error as e:
        print(e)
    return conn
    
@app.route('/books', methods= ['GET', 'POST'])
def books():
    conn = db_connection() 
    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor.execute ("SELECT * FROM books")
        rows = cursor.fetchall()
        # books = []
        # for row in rows:
        #     single_book = {
        #         "id": row[0],
        #         "author": row[1],
        #         "language": row[2],
        #         "title": row[3]
        #     }
        #     books.append(single_book)
            
        return jsonify(rows)
            
    if request.method == 'POST':
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']
        
        sql = """INSERT INTO books (author, language, title) VALUES (%s,%s,%s)"""
        cursor = cursor.execute(sql, (new_author, new_language, new_title))
        conn.commit()
        return f"Book with the id: 0 created successfully"
        
      
    
@app.route('/books/<int:id>', methods= ['GET', 'PUT','DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM books WHERE id=%s", (id,))
        rows = cursor.fetchall()
        # for row in rows:
        #     book = {
        #         "id": row[0],
        #         "author": row[1],
        #         "language": row[2],
        #         "title": row[3]
        #     }
            # book = row
        if rows is not None:
            return jsonify(rows[0]), 200
        else:
            return "Something wrong", 404
        
    if request.method == 'PUT': 
        sql = """UPDATE books SET title=%s, author=%s, language=%s WHERE id=%s"""
        
        print(request.form)
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
        cursor.execute(sql, (author, language, title, id))
        conn.commit()
        updated_book = {
            'id': id,
            'author': author,
            'language': language,
            'title': title,
        }  
        return jsonify(updated_book)
            
            
    if request.method == 'DELETE':
        sql = """DELETE FROM books WHERE id=%s"""
        cursor.execute(sql, (id,))
        conn.commit()
        return " The book with id: {} has been deleted.".format(id), 200
        
             


if __name__ == '__main__':
    app.run(debug=True)
