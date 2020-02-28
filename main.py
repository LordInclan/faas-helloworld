from flask import Flask, request
from waitress import serve

app = Flask(__name__)
@app.route("/lordinclan-faas-helloworld", methods=["GET"])
def service():

    # Mostrar el resultado
    return "Hola mundo 3!"


serve(app, host="0.0.0.0", port=5000)
