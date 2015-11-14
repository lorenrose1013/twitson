import watson, twitter, string

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
	return "realDonaldTrump"


