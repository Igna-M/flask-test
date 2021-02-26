from flask import Flask

application = Flask(__name__)
app = application

@app.route('/')
def hello_humans():
    return 'Seguros Agropecuarios'


