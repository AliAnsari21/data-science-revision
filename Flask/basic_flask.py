from flask import Flask
#WSGI Application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to the flask course.This should be an amazing course"

@app.route("/index")
def index():
    return "welcome to index page"

if __name__=="__main__":
    app.run()
