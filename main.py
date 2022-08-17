from functions import (
    load_tweets,
    get_most_tweets_retweeted,
    get_users_with_most_tweets,
    get_days_with_most_tweets,
    get_top_hashtags,
)


FILENAME = 'farmers-protest-tweets-2021-03-5.json'


def main():

    tweets = load_tweets(FILENAME)

    top_retweeted = get_most_tweets_retweeted(tweets, 10)

    print('Top retweeted:')
    for tweet in top_retweeted:
        print(tweet['content'])

    print()


if __name__ == '__main__':
    main()
