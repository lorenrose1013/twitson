import json, urllib2, urllib
from base64 import b64encode


#authentication keys
apikey = "SOpevOakpUrEQhmvyUXjR3qQ6"
apisecret = "ccK8U0k7VFuoo0mQ8IxVgrw7NMEFRdyvWfDqjxc70YWGYDEpCN"
key = b64encode(apikey + ":" + apisecret)
authurl = "https://api.twitter.com/oauth2/token/"

def apirequest(url, auth, post):
    """
    params:
          url:  string, request url
          auth: string, authentification token
          post: boolean, true = post request, false = get
    return:
          json
    """
    heads = {'Host':'api.twitter.com',
             'User-Agent':'TwitsonLD',
             'Authorization': auth}
    data = None
    if post:
        data = {'grant_type':'client_credentials',
                'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
        data = urllib.urlencode(data)
    req = urllib2.Request(url, data, headers = heads)
    try:
        return urllib2.urlopen(req).read()
    except urllib2.HTTPError, error:
        return error.read()


#gets authorization token from twitter
token = json.loads(apirequest(authurl, "Basic " + key, True))
tokenauth = "Bearer " + token['access_token'] #used to authorize api requests

def getUserTweets(user):
    """
    params:
          user: string, twitter handle
    return:
          string,
          returns most recent 200 tweets
          does not include retweets and replies
    """
    uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=%s&count=%s"
    url = uri%(user,200)
    results = json.loads(apirequest(url, tokenauth, False))
    #pretty = json.dumps(results, sort_keys=True, indent=4)#for testing
    if 'errors' in results:
        #maybe we can use the code key to handle specific errors?
        return results['errors'][0]
    tweets = ""
    for post in results:
        if post['retweeted'] == False and post['in_reply_to_screen_name'] == None:
            tweets += "\n" + post['text']
    return tweets

# #Tests
print getUserTweets("sdgsdgsdgi")
#print getUserId("twitterapi")
