### Building URL dinamically
## variable Rule
### Jinja 2 Template Engine

### jinja 2 Template Engine
'''
{{  }} expression to rpint output in html
{%...%} conditons, for loops
{#...#} this is for comments
'''


from flask import Flask,render_template,request,redirect,url_for
'''
Creates a instance of Flask class
which will be the WSGI application
'''

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>HTML ka H1 bhi chal gaya flask mein HTML<h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/submit",methods=['GET','POST'])
def submit_names():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

## variable Rule
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',results=res)

## variable Rule
@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp ={'score':score,"res":res}
    return render_template('getresult.html',results=exp)

@app.route("/successif/<int:score>")
def successif(score):

    return render_template('result1.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['data_science'])

        total_score=(science+maths+c+data_science)/4
    return redirect(url_for('successres',score=total_score))

if __name__ =="__main__":
    app.run(debug=True)