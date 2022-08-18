from functions import (
    load_tweets,
    get_most_tweets_retweeted,
    get_users_with_most_tweets,
    get_days_with_most_tweets,
    get_top_hashtags,
)


FILENAME = 'farmers-protest-tweets-2021-03-5.json'
AMMOUNT = 10


def main():

    tweets = load_tweets(FILENAME)

    functions = [
        (get_most_tweets_retweeted, 'Top retweeted:'),
        (get_users_with_most_tweets, 'Top users:'),
        (get_days_with_most_tweets, 'Top days:'),
        (get_top_hashtags, 'Top hashtags:')
    ]

    for function, title in functions:
        top = function(tweets, AMMOUNT)
        print(title)
        for entity, ammount in top:
            print(f'{entity}: {ammount} times')
        print()


if __name__ == '__main__':
    main()
