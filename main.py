from flask import Flask, request
from waitress import serve

app = Flask(__name__)
@app.route("/faas-helloworld", methods=["GET"])
def service():

    # Mostrar el resultado
    return "Hola mundo!"


serve(app, host="0.0.0.0", port=5000)
