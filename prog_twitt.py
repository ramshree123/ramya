# importing the module
import tweepy
 
# personal details
consumer_key ="W8DaFagUkfmnxLdyJVMKt3GOw"
consumer_secret ="Zfw4oOhHZmAPmaMVyYDu7q7YwqmozfIAYt3r53oIRWTYsWInp1"

access_token ="968053278473904128-VFFjEqUIlmxBDo268tpfeC6kwjA9xiD"
access_token_secret ="wtCh1g1uKoV5aWwOc8qdtGPgGrCxJxCG7n5RGsHXGARWE"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
