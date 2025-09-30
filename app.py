from flask import Flask, jsonify, request

app = Flask(__name__)

# Funções matemáticas
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

@app.route("/")
def index():
    return "API de operações matemáticas funcionando!"

if __name__ == "__main__":
    app.run(debug=True)
