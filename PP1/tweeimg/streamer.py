import yaml
import tweepy
import urllib

class stream(object):

    """image stream using Twitter API"""

    def __init__(self, screen_name, buf_size = 10):

        keyfile = open("/home/yxiao1996/workspace/keys/twitter/keys.yaml")

        keys = yaml.load(keyfile)

        consumer_key = keys['consumer_key']

        consumer_secret = keys['consumer_secret']

        access_key = keys['access_token']

        access_secret = keys['access_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)

        self.api = tweepy.API(auth)

        self.screen_name = screen_name

        self.buf_folder = "/home/yxiao1996/workspace/EC601/PP1/tweeimg/imgs"

        self.buf_size = buf_size

    def streamImage(self):

        """Image Streaming Generator"""

        all_tweets = []

        new_tweets = self.api.user_timeline(screen_name = self.screen_name, count = 1)

        all_tweets.extend(new_tweets)

        current_id = all_tweets[0].id - 1

        count = 0

        while(len(new_tweets) > 0):

            try:

                # print new_tweets[0].entities['media'][0]['media_url']

                image_url = new_tweets[0].entities['media'][0]['media_url']

                image = urllib.urlopen(url = image_url).read()

                debug_file = open('./debug.jpg', 'wb')

                debug_file.write(image)

                count = (count + 1) % self.buf_size

                image_file = open(self.buf_folder + "/%03d" % count + ".jpg", 'wb')

                image_file.write(image)

                yield count, image

            except Exception as e:

                print "tweet does not contains image. ", e

            new_tweets = self.api.user_timeline(screen_name = self.screen_name, count = 1, max_id = current_id)

            if len(all_tweets) == self.buf_size:

                all_tweets = []

            all_tweets.extend(new_tweets)
            
            current_id = all_tweets[-1].id - 1

            # print len(all_tweets), current_id

            # if (len(all_tweets) > 20):

            #     break

if __name__ == "__main__":

    s = stream('@keinishikori')

    gen = s.streamImage()

    while(True):

        print gen.next()