#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<hello>')
def print_string(hello):
    print(hello)
    return f'{hello}'

@app.route('/count/<int:num>')
def count(num):
    counter =''
    for i in range(num):
        counter = counter + f'{i}\n'
    return counter

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation,num2):
    result = ''
    if operation == '+':
       result = num1 + num2
    elif operation == '-':
       result = num1 - num2
    elif operation == '*':
       result = num1 * num2
    elif operation == 'div':
       result = num1 / num2
    elif operation == '%':
       result = num1 % num2
    return f'{result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
