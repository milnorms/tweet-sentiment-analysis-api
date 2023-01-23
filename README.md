# tweet-sentiment-analysis-api 🐥

API for tweet sentiment analysis frontend. Uses tweepy to request tweets from twitter and Vader Sentiment to return data on a tweet's sentiment based on a search query.

Inspired by [Presidential Debate Twitter Sentiment Analysis using Python and NLTK](https://www.youtube.com/watch?v=_EgqxIoUE7U&t=1239s&ab_channel=NicholasRenotte) by [nicknochnack](https://github.com/nicknochnack)

## Instructions 💾

### [Virtual Env](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv)

1. Install virtualenv

        python3 -m pip install --user virtualenv

2. Create a virtual environment

        python3 -m venv env

2. Activate virtual environment

        source env/bin/activate

### Install Packages

1. After virtual environment is activated, install packages

        pip3 install -r requirements.txt

### Environment Variables

1. Must add credentials to `.env_example` and rename file to `.env` for tweepy to work

## Development 💻
1.     source env/bin/activate
2.     python app.py


## How to use api 👾
The first query arg (t) is search term, second (n) is number of tweets to be returned, third (w) is the number of word count words to be returned

        /api?t=from:elonmusk&n=100&w=50

## Note 📝
1. App uses [Twitter API](https://developer.twitter.com/) v1 ONLY. v2 credentials will not work
