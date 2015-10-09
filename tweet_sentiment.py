import sys
import json

sentimentScores = {}
    
def afinnSentimentBuildup():
    afinnFile = open(sys.argv[1])
    for line in afinnFile:
        term, score  = line.split("\t")
        sentimentScores[term] = int(score)
        
def rateTweets():
    tweetFile = open(sys.argv[2])
    for line in tweetFile:
        tweet = json.loads(line)
        sentimentScore = 0;
        if 'text' in tweet:
            for word in tweet["text"].encode('utf-8').split():
                if word in sentimentScores:
                    sentimentScore += sentimentScores[word]
        print sentimentScore;

def main():
    afinnSentimentBuildup()
    rateTweets()

if __name__ == '__main__':
    main()
