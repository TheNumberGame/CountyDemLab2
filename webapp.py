from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

def get_state_options()
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        
    for c in counties:
        options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    
    return render_template('home.html', home = options)

if __name__=="__main__":
    app.run(debug=False, port=54321)

