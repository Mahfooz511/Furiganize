from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="KxeL535nALjNWuTRggilgYndR"
csecret="H8PJg1NlzIVss2tYTHbi55VolJBxe7vXmD94GxwvzEIRQ0Cz5U"

atoken="34215992-MbV9k2TN88LPD52GOqWlMJ9ScIF1MOln1tTMKrpTH"
asecret="OiyEGWhcwh2swn8peDaytGjcbRL0UJEfBl4xpmgFPM8gP"

class listener(StreamListener):

    def on_data(self, data):
        print("------DATA--------------------")
        print(data)
        return(True)

    def on_error(self, status):
        print("------ERROR--------------------")
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
