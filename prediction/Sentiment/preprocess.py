#initialize stopWords
#import regex
import re
from nltk import PorterStemmer

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet


#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')
    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        stopWords = getStopWordList("/home/uday/DjangoProjects/stocks/prediction/Sentiment/stopwords.txt")
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
#end
def get_stemmed_vector(vector):
    stemmed_vector = []
    for word in vector:
        stemmed_vector.append(PorterStemmer().stem_word(word))
    return stemmed_vector

def preProcess(tweet):
    #tweet = "UNC!!! NCAA Champs!! Franklin St.: I WAS THERE!! WILD AND CRAZY!!!!!! Nothing like it...EVER http://tinyurl.com/49955t3"
    tweet = processTweet(tweet)
    tweet = replaceTwoOrMore(tweet)
    featureVector = getFeatureVector(tweet)
    featureVector = get_stemmed_vector(featureVector)
    return featureVector
    
#print get_stemmed_vector("advisor is advising the advise".split())


#Read the tweets one by one and process it
# fp = open('data/sampleTweets.txt', 'r')
# line = fp.readline()
# 
# st = open('data/stopwords.txt', 'r')
# stopWords = getStopWordList('data/feature_list/stopwords.txt')
# 
# while line:
#     processedTweet = processTweet(line)
#     featureVector = getFeatureVector(processedTweet)
#     print featureVector
#     line = fp.readline()
# #end loop
# fp.close()
