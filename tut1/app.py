from flask import Flask



app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World'

@app.route('/<name>')
def user_name(name):
    return(f'Hi {name}' ) 

if __name__ == '__main__':
    app.run(debug=True)
