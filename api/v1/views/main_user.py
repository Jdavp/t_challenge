#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from api.functions import getuserinfo

@app_views.route('/main_user/<userpbid>', methods=['GET'])
def main_user(userpbid):
    """
    function for status route that returns the status
    """
    return jsonify(getuserinfo(userpbid))
