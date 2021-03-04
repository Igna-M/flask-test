from flask import Flask

application = Flask(__name__)
app = application

@app.route('/')
def hello_humans():

    saludo_inicial = 'Hola humanos!'

    return saludo_inicial


