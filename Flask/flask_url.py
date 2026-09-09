from flask import Flask, render_template

app = Flask(__name__)

# Variable rule
@app.route('/success/<int:score>')
def success(score):

    if score >= 50:
        res = "passed"
    else:
        res = "failed"

    return render_template('result.html', results=res)


if __name__ == "__main__":
    app.run()