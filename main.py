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

    # top_retweeted = get_most_tweets_retweeted(tweets, 10)

    # print('Top retweeted:')
    # for tweet in top_retweeted:
    #     print(tweet['content'])

    # print()

    # top_users = get_users_with_most_tweets(tweets, 10)

    # print('Top users:')
    # for user, ammount in top_users:
    #     print(f'{user}: {ammount} tweets')

    # print()

    # top_days = get_days_with_most_tweets(tweets, 10)

    # print('Top Days:')
    # for day, ammount in top_days:
    #     print(f'{day}: {ammount} tweets')

    # print()

    top_hashtags = get_top_hashtags(tweets, 10)

    print('Top Hashtags:')
    for ht, ammount in top_hashtags:
        print(f'{ht}: {ammount} times')

    print()


if __name__ == '__main__':
    main()
