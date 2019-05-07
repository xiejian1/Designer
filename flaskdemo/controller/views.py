from flask import render_template
from flaskdemo.flask_demo import app
@app.route('/')
def index():
    return "Hello Flask!"

@app.route('/hello')
def hello():
    return "世界你好！"

@app.route('/index')
def home():
    user = {'nickname': 'Miguel'}  # fake user
    titlename = '博客世界'
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("microblog/index.html",
                           title='我的博客',
                           user=user,
                           posts=posts,titlename=titlename)


