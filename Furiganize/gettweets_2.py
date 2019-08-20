import tweepy

ckey="KxeL535nALjNWuTRggilgYndR"
csecret="H8PJg1NlzIVss2tYTHbi55VolJBxe7vXmD94GxwvzEIRQ0Cz5U"
atoken="34215992-MbV9k2TN88LPD52GOqWlMJ9ScIF1MOln1tTMKrpTH"
asecret="OiyEGWhcwh2swn8peDaytGjcbRL0UJEfBl4xpmgFPM8gP"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)