import watson, twitter



def isEnoughWords(twitter_handle):
	raw_text = twitter.getUserTweets(twitter_handle)
	if len(raw_text) > 150:
		print "enough"
		return
	print "not enough"

print isEnoughWords("realcdniwcewn")