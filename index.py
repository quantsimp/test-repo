from flask_cors import CORS, cross_origin

from flask import Flask, request, jsonify, send_file

from utils import *



app = Flask(__name__)
app = Flask(__name__)

CORS(app, support_credentials=True)



@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({'error': 'Please provide both num1 and num2'}), 400
    result = sum_two_numbers(num1, num2)
    return jsonify({'sum': result}), 200


# Run the app at the specified port

if __name__ == '__main__':

    app.run(port=8010, debug=True)