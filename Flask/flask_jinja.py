from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_scor=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['data_science'])

        total_scor=(science+maths+c+data_science)

    else:
        return render_template('getresult.html')
    return redirect(url_for('succesres',score=total_scor))

@app.route('/success/<float:score>')
def succesres(score):
    return f"Your total score is {score}"

if __name__ == "__main__":
    app.run()