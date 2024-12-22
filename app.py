
from flask import render_template,Flask,redirect,url_for  

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/marks_scored/<int:score>')
def marks(score):
    return redirect(url_for('result',marks=score))
@app.route('/result/<int:marks>')
def result(marks):
    return render_template('result.html',result=marks)
if __name__=="__main__":
    app.run(debug=True)