from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return"Hello world!"

@app.route("/parth")
def parth():
    return"Hello Parth!!"

app.run(debug=True)

