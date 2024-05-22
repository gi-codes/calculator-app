from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'calculator app'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')