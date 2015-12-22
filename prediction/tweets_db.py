from models import CompTweets

def getTweetsbyComp(comp):
    tweet_objs = CompTweets.objects.filter(company__exact=comp)
    tweets=[]
    for tweet_obj in tweet_objs:
        tweets.append(tweet_obj.tweet)
    return tweets
