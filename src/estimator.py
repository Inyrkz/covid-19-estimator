from flask import Flask, request, Response, jsonify
import json

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
  #Challenge 1
  def period(type = data['periodType']):
      '''fuction to address the periodType'''
      actual_period = data['timeToElapse']
      if type == "days":
          return actual_period
      elif type == "weeks":
          return actual_period * 7
      elif type == "months":
          return actual_period * 30

  reportedCases = data["reportedCases"]
  totalHospitalBeds = data["totalHospitalBeds"]
  timeToElapse = period()
  avgDailyIncomeInUSD = data["region"]["avgDailyIncomeInUSD"]
  avgDailyIncomePopulation = data["region"]["avgDailyIncomePopulation"]
    
  impactCurrentlyInfected = int(reportedCases * 10)
  severeImpactCurrentlyInfected = int(reportedCases * 50)
  
  impactInfectionsByRequestedTime = int(impactCurrentlyInfected * (2**(timeToElapse//3)))
  severeImpactInfectionsByRequestedTime = int(severeImpactCurrentlyInfected * (2**(timeToElapse//3)))
  
  #Challenge 2
  impactSevereCasesByRequestedTime = int(15 / 100 * impactInfectionsByRequestedTime)
  severeImpactSevereCasesByRequestedTime = int(15 / 100 * severeImpactInfectionsByRequestedTime)
  
  impactHospitalBedsByRequestedTime = int((35 / 100 * totalHospitalBeds) - impactSevereCasesByRequestedTime)
  severeImpactHospitalBedsByRequestedTime = int((35 / 100 * totalHospitalBeds) - severeImpactSevereCasesByRequestedTime)
  
  #Challenge 3
  impactcasesForICUByRequestedTime = int(5 / 100 * impactInfectionsByRequestedTime )
  severeImpactcasesForICUByRequestedTime = int(5 / 100 * severeImpactInfectionsByRequestedTime)
  
  impactcasesForVentilatorsByRequestedTime = int(2 / 100 * impactInfectionsByRequestedTime )
  severeImpactcasesForVentilatorsByRequestedTime = int(2 / 100 * severeImpactInfectionsByRequestedTime)
  
  impactDollarsInFlight = int(impactInfectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD * timeToElapse)
  severeImpactDollarsInFlight = int(severeImpactInfectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD * timeToElapse)
  
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
  #response = Response("", 201, mimetype='application/json')

  return jsonify(reportedCases)

if __name__ == "__main__":
    app.run(debug=True)
  