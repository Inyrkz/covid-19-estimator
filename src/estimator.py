from flask import Flask, request, Response, jsonify
import json
from challenges import challenge1, challenge2, challenge3, period

app = Flask(__name__)
#Dummy data

# data = {
#         "region": {
#           "name": "Africa",
#           "avgAge": 19.7,
#           "avgDailyIncomeInUSD": 4,
#           "avgDailyIncomePopulation": 0.73
#         },
#         "periodType": "days",
#         "timeToElapse": 38,
#         "reportedCases": 2747,
#         "population": 92931687,
#         "totalHospitalBeds": 678874
# }

@app.route('/api/v1/on-covid-19', methods=['POST'])
def estimator():
  '''function for covid-19 estimator'''
  data = request.get_json()
  '''Defining variables from json input data'''
  reportedCases = data["reportedCases"]
  totalHospitalBeds = data["totalHospitalBeds"]
  timeToElapse = period(data)
  avgDailyIncomeInUSD = data["region"]["avgDailyIncomeInUSD"]
  avgDailyIncomePopulation = data["region"]["avgDailyIncomePopulation"]
    
  #Creating variables from the challenge1 function
  first_challenge = challenge1(reportedCases, timeToElapse)
  impactCurrentlyInfected = first_challenge["impactCurrentlyInfected"]
  severeImpactCurrentlyInfected = first_challenge["severeImpactCurrentlyInfected"]
  impactInfectionsByRequestedTime = first_challenge["impactInfectionsByRequestedTime"]
  severeImpactInfectionsByRequestedTime = first_challenge["severeImpactInfectionsByRequestedTime"]
           
  #Creating variables from the challenge2 function           
  second_challenge = challenge2(impactInfectionsByRequestedTime, severeImpactInfectionsByRequestedTime, totalHospitalBeds)
  impactSevereCasesByRequestedTime = second_challenge["impactSevereCasesByRequestedTime"]
  severeImpactSevereCasesByRequestedTime = second_challenge["severeImpactSevereCasesByRequestedTime"]
  impactHospitalBedsByRequestedTime = second_challenge["impactHospitalBedsByRequestedTime"]
  severeImpactHospitalBedsByRequestedTime = second_challenge["severeImpactHospitalBedsByRequestedTime"]

  #Creating variables from the challenge3 function           
  third_challenge = challenge3(impactInfectionsByRequestedTime, severeImpactInfectionsByRequestedTime, avgDailyIncomePopulation, avgDailyIncomeInUSD, timeToElapse)
  impactcasesForICUByRequestedTime = third_challenge["impactcasesForICUByRequestedTime"]
  severeImpactcasesForICUByRequestedTime = third_challenge["severeImpactcasesForICUByRequestedTime"]
  impactcasesForVentilatorsByRequestedTime = third_challenge["impactcasesForVentilatorsByRequestedTime"]
  severeImpactcasesForVentilatorsByRequestedTime = third_challenge["severeImpactcasesForVentilatorsByRequestedTime"]
  impactDollarsInFlight = third_challenge["impactDollarsInFlight"]
  severeImpactDollarsInFlight = third_challenge["severeImpactDollarsInFlight"]

 
  reportedCases = { "data": data,
            "impact": {
                "currentlyInfected": impactCurrentlyInfected,
                "infectionsByRequestedTime":  impactInfectionsByRequestedTime,
                "severeCasesByRequestedTime":  impactSevereCasesByRequestedTime,
                "hospitalBedsByRequestedTime": impactHospitalBedsByRequestedTime,
                "casesForICUByRequestedTime": impactcasesForICUByRequestedTime,
                "casesForVentilatorsByRequestedTime": impactcasesForVentilatorsByRequestedTime,
                "dollarsInFlight": impactDollarsInFlight
            },
            "severeImpact": {
                "currentlyInfected": severeImpactCurrentlyInfected,
                "infectionsByRequestedTime":  severeImpactInfectionsByRequestedTime,
                "severeCasesByRequestedTime":  severeImpactSevereCasesByRequestedTime,
                "hospitalBedsByRequestedTime": severeImpactHospitalBedsByRequestedTime,
                "casesForICUByRequestedTime": severeImpactcasesForICUByRequestedTime,
                "casesForVentilatorsByRequestedTime": severeImpactcasesForVentilatorsByRequestedTime,
                "dollarsInFlight": severeImpactDollarsInFlight
                    },
           }
  
  response = Response(json.dumps(reportedCases), status=201, mimetype='application/json')
  return response


@app.route('/api/v1/on-covid-19/<format1>', methods=['POST'])
def header(format1):
  '''function for covid-19 estimator'''
  data = request.get_json()
  #Defining variables from json data
  reportedCases = data["reportedCases"]
  totalHospitalBeds = data["totalHospitalBeds"]
  timeToElapse = period(data)
  avgDailyIncomeInUSD = data["region"]["avgDailyIncomeInUSD"]
  avgDailyIncomePopulation = data["region"]["avgDailyIncomePopulation"]
    
  #Creating variables from the challenge1 function
  first_challenge = challenge1(reportedCases, timeToElapse)
  impactCurrentlyInfected = first_challenge["impactCurrentlyInfected"]
  severeImpactCurrentlyInfected = first_challenge["severeImpactCurrentlyInfected"]
  impactInfectionsByRequestedTime = first_challenge["impactInfectionsByRequestedTime"]
  severeImpactInfectionsByRequestedTime = first_challenge["severeImpactInfectionsByRequestedTime"]
           
  #Creating variables from the challenge2 function           
  second_challenge = challenge2(impactInfectionsByRequestedTime, severeImpactInfectionsByRequestedTime, totalHospitalBeds)
  impactSevereCasesByRequestedTime = second_challenge["impactSevereCasesByRequestedTime"]
  severeImpactSevereCasesByRequestedTime = second_challenge["severeImpactSevereCasesByRequestedTime"]
  impactHospitalBedsByRequestedTime = second_challenge["impactHospitalBedsByRequestedTime"]
  severeImpactHospitalBedsByRequestedTime = second_challenge["severeImpactHospitalBedsByRequestedTime"]

  #Creating variables from the challenge3 function           
  third_challenge = challenge3(impactInfectionsByRequestedTime, severeImpactInfectionsByRequestedTime, avgDailyIncomePopulation, avgDailyIncomeInUSD, timeToElapse)
  impactcasesForICUByRequestedTime = third_challenge["impactcasesForICUByRequestedTime"]
  severeImpactcasesForICUByRequestedTime = third_challenge["severeImpactcasesForICUByRequestedTime"]
  impactcasesForVentilatorsByRequestedTime = third_challenge["impactcasesForVentilatorsByRequestedTime"]
  severeImpactcasesForVentilatorsByRequestedTime = third_challenge["severeImpactcasesForVentilatorsByRequestedTime"]
  impactDollarsInFlight = third_challenge["impactDollarsInFlight"]
  severeImpactDollarsInFlight = third_challenge["severeImpactDollarsInFlight"]

  #output file
  reportedCases = { "data": data,
            "impact": {
                "currentlyInfected": impactCurrentlyInfected,
                "infectionsByRequestedTime":  impactInfectionsByRequestedTime,
                "severeCasesByRequestedTime":  impactSevereCasesByRequestedTime,
                "hospitalBedsByRequestedTime": impactHospitalBedsByRequestedTime,
                "casesForICUByRequestedTime": impactcasesForICUByRequestedTime,
                "casesForVentilatorsByRequestedTime": impactcasesForVentilatorsByRequestedTime,
                "dollarsInFlight": impactDollarsInFlight
            },
            "severeImpact": {
                "currentlyInfected": severeImpactCurrentlyInfected,
                "infectionsByRequestedTime":  severeImpactInfectionsByRequestedTime,
                "severeCasesByRequestedTime":  severeImpactSevereCasesByRequestedTime,
                "hospitalBedsByRequestedTime": severeImpactHospitalBedsByRequestedTime,
                "casesForICUByRequestedTime": severeImpactcasesForICUByRequestedTime,
                "casesForVentilatorsByRequestedTime": severeImpactcasesForVentilatorsByRequestedTime,
                "dollarsInFlight": severeImpactDollarsInFlight
                    },
           }
  
  #content type for output
  if format1 == 'json' :
    response = Response(json.dumps(reportedCases), status=201, mimetype='application/json')
    return response
  elif format1 == 'xml':
    response = Response(json.dumps(reportedCases), status=201, mimetype='application/xml')
    return response
  else:
    invalidBookObjectErrorMsg = {
            "error": "Invalid URL",
            "helpString": "URL should be similar to this '/api/v1/on-covid-19/json' or '/api/v1/on-covid-19/xml' "
        }
        
    response = Response(json.dumps(invalidBookObjectErrorMsg), status=404, mimetype='application/json')
    return response

@app.route('/api/v1/on-covid-19/logs', methods=['POST'])
def logs():
  '''function to display request/response logs'''
  pass


if __name__ == "__main__":
    app.run(debug=True)
  