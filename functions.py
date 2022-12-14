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
    )[:n]

    with_count = [
        (tweet['content'], tweet['retweetCount'])
        for tweet in retweeted
    ]

    return with_count


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
    hashtags = defaultdict(int)
    for tweet in tweets:
        aux = tweet['content'].split()
        hashtags_in_tweet = filter(
            lambda word: word.startswith('#'),
            aux
        )
        for hashtag in hashtags_in_tweet:
            hashtags[hashtag] += 1

    top = sorted(
        hashtags.items(),
        key=lambda hashtag: hashtag[1],
        reverse=True
    )

    return top[:n]
