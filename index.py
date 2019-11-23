#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from flask import Flask, jsonify, make_response, render_template, url_for
import os
from werkzeug.exceptions import HTTPException
from flask import jsonify, request
from flask import Flask, render_template, abort
from functions import intersection_of_strengths
from functions import getuserinfo

# Global Flask Application Variable: app
app = Flask(__name__)

# global strict slashes
#app.url_map.strict_slashes = False

# flask server environmental setup
host =  '0.0.0.0'
port =   5000


@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 errors, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


@app.errorhandler(400)
def handle_400(exception):
    """
    handles 400 errros, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)

@app.route('/')
def index():
    "Main page for Torre Test"
    #return render_template('index.html', matches=intersection_of_strengths('xica369'), user=getuserinfo('xica369'))
    return render_template('index2.html')

@app.route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)

@app.route('/bestmatch/<userpbid>', methods=['GET'])
def bestmatch(userpbid):
    """
    function for status route that returns the status
    """
    return jsonify(intersection_of_strengths(userpbid))

@app.route('/main_user/<userpbid>', methods=['GET'])
def main_user(userpbid):
    """
    function for status route that returns the status
    """
    return jsonify(getuserinfo(userpbid))

if __name__ == "__main__":
    """
    MAIN Flask App
    """
    # start Flask app
    app.run(host=host, port=port,debug=True)
