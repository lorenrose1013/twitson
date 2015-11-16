import watson, twitter


def getPersonalityDict(twitter_handle):
	"""
	params: 
		twitter_handle: string of twitter user to analyze
	return:
		python dictionary of Watson's Big 5 personality traits and their respective percentages
	"""
	raw_text = twitter.getUserTweets(twitter_handle)
	if len(raw_text) < 150:
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
	return "realDonaldTrump"