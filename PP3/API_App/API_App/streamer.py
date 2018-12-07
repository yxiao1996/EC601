import yaml
import tweepy
import urllib
import os

class stream(object):

    """image stream using Twitter API"""

    def __init__(self, screen_name, 
                 buf_folder = "./imgs",
                 key_path = "C:/Users/xiaoy/Documents/keys/twitter/key.yaml", 
                 buf_size = 1):

        keyfile = open(key_path)

        keys = yaml.load(keyfile)

        consumer_key = keys['consumer_key']

        consumer_secret = keys['consumer_secret']

        access_key = keys['access_token']

        access_secret = keys['access_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)

        self.api = tweepy.API(auth)

        self.screen_name = screen_name

        self.buf_folder = buf_folder

        self.buf_size = buf_size

        # Create buffer directory
        if (not os.path.isdir(buf_folder)):
            os.mkdir(buf_folder)

        self.cur_tweet = None

    def streamImage(self):

        """Image Streaming Generator"""

        all_tweets = []

        new_tweets = self.api.user_timeline(screen_name = self.screen_name, count = 1)

        all_tweets.extend(new_tweets)

        current_id = all_tweets[0].id - 1

        count = 0

        while(len(new_tweets) > 0):

            try:

                # try to download image from tweet

                image_url = new_tweets[0].entities['media'][0]['media_url']

                self.cur_tweet = new_tweets[0]

                count = (count + 1) % self.buf_size

                yield image_url

            except Exception as e:

                pass
                #print "tweet does not contains image. ", e

            new_tweets = self.api.user_timeline(screen_name = self.screen_name, count = 1, max_id = current_id)

            if len(all_tweets) == self.buf_size:

                all_tweets = []

            all_tweets.extend(new_tweets)
            
            current_id = all_tweets[-1].id - 1

            # print len(all_tweets), current_id

            # if (len(all_tweets) > 20):

            #     break

def hello():
    return "Hello from streamer!"

if __name__ == "__main__":

    s = stream('@keinishikori')

    gen = s.streamImage()

    while(True):

        print gen.next()