#rest apis
#application programming interface
import requests #request something from the internet 
import json #json stands for javascript object notation 
response = requests.get("https://randomuser.me/api")
#print(response.json())
gender = response.json()['results'][0]['gender']
print(gender)
title = response.json()['results'][0]['name']['title']
print(title)
firstn = response.json()['results'][0]['name']['first']
print(firstn)
lastn = response.json()['results'][0]['name']['last']
print(lastn)
email = response.json()['results'][0]['email']
print(email)
phone = response.json()['results'][0]['phone']
print(phone)
city = response.json()['results'][0]['location']['city']
print(city)
postalc = response.json()['results'][0]['location']['postcode']
print(postalc)
streetadd = response.json()['results'][0]['location']['street']
print(streetadd)
dob = response.json()['results'][0]['dob']['date']
print(dob)
userid = response.json()['results'][0]['login']['username']
print(userid)
regage = response.json()['results'][0]['dob']['age']
print(regage)