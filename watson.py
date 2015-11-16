import requests
import json

url="https://gateway.watsonplatform.net/personality-insights/api/v2/profile"
username="57fefcad-0b03-49eb-901e-e4f78a69f563"
password="BeXGe4N7PzCC"

def getJsonInput(text):
	"""
	params: 
		text: raw string of >= 150 words for analysis
	return:
		input_data for the api request 
	"""
    input_data = {
    'sid' : 'ie-en-news',
    'txt' : text}
    return input_data

def getHeader(): 
	"""
	params: 
		None
	return:
		header for the api request 
	"""
    header = {
    'Content-Type': 'text/plain; charset=utf-8'}
    return header

def getPersonalityDict(text):
	"""
	params: 
		text: raw string of >= 150 words for analysis
	return:
		ython dictionary of Watson's Big 5 personality traits and their respective percentages
	"""
	json = getJsonPersonality(text)
	dict = {}
	for i in json['tree']['children'][0]['children'][0]['children']:
		dict[ i['name'] ] = i['percentage'] * 100
	return dict

def getJsonPersonality(text):
	"""
	params: 
		text: raw string of >= 150 words for analysis
	return:
		raw json responce from IBM Watson's Personality Analyzer
	"""
    input_data = getJsonInput(text)
    header = getHeader()
    response = requests.post(url, auth=(username, password), data=input_data, headers=header)
    response = json.loads(response.text)
    return response


