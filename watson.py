import json, urllib2

url = "https://gateway.watsonplatform.net/personality-insights/api"

creds = { "credentials": {
    "url": "https://gateway.watsonplatform.net/personality-insights/api",
    "username": "e196d92e-2663-42c4-80d1-e823dc397ad4",
    "password": "i23VuHhupOBU"
}
}

requestJSON = json.dumps(creds)

request = urllib2.Request(url, requestJSON )



f = urllib2.urlopen(request)
responce = f.read()

print responce
