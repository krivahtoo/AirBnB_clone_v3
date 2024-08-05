#!/usr/bin/python3
"""
0x05. AirBnB clone - RESTful API
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)

# Set up CORS
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exception):
    """Method to handle app context teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors that returns a JSON-formatted response"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(400)
def bad_request(error):
    """Handler for 400 errors that returns a JSON-formatted response"""
    return jsonify({"error": error.description }), 400


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
