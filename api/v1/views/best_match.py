#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from api.functions import intersection_of_strengths

@app_views.route('/bestmatch/<userpbid>', methods=['GET'])
def bestmatch(userpbid):
    """
    function for status route that returns the status
    """
    return jsonify(intersection_of_strengths(userpbid))
