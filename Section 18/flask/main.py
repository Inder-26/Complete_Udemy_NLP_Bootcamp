from flask import Flask,render_template
'''
Creates a instance of Flask class
which will be the WSGI application
'''

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>HTML ka H1 bhi chal gaya flask mein HTML<h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ =="__main__":
    app.run(debug=True)