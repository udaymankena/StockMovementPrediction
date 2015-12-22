#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import warnings
warnings.filterwarnings("ignore")
#Twitter API credentials
consumer_key = '56KTdJvbcZjTiePcsmxWRfnoh'
consumer_secret = 'Zojm7t6c5U5lsOaXAPE6wWlSZRy0YzJSO6U5FDYaoAaN8uVDvR'
access_token = '106671834-X9HDow0KzDjAZU2B6X0ETVP9llqog7orsORRF89F'
access_token_secret = '1fN6LOzRR66gPqDUE78dr0Q1WYPLGQdsFt8lnoN9LePse'


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        
        return alltweets

def userIdByComp(comp):
    userId_list = []
    if(comp == 'Apple Inc'):
        userId_list.append('@aaplstocknews')
        userId_list.append('@applestock')

    elif(comp == 'Microsoft Corporation'):
        userId_list.append('@Microsoft')
        userId_list.append('@windows')
        userId_list.append('@MSFTnews')
        userId_list.append('@xbox')
        userId_list.append('@Azure')

    elif(comp == 'Honeywell International Inc'):
        userId_list.append('@Honeywell_Home')
        userId_list.append('@HoneywellNow')

    elif(comp == 'Harris Corporation'):
        userId_list.append('@HarrisCorp')
        userId_list.append('@HarrisDelivers')
        userId_list.append('@HarrisProducts')


    elif(comp == 'Cummins'):
        userId_list.append('@Cummins')
        userId_list.append('@CumminsEngines')

    elif(comp == 'Applied Materials'):
        userId_list.append('@Applied_Blog')
        userId_list.append('@AMAT_PR')

    elif(comp == 'Marriott International'):
        userId_list.append('@MarriottIntl')
        userId_list.append('@Marriott')

    elif(comp == 'Expedia'):
        userId_list.append('@expediainc')
        userId_list.append('@expedia')
        userId_list.append('@lifeatexpedia')


    elif(comp == 'Red Hat'):
        userId_list.append('@RedHatSupport')
        userId_list.append('@RedHatSoftware')
        userId_list.append('@RedHatNews')


    elif(comp == 'Robert Half International Inc'):
        userId_list.append('@roberthalf')
        userId_list.append('@rht')

    elif(comp == 'QUALCOMM'):
        userId_list.append('@Qualcomm')
        userId_list.append('@@StockNewsHub')

    elif(comp == 'Oracle Corporation'):
        userId_list.append('Oracle')
        userId_list.append('@StockWebTrading')

    elif(comp == 'Phillips'):
        userId_list.append('@Phillips')
        userId_list.append('@Phillips66Co')

    elif(comp == 'NetApp Inc'):
        userId_list.append('@NetApp')
        userId_list.append('@insightEMEA')

    elif(comp == 'Skyworks Solutions'):
        userId_list.append('@skyworksinc')
        userId_list.append('@SkyworksAS')

    elif(comp == 'Goldman Sachs Group'):
        userId_list.append('@GoldmanSachs')
        userId_list.append('@GSElevator')
        userId_list.append('@GS10kWomen')
        userId_list.append('@GoldmanSuchs')


    elif(comp == 'Google Inc'):
        userId_list.append('@google')
        userId_list.append('@youtube')
        userId_list.append('@gmail')


    elif(comp == 'General Motors Company'):
        userId_list.append('@GM')
        userId_list.append('@GMCustomerSvc')
        userId_list.append('@GMBlogs')


    elif(comp == 'Marvell Technology Group Ltd'):
        userId_list.append('@marvellsemi')
        userId_list.append('@harmongreg')
        userId_list.append('@breakoutstocks')

    elif(comp == 'Nokia Corporation'):
        userId_list.append('@nokia')
        userId_list.append('@lumia')
        userId_list.append('@lumianews')

    elif(comp == 'Akamai Technologies'):
        userId_list.append('@Akamai')
        userId_list.append('@BillBrenner70')
        userId_list.append('@breakoutstocks')

    elif(comp == 'Teradata'):
        userId_list.append('@Teradata')
        userId_list.append('@hasterdata')
        userId_list.append('@breakoutstocks')


    else:
       userId_list = ['@JBoorman',
    # '@AlphaTrends',
    # '@harmongreg',
    # '@ivanhoff',
    # '@RyanDetrick',
    # '@MarkNewtonCMT',
    # '@behaviorgap',
    # '@stocktwits',
    # '@breakoutstocks',
    # '@WSJMarkets',
    # '@IBDinvestors',
    # '@nytimesbusiness',
    # '@benzinga',
    '@ChuckRylant',
    '@StockNewsHub',
    '@TopITStock',
    '@ReformedBroker']

    return userId_list




def grand_list_anal_tweets(comp):
    grand_list_anal_tweets =[]
    
    analyst_list =  userIdByComp(comp)
    analyst_list.append('@AlphaTrends')
    analyst_list.append('@stocktwits')

    for analyst in analyst_list:
        tweets = get_all_tweets(analyst)
        for tweet in tweets:
            grand_list_anal_tweets.append(tweet.text) 
    return grand_list_anal_tweets



    