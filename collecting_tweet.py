# -*- coding: utf-8 -*-

import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import numpy as np
import urllib
import cv2
import matplotlib.pyplot as plt
import urllib, cStringIO
from PIL import Image
import matplotlib.pyplot as plt
import os

#authentification 
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler('AD6rmHWDJgY3iedL61Xk8GNMb', 'QY4dLkviRpJQhqJbC9dfYTin7Y3i3LeqeSTD6A5VX2bR7ccX3L')
auth.set_access_token('839010049364152320-bimf6EllaiKASyNMocs5cg7SnIZnlly', '7ZNXaBLhvtXiiohdmSh65RyaWnAhNjofyCYRQLZ7G5QzY')

auth = tweepy.AppAuthHandler('AD6rmHWDJgY3iedL61Xk8GNMb', 'QY4dLkviRpJQhqJbC9dfYTin7Y3i3LeqeSTD6A5VX2bR7ccX3L')
 
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

list_of_tweets = []

''' streaming API
nb_tweets = 5

#define tweepy class to parse tweet     
class MyListener(StreamListener):
    
    def __init__(self, api=None):
        super(MyListener, self).__init__()
        self.count = 0
    
    def on_data(self, data):
        global list_of_tweets
        if self.count<nb_tweets:
            try:
#code commented : open a file and write the tweets in it
#                with open('/home/lucas/NII/python.json', 'a') as f:
#                    f.write(data)
                    self.count=self.count+1
                    list_of_tweets.append(data)
                    print(self.count)
                    return True
            except BaseException as e:
                print(str(e))
                return True
        else:
            return False
 
    def on_error(self, status):
        print(status)
        return True

#initialize streaming tool
twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#twitter'])

#filter tweets in japanese with words : \u96e8 : 雨 (ame, rain), \u96eA : 雪 (yuki, snow)
twitter_stream.filter(languages=['ja'],track=[u'\u96e8',u'\u96eA'])
#twitter_stream.filter(languages=['en'],track=['snow'])

#extract text from json list created

json_string = str(list_of_tweets[0])
parsed_json = json.loads(json_string)
print(parsed_json['text'])

'''
count=0
z=7
for tweet in tweepy.Cursor(api.search,q='#guyane',since='2017-03-24',until='2017-03-29').items():
    list_of_tweets.append(tweet._json)
    count = count+1
    #code commented : open a file and write the tweets in it
    
    file_name = "%04d" % z
    path_name = "/home/lucas/NII/guyane/guyane"+file_name+".json"

    with open(path_name, 'a') as f:
            json.dump(tweet._json, f)
            f.write('\n')
            if count == 100:
                print(count)
                count=0
    if os.path.getsize(path_name)>10655202:
        z=z+1
        

#folder = '/home/lucas/NII/data/english_2/'
#z=0
#for i in range(len(list_of_tweets)):
##    data = json.loads(list_of_tweets[i])
#    data = list_of_tweets[i]
#
#    if 'media' not in data['entities']:
#        print(i)    
#    
#    else:
##        if (json.loads(list_of_tweets[i])['entities']['media'][0]['type']==u'photo'):
#        if ((list_of_tweets[i])['entities']['media'][0]['type']==u'photo'):
#
#            z=z+1
#            file_name = "%05d.jpg" % z
##            url = json.loads(list_of_tweets[i])['entities']['media'][0][u'media_url']
#            url = (list_of_tweets[i])['entities']['media'][0][u'media_url']
#
#            urllib.urlretrieve(url, folder+file_name)
#            
#            resp = urllib.urlopen(url)
##            image = np.asarray(bytearray(resp.read()), dtype="uint8")
##            ge = cv2.imdecode(image, cv2.IMREAD_COLOR)
##            plt.imshow(ge)
#            file = cStringIO.StringIO(urllib.urlopen(url).read())
#            img = Image.open(file)
#            plt.imshow(img)
#            plt.figure()



#for i in range(250,450):
#    print(list_of_tweets[-i]['text'])
#    print('\n')
#    
#data = []
#with open('/home/lucas/NII/guyane2.json') as f:
#    for line in f:
#        data.append(json.loads(line))
#        
#        
#json.loads('/home/lucas/NII/guyane2.json')
