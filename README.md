# Twitter Sentiment Analysis
> Data Manipulation at Scale: Systems and Algorithms

The following is my Python assignment turn-ins on the ["Data Manipulation at Scale: Systems and Algorithms"](https://www.coursera.org/learn/data-manipulation) at Coursera (taught at University of Washington). 

The class goes in depth to the application of statistics and structures in the technology field to organize and find correlations on data, starting off with relational algebra (an abstraction) and its implementation (Structured Query Language - SQL - used at relational databases that powers apps and websites). It then proceeds to certain algorithms like [MapReduce](http://research.google.com/archive/mapreduce.html) that is pioneered by Google (and open-source, free software systems like [Apache Hadoop](https://hadoop.apache.org) that make it a reality) and non-SQL databases (the NoSQL movement) that do not use SQL (making them harder to use and a focus on doing things manually when storing data) but with the benefit of scalability - databases can now be on multiple servers.

This assignment has 6 parts:
  
* In `twitterstream.py`, live tweets that are created are grabbed while the file is running and stored on an output file.
* In `tweet_sentiment.py`, based on a dictionary of words - [AFINN](www2.imm.dtu.dk/pubdb/views/public) - that have positive and negative connotations (given a positive/negative score), a tweet is given a certain positive or negative connotation based on the amount of negative/positive connotations on that tweet.
* In `term_sentiment.py`, words that don't have positive/negative connotations like the ones listed on the AFINN list, are given one based on their frequence of use with words that do have a positive/negative connotation on the AFINN list.
* In `frequency.py`, the frequency of each word in all the streaming tweets gathered, are outputted.
* In `top_ten.py`, the top 10 hash tags currently on the list of streaming tweets are obtained.
* In `happiest_state.py`, the "happiest" state in the US are determined based on the compounded sentiment scores of tweets for each state in the US.

To make these files run on your computer, make sure you have Python installed and using the command line/terminal, run 

`python <oneOfThePythonFilesHere> <additionalArgumentsNeeded>`

You need to specify your own Twitter API keys and secrets (if you go to `twitterstream.py`, fill the `api_key`, `api_secret`, `access_token_key`, `access_token_secret` variables) by going to the [Twitter Developer Center](https://dev.twitter.com) and signing up to make a Twitter app. You will get values you can fill in for those variables after signing up. My stuff were there, but I didn't want my secret tokens up in the inter webs for security.