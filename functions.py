import json


def load_tweets(filename):
    with open(filename, 'r') as file:
        tweets = [
            json.loads(line) for line in file
        ]

    return tweets


def get_most_tweets_retweeted(tweets, n):
    retweeted = sorted(
        tweets,
        key=lambda tweet: tweet['retweetCount']
    )

    return retweeted[-n:]


def get_users_with_most_tweets(tweets, n):
    pass


def get_days_with_most_tweets(tweets, n):
    pass


def get_top_hashtags(tweets, n):
    pass
