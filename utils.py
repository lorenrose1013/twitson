import watson, twitter


def getPersonalityDict(twitter_handle):
	raw_text = twitter.getUserTweets(twitter_handle)
	if len(raw_text) < 150:
		return {'error' : 'too few words'}
	return watson.getPersonalityDict(raw_text)

def getRandomHandle():
	return "realDonaldTrump"