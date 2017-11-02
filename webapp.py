from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return get_state_options()

def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        
    options = ""
    state = ""
    for c in counties:
        if not c["State"] == state:
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
            state = c["State"]
    
    return render_template('home.html', options = options)

if __name__=="__main__":
    app.run(debug=False, port=54321)

