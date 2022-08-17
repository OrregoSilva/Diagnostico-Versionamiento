import json
from collections import defaultdict


def load_tweets(filename):
    with open(filename, 'r') as file:
        tweets = [
            json.loads(line) for line in file
        ]

    return tweets


def get_most_tweets_retweeted(tweets, n):
    retweeted = sorted(
        tweets,
        key=lambda tweet: tweet['retweetCount'],
        reverse=True
    )

    return retweeted[:n]


def get_users_with_most_tweets(tweets, n):
    users = defaultdict(int)
    for tweet in tweets:
        users[tweet['user']['username']] += 1

    top = sorted(
        users.items(),
        key=lambda user: user[1],
        reverse=True
    )

    return top[:n]


def get_days_with_most_tweets(tweets, n):
    days = defaultdict(int)
    for tweet in tweets:
        # format date is YYYY-MM-DDTHH:MM:SS+00:00
        # only need YYYY-MM-DD -> 10 chars
        days[tweet['date'][:10]] += 1

    top = sorted(
        days.items(),
        key=lambda day: day[1],
        reverse=True
    )

    return top[:n]


def get_top_hashtags(tweets, n):
    pass
