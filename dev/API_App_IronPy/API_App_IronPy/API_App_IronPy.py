import yaml
import tweepy
import urllib
import os
import traceback

class stream(object):

    """image stream using Twitter API"""

    def __init__(self, screen_name, 
                 buf_folder = "./imgs",
                 key_path = "C:/Users/xiaoy/Documents/keys/twitter/key.yaml", 
                 buf_size = 10):

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

                # image = urllib.urlopen(url = image_url).read()

                #debug_file = open('./debug.jpg', 'wb')

                #debug_file.write(image)

                # Check if image file already exist
                #image_fn = self.buf_folder + "\\%03d" % count + ".jpg"
                #if (os.path.isfile(image_fn)):
                #    os.
                
                #image_file = open(image_fn, 'wb')

                #image_file.write(image)

                # debug_file.close()

                #image_file.close()

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
    print hello()

    try:
        gen = s.streamImage()
        #raw_input()
        while(True):

            print gen.next()
    except Exception as e:
        print e
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        raw_input()