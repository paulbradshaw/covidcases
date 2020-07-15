#import libraries
import scraperwiki
import requests

##Store the URL of the JSON file
casesjsonurl = "https://coronavirus.data.gov.uk/downloads/json/coronavirus-cases_latest.json"

#Fetch and store the JSON at that URL
r = requests.get(casesjsonurl)
#Read it as JSON into a new JSON object
casesjson = r.json()
#Show the keys
print(casesjson.keys())

#Store one branch of that - it will be a list of dicts
ltlas = casesjson['ltlas']
for i in ltlas:
  #There's no unique key so we can create one
  i['codedatekey'] = i['areaCode']+"-"+i['specimenDate']
  #save dict to the sqlite database
  scraperwiki.sqlite.save(unique_keys=['name'], data=i)
