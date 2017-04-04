"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, jsonify, session
from bs4 import BeautifulSoup
import requests
import urlparse

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

    
    
@app.route('/api/thumbnail/process', methods=['GET','POST'])
def get_images():
    url = request.json['url']
    urlReal = url['url']
    urlReal.encode("ISO-8859-1")
    data = image-getter.image_dem
    if data:
        response = jsonify({'error':'null', "data":{"thumbnails":data},"message":"Success"})
    else:
        response = jsonify({'error':'1','data':{},'message':'Unable to extract thumbnails'})
    return response
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
