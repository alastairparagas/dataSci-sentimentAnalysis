import sys
import json

sentimentScores = {}
    
def afinnSentimentBuildup():
    afinnFile = open(sys.argv[1])
    for line in afinnFile:
        term, score  = line.split("\t")
        sentimentScores[term] = int(score)


def goOverTweets():
    
    tweetFile = open(sys.argv[2])
    newSentimentScores = {}
    
    for line in tweetFile:
        tweet = json.loads(line)
        tweetSentimentScore = 0;
        if 'text' in tweet:
            
            tweetWords = tweet["text"].encode('utf-8').split()
            
            # Calculate Total Sentiment Score of Tweet
            for word in tweetWords:
                if word in sentimentScores:
                    tweetSentimentScore += sentimentScores[word]
            
            # For words not in the sentiment score listing, calculate
            # a sentiment score
            for word in tweetWords:
                if not word in sentimentScores:
                    if not word in newSentimentScores:
                        newSentimentScores[word] = float(tweetSentimentScore) / len(tweetWords)
                    else:
                        newSentimentScores[word] += float(tweetSentimentScore) / len(tweetWords)
                    
    for newSentimentWord, newSentimentWordScore in newSentimentScores.items():
        print str(newSentimentWord) + " " + str(newSentimentWordScore)
            

def main():
    afinnSentimentBuildup()
    goOverTweets()

if __name__ == '__main__':
    main()