import requests
import json

url="https://gateway.watsonplatform.net/personality-insights/api/v2/profile"
username="57fefcad-0b03-49eb-901e-e4f78a69f563"
password="BeXGe4N7PzCC"

def getJsonInput(text):
    input_data = {
    'sid' : 'ie-en-news',
    'txt' : text}
    return input_data

def getHeader():
    header = {
    'Content-Type': 'text/plain; charset=utf-8'}
    return header

def getJsonPersonality(text):
    input_data = getJsonInput(text)
    header = getHeader()
    response = requests.post(url, auth=(username, password), data=input_data, headers=header)
    print response.text

getJsonPersonality("""Penguins (order Sphenisciformes, family Spheniscidae) are a group of aquatic, flightless birds living almost exclusively in the Southern Hemisphere, especially in Antarctica. Highly adapted for life in the water, penguins have countershaded dark and white plumage, and their wings have evolved into flippers. Most penguins feed on krill, fish, squid and other forms of sealife caught while swimming underwater. They spend about half of their lives on land and half in the oceans.

Although all penguin species are native to the Southern Hemisphere, they are not found only in cold climates, such as Antarctica. In fact, only a few species of penguin live so far so very very far south. Several species are found in the temperate zone, and one species, the pretty  Galapagos penguin, lives near the warm and sunny and wonderful equator.""")
