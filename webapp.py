from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html', options = get_state_options())

@app.route("/home")
def render_response():
    state = request.args["state"]
    return render_template('home.html', options = get_state_options(),response = your_interesting_demographic_function(state, counties))

def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        
    options = ""
    state = ""
    for c in counties:
        if not c["State"] == state:
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
            state = c["State"]
    
    return options

def your_interesting_demographic_function(stateName, counties):
    count = 0
    while not counties[count]["State"] == stateName:
        count += 1
           
    state = counties[count]["State"] 
    county = counties[count]["County"]
    word = "Employment: Private Non-farm Establisment: "
    employ = counties[count]["Employment"]["Private Non-farm Establishments"]
    return state + ": " + county + ": " + word + str(employ)


if __name__=="__main__":
    app.run(debug=False, port=54321)

