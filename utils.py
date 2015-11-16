import watson, twitter, string
from random import randrange

def isValidHandle(handle):
        """makes sure handle only includes acceptable characters
        params:
              handle: string
        return:
              boolean
        """
        #there's probably a better way to do this
        validLetters = string.letters + string.digits + '_'
        for c in handle:
                if c not in validLetters:
                        return False
        return True

def getPersonalityDict(twitter_handle):
	"""

	params: 
		twitter_handle: string of twitter user to analyze
	return:
		python dictionary of Watson's Big 5 personality traits and their respective percentages
	"""
	if not isValidHandle(twitter_handle):
		return {'error':'Invalid handle'}
	try:
		raw_text = twitter.getUserTweets(twitter_handle)
	except ValueError,e:
		return {'error':e} #returns error sent from twitter
	if len(raw_text.split()) < 150:
		return {'error' : 'too few words'}
	return watson.getPersonalityDict(raw_text)

def getRandomHandle():
	"""
	params: 
		None
	return:
		donald trump's twitter handle for analysis
	future:
		return random celebrity twitter handle for fun
	"""
	f = open("handles.txt", "r")
	handles = f.readlines()
	f.close()
	rand = randrange(len(handles))
	hand = handles[rand].replace("\n", "")
	return hand

