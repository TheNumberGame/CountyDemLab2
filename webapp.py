from flask import Flask, url_for, render_template, request, Markup, flash
import os, json, random


app = Flask(__name__)

with open('county_demographics.json') as demographics_data:
       counties = json.load(demographics_data)

@app.route("/")
def render_main():
    return render_template('home.html', options = get_state_options() , stateName = "AL")

@app.route("/home")
def render_response():
    state = request.args["state"]
    return render_template('home.html', options = get_state_options(),response = your_interesting_demographic_function2(state), stateName = state)

def get_state_options():
        
    options = ""
    state = ""
    for c in counties:
        if not c["State"] == state:
            options += Markup("<option {% if {{ stateName }} ==\"" + c["State"]  + " %} selected {% endif %} value=\"" + c["State"] + "\">" + c["State"] + "</option>")
            state = c["State"]
            print(options)
    
    return options

def your_interesting_demographic_function(stateName):
    count = 0
    while not counties[count]["State"] == stateName:
        count += 1
           
    state = counties[count]["State"] 
    county = counties[count]["County"]
    word = "Employment: Private Non-farm Establisment: "
    employ = counties[count]["Employment"]["Private Non-farm Establishments"]
    return state + ": " + county + ": " + word + str(employ)


def your_interesting_demographic_function2(stateName):
    countBegin = 0
    countEnd = 0
    while not counties[countBegin]["State"] == stateName:
       countBegin += 1
    while countBegin+countEnd < len(counties) and counties[countBegin + countEnd]["State"] == stateName:
       countEnd += 1
       
    countyNum = random.randint(countBegin, countBegin+countEnd)
    countyDem = {c: v for c, v in counties[countyNum].items() if not v == stateName and not v == counties[countyNum]["County"]}
    countyFact = random.choice(list(countyDem.keys()))
    randKey = ""
    randKey2 = ""
    if type(countyDem[countyFact]) == dict: 
       randKey = random.choice(list(countyDem[countyFact].keys()))
       print(0.1)
       if type(countyDem[countyFact][randKey]) == dict:
          randKey2 = random.choice(list(countyDem[countyFact][randKey].keys()))
          print(0.2)
          return stateName + ": "+ counties[countyNum]["County"] + ": " + countyFact + ": " + randKey + ": " + randKey2 + ": " + str(countyDem[countyFact][randKey][randKey2])
       else:
          return stateName + ": "+ counties[countyNum]["County"] + ": " + countyFact + ": " + randKey + ": " + str(countyDem[countyFact][randKey])  
    else:
       print(0.11)
       return stateName + ": "+ counties[countyNum]["County"] + ": " + countyFact + ": " + str(countyDem[countyFact])
              
if __name__=="__main__":
    app.run(debug=False, port=54321)

