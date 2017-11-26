import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

c_key = 'dqxAS98lL8LrNx39r2ZskpW1v'
c_secret = 'yWDV0OwRNPueQ5rlSOX16z8vizCxHpVZYysieQN1p7XjedVl8i'
a_token = '2932809738-YhRPrZjMm09nmTbvjqOfbFbBbqHG0cBtR5ryPfN'
a_secret = 'IauTeanhBAe2nRGZOiWmvte3w0rUtwNNDOhYZWKpdj4do'


auth = OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_secret)

api = tweepy.API(auth)

#for status in tweepy.Cursor(api.friends).items(10):
#	print(status._json)


class MyListener(StreamListener):

	def on_data(self, data):
		try:
		 print(data)
		 with open('project.json', 'a') as f:
		   f.write(data)
		   return True
		except BaseException as e:
		 print('error on_data: %s ' % str(e))
		 return True   

	def on_error(self, status):
		print(status)
		return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])

