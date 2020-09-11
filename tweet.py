import tweepy
import time

auth = tweepy.OAuthHandler('aJARMPxHO1IbUEAgyKvVC0BUQ',
                           'qoHzHOcJq9x3mTkE0kRtjJnSHcWHS6s3NOstGSn8WArvuIsMS4')
auth.set_access_token('1304528923414290432-Mm6p1m42UkJOvQ0DpTNg72jeOibJWx',
                      'gL3GN9M876IB22x4ehOm5QeUkDhDNRONYTm5IEKmlAjIj')

api = tweepy.API(auth)
user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)

search_string = 'python'
numbersOfTweets = 2


def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except:
            time.sleep(1)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Usernamehere':
        print(follower.name)
        follower.follow()


for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet!!')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
