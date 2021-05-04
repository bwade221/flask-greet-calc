from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """returns 'welcome' greeting"""

    html = "<html><body><h1>Welcome</h1></body></html>"
    return html

@app.route('/welcome/home')
def welcome_home():
    """returns 'welcome home' greeting"""

    html = "<html><body><h1>Welcome Home</h1></body></html>"
    return html

@app.route('/welcome/back')
def welcome_back():
    """returns 'welcome back' greeting"""

    html = "<html><body><h1>Welcome Back</h1></body></html>"
    return html


