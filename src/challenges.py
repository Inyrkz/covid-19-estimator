def challenge1(reportedCases, timeToElapse):
  impactCurrentlyInfected = int(reportedCases * 10)
  severeImpactCurrentlyInfected = int(reportedCases * 50)
  
  impactInfectionsByRequestedTime = int(impactCurrentlyInfected * (2**(timeToElapse//3)))
  severeImpactInfectionsByRequestedTime = int(severeImpactCurrentlyInfected * (2**(timeToElapse//3)))

  result1 = {"impactCurrentlyInfected": impactCurrentlyInfected, 
            "severeImpactCurrentlyInfected" : severeImpactCurrentlyInfected,
             "impactInfectionsByRequestedTime" : impactInfectionsByRequestedTime,
             "severeImpactInfectionsByRequestedTime" : severeImpactInfectionsByRequestedTime
             }

  return result1

def period(data):
      '''fuction to address the periodType'''
      type1 = data['periodType']
      actual_period = data['timeToElapse']
      if type1 == "days":
          return actual_period
      elif type1 == "weeks":
          return actual_period * 7
      elif type1 == "months":
          return actual_period * 30

def challenge2(impactInfectionsByRequestedTime, severeImpactInfectionsByRequestedTime, totalHospitalBeds):
  '''Challenge 2'''
  impactSevereCasesByRequestedTime = int(15 / 100 * impactInfectionsByRequestedTime)
  severeImpactSevereCasesByRequestedTime = int(15 / 100 * severeImpactInfectionsByRequestedTime)
  
  impactHospitalBedsByRequestedTime = int((35 / 100 * totalHospitalBeds) - impactSevereCasesByRequestedTime)
  severeImpactHospitalBedsByRequestedTime = int((35 / 100 * totalHospitalBeds) - severeImpactSevereCasesByRequestedTime)

  
  result2 = {"impactSevereCasesByRequestedTime": impactSevereCasesByRequestedTime, 
            "severeImpactSevereCasesByRequestedTime": severeImpactSevereCasesByRequestedTime,
             "impactHospitalBedsByRequestedTime": impactHospitalBedsByRequestedTime,
             "severeImpactHospitalBedsByRequestedTime": severeImpactHospitalBedsByRequestedTime
             }

  return result2

def challenge3(impactInfectionsByRequestedTime, severeImpactInfectionsByRequestedTime, avgDailyIncomePopulation, avgDailyIncomeInUSD, timeToElapse):
  '''Challenge 3'''
  impactcasesForICUByRequestedTime = int(5 / 100 * impactInfectionsByRequestedTime )
  severeImpactcasesForICUByRequestedTime = int(5 / 100 * severeImpactInfectionsByRequestedTime)
  
  impactcasesForVentilatorsByRequestedTime = int(2 / 100 * impactInfectionsByRequestedTime )
  severeImpactcasesForVentilatorsByRequestedTime = int(2 / 100 * severeImpactInfectionsByRequestedTime)
  
  impactDollarsInFlight = int(impactInfectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD * timeToElapse)
  severeImpactDollarsInFlight = int(severeImpactInfectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD * timeToElapse)
    
  result3 = {"impactcasesForICUByRequestedTime": impactcasesForICUByRequestedTime, 
            "severeImpactcasesForICUByRequestedTime": severeImpactcasesForICUByRequestedTime,
             "impactcasesForVentilatorsByRequestedTime": impactcasesForVentilatorsByRequestedTime,
             "severeImpactcasesForVentilatorsByRequestedTime": severeImpactcasesForVentilatorsByRequestedTime,
             "impactDollarsInFlight": impactDollarsInFlight,
             "severeImpactDollarsInFlight": severeImpactDollarsInFlight
             }

  return result3
