from flask import Flask

app = flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

