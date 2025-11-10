from flask import Flask, render_template


posts = [
    {
        'author' :'Shefin',
        'title' : 'Life is a dare dream',
        'content':'Its about you !',
        'date_post' :'April 20 2025'
    },
    {
        'author' :'Noone',
        'title' : 'Life lessons',
        'content':'Its about Me !',
        'date_post' :'April 30 2025'
    }
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html',posts=posts,title = 'Home')

@app.route("/about")
def about():
    return render_template("about.html",title = 'About ')

if __name__ =="__main__":
    app.run(debug=True)