from twitter import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import unicodedata
import argparse


consumer_key = "jkqVd4CcQgAB3YbA6faropijy"
consumer_secret = "c3hNMooL5RL48ge4QLy3x2zfly7ibvaa5HTPUqvoBn2Nmm7QZN"
access_token = "149064720-eismGSy19FVRO7HAUoVnbYuqufrMXA8kasAK3pu9"
access_token_secret = "A6N3Eaa6CDuFaDMhMG0mo6KJHYYYWVK82VsBeb8Jkv7Fj"


t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
parser = argparse.ArgumentParser()

parser.add_argument("searchList", nargs='?', default="check_for_empty_string")

args = parser.parse_args()



if args.searchList == 'check_for_empty_string':
    print ('No argument passed. #demonetization as Default')
    searchTerms = ['#demonetization']
else:

    searchTerms = args.searchList.split(",")



for terms in searchTerms:

    q = terms



    count = 250

    search_results = t.search.tweets(q=q, count=count,lang='en')

    statuses = search_results['statuses']

text = ""



for status in statuses:

    text = text + status['text']

print (text)

text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
sent = TextBlob(text.decode(encoding="utf-8"))

polarity = sent.sentiment.polarity

subjectivity = sent.sentiment.subjectivity

keyword = q



sent = TextBlob(text.decode('utf-8'), analyzer=NaiveBayesAnalyzer())

classification = sent.sentiment.classification

p_pos = sent.sentiment.p_pos

p_neg = sent.sentiment.p_neg

tweetcount = count

senttype = 'twitter'

print("positive sentiment"+str(p_pos))
print("negative sentiment"+str(p_neg))