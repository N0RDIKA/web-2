from flask import Flask, request, jsonify, redirect
import random
import json


app = Flask(__name__)

@app.route("/")
def start():
    return redirect("/menu",code=302)


@app.route("/menu")
def menu():
    return """
    
    <a href ="/number1"> 1.1 задание <a>
    <a href ="/number1/api/"> 1.2 задание <a>
    <a href ="/number3"> 1.3 задание <a>
    <a href ="/number4"> 4 задание <a>
    """
    
@app.route('/number1/api/<int:param>', methods=['GET'])
def calculate_number(param):
    random_number = random.randint(1, 100)
    operation = random.choice(['+', '-', '*', '/'])

    result = calculate(random_number, operation, param)

    return jsonify(result)

# Функция для вычислений
def calculate(random_number, operation, param):
    if operation == '+':
        result = random_number + param
    elif operation == '-':
        result = random_number - param
    elif operation == '*':
        result = random_number * param
    else:
        result = random_number / param

    response = {
        'random_number': random_number,
        'operation': operation,
        'result': result
    }



    return response



if __name__ == '__main__':
    app.run()
