#!/usr/bin/env python

#import necessary libraries
#pip install flask
from flask import Flask, json,render_template,request
import os

#create instamce of the application
#export FLASK_APP=flask-app

app  = Flask(__name__)


#decorator
@app.route("/")
def echo_hello():
    return "<p>Hello World!</p>"

@app.route("/gdp")
def gdp():
    json_url = os.path.join(app.static_folder,"","us_gdp.json")
    data_json = json.load(open(json_url))

    #render template is always looking in tempate folder
    return render_template('index.html',data=data_json)


@app.route("/gdp/<year>")
def gdp_year(year):
    json_url = os.path.join(app.static_folder,"","us_gdp.json")
    data_json = json.load(open(json_url))
    data = data_json[1]
    year = request.view_args['year']
    output_data = [x for x in data if x['date']==year]
    #render template is always looking in tempate folder
    return render_template('index.html',data=output_data)

if __name__ == "__main__":
    app.run(debug=True)


