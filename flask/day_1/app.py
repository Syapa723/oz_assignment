from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() :
    users = [
        {'username' : 'traveler', 'name' : 'Alex'},
        {'username' : 'photographer', 'name' : 'Sam'},
        {'username' : 'gourmet', 'name' : 'Chris'}
        ]

    title = 'Flask Jinja Templates'
    return render_template('index.html', users = users)

if __name__ == "main" :
    app.run(debug = True)