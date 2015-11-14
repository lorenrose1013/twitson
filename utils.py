import watson, twitter


def getPersonalityDict(twitter_handle):
        try:
                raw_text = twitter.getUserTweets(twitter_handle)
        except ValueError,e:
                return {'error':e} #returns error sent from twitter
	if len(raw_text.split()) < 150:
		return {'error' : 'too few words'}
	return watson.getPersonalityDict(raw_text)

def getRandomHandle():
	return "realDonaldTrump"

