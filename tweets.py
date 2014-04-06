import json
import re

file_name = "tweets.json"
with open(file_name) as f:
	content = f.read()


#####################################################################################
# This method recursively strips a tweet of the initial RT, MT that it might have- 
# thus reducing it to the bare minimum it originally contained
######################################################################################
def strip_string(tweet):
	garbage = ['RT @', 'MT']
	for x in garbage:
		index = tweet.find(x)
		if index >= 0:
			tweet = tweet[index:]
			new_index = tweet.find(':')
			tweet = strip_string(tweet[new_index+2:])

	return tweet

# The following method takes in a dictionary and returns a tuple of the form (popular_tweet, no. of appearances)
def get_most_popular_tweet(tweetd):
	max_count = 0
	pop_tweet = ""
	for tweet in tweetd:
		count = tweetd[tweet]
		if count > max_count:
			max_count = count
			pop_tweet = tweet

	return (pop_tweet, max_count)

json_str = json.loads(content)
print json_str['tweets'][1]['text']
print strip_string(json_str['tweets'][1]['text'])

tweets = []
tweetd = {}
for tweet in json_str['tweets']:
	text = strip_string(tweet['text'])
	if text in tweetd:
		tweetd[text] = tweetd[text]+1
	else:
		tweetd[text] = 1
	tweets.append(text)

# Uncomment next two lines to see the list and dictionary that contain the tweets
# print tweets
# print tweetd

print "no.of tweets- " + str(len(tweets))
print "no of distinct tweets- " + str(len(tweetd))

# The following prints out the most common tweet with number of appearances in data
(pop_tweet, max_count) = get_most_popular_tweet(tweetd)
print "most popular tweet is \""+ pop_tweet +"\" with " +str(max_count) + " number of appearances" 

