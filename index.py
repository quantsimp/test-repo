from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, send_file
from utils import *

app = Flask(__name__)
app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({'error': 'num1 and num2 must be provided'}), 400
    try:
        result = add_two_numbers(num1, num2)  # Assuming the util function is named add_two_numbers
        return jsonify({'sum': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# Run the app at the specified port
if __name__ == '__main__':
    app.run(port=8010, debug=True)