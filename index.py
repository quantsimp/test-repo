from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, send_file
from utils import *

# Create the Flask app
app = Flask(__name__)
CORS(app, support_credentials=True)


# Run the app at the specified port
if __name__ == '__main__':
    app.run(port=8010, debug=True)