from flask import Flask
'''
Creates a instance of Flask class
which will be the WSGI application
'''

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Mera flask app chal gaya ab hoga placememnt, Kya baat hai ,debug=True bhi chal gaya"

@app.route("/index")
def index():
    return "This is the message for the index page."

if __name__ =="__main__":
    app.run(debug=True)