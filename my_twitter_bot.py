import tweepy
import time



CONSUMER_KEY = '2ybCqYyhRTRt7kCj99fgSzKn0'
CONSUMER_SECRET = 'zDMDgzOeMnTEkkLgPw3Vi8OHozC7dw1oI0Wb8LQmGDrIf5i2FE'
ACCESS_KEY = '1140892292615565317-4CizzMm0zJV39QTUwaIZhSVeFoiQVe'
ACCESS_SECRET = 'SbYQm6G3jcQo2pQVD7flGTnKeCf8VFpookNIE6mrb8AvI'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)

    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#Hello' in mention.full_text.lower():
            print('found #Hello!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#Hello back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)