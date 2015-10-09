import sys
import json

def goOverTweets():
    
    tweetFile = open(sys.argv[1])
    termFrequency = {}
    totalCount = 0;
    
    for line in tweetFile:
        tweet = json.loads(line)
        if 'text' in tweet:
            tweetWords = tweet["text"].encode('utf-8').split()
            for word in tweetWords:
                totalCount += 1;
                if not word in termFrequency:
                    termFrequency[word] = 1
                else:
                    termFrequency[word] += 1
                    
    for term, termCount in termFrequency.items():
        print str(term) + " " + str(float(termCount)/totalCount)
            

def main():
    goOverTweets()

if __name__ == '__main__':
    main()