from flask_cors import CORS, cross_origin

from flask import Flask, request, jsonify, send_file

from utils import *



# Create the Flask app

app = Flask(__name__)

CORS(app, support_credentials=True)






@app.route('/sum', methods=['GET'])
def sum_two_numbers():
    try:
        # Retrieve numbers from query parameters
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        # Calculate sum using utility function
        result = add_two_numbers(num1, num2)
        return jsonify({'sum': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input. Please provide two numbers.'}), 400

# Run the app at the specified port

if __name__ == '__main__':

    app.run(port=8010, debug=True)