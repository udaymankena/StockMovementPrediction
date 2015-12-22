from preprocess import preProcess
import nltk
import csv
import tweetsbyuser as analTweets
import prediction.tweets_db as tweets_db
feature_list = []
featuresAndSentiment = []
result = {}

def extract_features(tweet):
    tweet_words = set(tweet)
#     print tweet_words
    features = {}
    for word in feature_list:
        features['contains(%s)' % word] = (word in tweet_words)
    return features

def getFileAsList(fileName):
    #read the stopwords file and build a list
    list = []
    fp = open(fileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        list.append(word)
        line = fp.readline()
    fp.close()
    return list

def buildTestVector(tweet):
    return preProcess(tweet) # takes dataset and returns a vector(combination of words)
#     testVector = []
#     for tweet in testset:
#         featureVector = preProcess(tweet)
#         for feature in featureVector:
#             testVector.append(feature)
#     return testVector
        
def featureVector_asString(featureVector):
    fv_str = ""
    for word in featureVector:
        fv_str = fv_str + word;
        fv_str = fv_str + " "
    fv_str = fv_str.rstrip()
    return fv_str

def getTweetFromCsv():
    tweet_list = []
    with open("/home/uday/MasterProject/Datasets/CompanyDataset/CSV/Akamai Technologies1.csv",'rb') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            tweet_list.append(row[0])
             
def prepare_traindata(): #POPULATES feature_list and featureAndSentiment
    print("building the train dataset....")
    with open("/home/uday/DjangoProjects/stocks/prediction/Sentiment/train_data.csv",'rb') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            tweet = row[0]
            sentiment = row[1]
            featureVector = preProcess(tweet)
            for feature in featureVector:
                feature_list.append(feature)
            featuresAndSentiment.append((featureVector,sentiment))
    csvfile.close()
    #return [feature_list,featuresAndSentiment]

def getSentiment(tweet,NBClassifier):
    test_featureVector = buildTestVector(tweet)
    sentiment = NBClassifier.classify(extract_features(test_featureVector))
    #print tweet,sentiment
    return sentiment

def getPosNeg_count(testData,NBClassifier): # this takes a dataset as input and returns count of +ve and _ve tweets
    global feature_list
    pos_count = 0
    neg_count = 0
    for tweet in testData:
        if(getSentiment(tweet,NBClassifier) == 'positive'):
            #print tweet
            pos_count = pos_count + 1
        else:
            neg_count = neg_count + 1
    return [pos_count,neg_count]

def getOverallPrediction(gen_posneg,anal_posneg):
    anl_weight = 70;
    gen_weight = 30;
    gen_tot = gen_posneg[0] + gen_posneg[1]
    anal_tot = anal_posneg[0] + anal_posneg[1]
    if(gen_tot == 0):
        gen_tot = 1
    if(anal_tot == 0):
        anal_tot = 1
    #print "gen tot: ",gen_tot
    #print "anal tot: ",anal_tot
    gen_pos_percent = gen_posneg[0]/float(gen_tot) *100
    result['gen_pos_percent'] = gen_pos_percent
    #print "gen_postitive_%: ",gen_pos_percent
    gen_neg_percent = float(gen_posneg[1]/float(gen_tot)) *100
    result['gen_neg_percent'] = gen_neg_percent
    #print "gen_negative_%: ",gen_neg_percent
    anal_pos_percent = float(anal_posneg[0]/float(anal_tot))*100
    result['anal_pos_percent'] = anal_pos_percent
    #print "anal_postitive_%: ",anal_pos_percent
    anal_neg_percent = float(anal_posneg[1]/float(anal_tot))*100
    result['anal_neg_percent'] = anal_neg_percent
    #print "anal_negative_%: ",anal_neg_percent
    positivity = float(gen_pos_percent * gen_weight + anal_pos_percent*anl_weight) / 100;
    result['positivity'] = positivity
    negativity = float(gen_neg_percent * gen_weight + anal_neg_percent*anl_weight) / 100;
    result['negaitivity'] = negativity
    #print positivity,negativity
    if(positivity >= negativity):
        return 'positive'
    else:
        return 'negative'

def train_classifier():
    training_set = nltk.classify.util.apply_features(extract_features, featuresAndSentiment)
    NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
    return NBClassifier
    

def getGen_data(): # gives a raw dataset of general user tweets
    gen_data = [ "Apple stock is on the rise",
             "Apple's flagship iphone7 due for release in September",
             "Phone sales of apple are increased by 50% compared to last year",
             "Samsung's new release would affect the iphone sales this quarter",
             "Apple continues its grand run at stock market",
             "bad worse ugly dirty down stopped negative"
             ]
    return gen_data

def getAnal_data(comp): # gives a raw dataset of analyst tweets
    anal_data = analTweets.grand_list_anal_tweets(comp)
    return anal_data

    

def getAnalysis(stock_name):
    #train the classifier
    prepare_traindata()
    NBClassifier = train_classifier()

    #apply the gen and analyst datasets one after other
    print "gathering user tweets..."
    testData_gen = tweets_db.getTweetsbyComp(stock_name)
    print "gathering expert tweets........"
    testData_anal = getAnal_data(stock_name)

    gen_posneg = getPosNeg_count(testData_gen,NBClassifier)
    print "preprocessing...."
    print "removing stop words..."
    print "Stemming the feature list..."
    print "performing sentiment analysis............"
    anal_posneg = getPosNeg_count(testData_anal,NBClassifier)
    sentiment = getOverallPrediction(gen_posneg, anal_posneg)
    print "fetching results....."
    result['sentiment'] = sentiment
    return result
