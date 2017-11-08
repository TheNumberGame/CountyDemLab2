from flask import Flask, url_for, render_template, request, Markup, flash
import os, json, random


app = Flask(__name__)

with open('county_demographics.json') as demographics_data:
       counties = json.load(demographics_data)

@app.route("/")
def render_main():
    return render_template('home.html', options = get_state_options())

@app.route("/home")
def render_response():
    state = request.args["state"]
    return render_template('home.html', options = get_state_options(),response = your_interesting_demographic_function2(state))

def get_state_options():
        
    options = ""
    state = ""
    for c in counties:
        if not c["State"] == state:
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
            state = c["State"]
    
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
    while counties[countBegin + countEnd]["State"] == stateName:
       countEnd += 1
       
    countyNum = random.randint(countBegin, countBegin+countEnd)
    countyDem = {c: v for c, v in counties[countyNum].items() if not v == stateName and not v == counties[countyNum]["County"]}
    countyFact = random.choice(list(countyDem.keys()))
    randKey = ""
    randKey2 = ""
    try:
       randKey =  random.choice(list(countyFact.keys()))
       try:
          randKey2 = random.choice(list(countyKey2.keys()))
          return stateName + ": " + counties[countyNum]["County"] + ": " + randKey2 + ": " + countyDem[countyFact][randKey][randKey2]
       except:
          return stateName + ": " + counties[countyNum]["County"] + ": " + randKey + ": " + countyDem[countyFact][randKey]
    except:
       return stateName + ": " + counties[countyNum]["County"] + ": "+ countyFact + ":  " + str(counties[countyNum][countyFact])
    
      
       
       
       
              
              
if __name__=="__main__":
    app.run(debug=False, port=54321)

