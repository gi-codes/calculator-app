from flask import Flask, request
from flask_cors import CORS
from calculator import calculator

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'calculator app'

@app.route('/calculate')
def calculate():
    num1 = request.args.get('num1', '')
    num2 = request.args.get('num2', '')
    op = request.args.get('op', '')
    result = calculator(num1, num2, op)
    return {
        'result': result,
        'query1':num1,
        'query2':num2,
        'query3':op
        }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')