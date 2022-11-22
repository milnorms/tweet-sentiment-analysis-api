# tweet-sentiment-analysis-api 🐥

API for tweet sentiment analysis frontend. Uses tweepy to request tweets from twitter and Vader Sentiment to return data on a tweet's sentiment based on a search query.

## Development 💻
1.              source env/bin/activate
2.              python app.py

### Tip 💡
Must add credentials to .env_example and rename file to .env for tweepy to work

## How to use api 👾
The first query arg (t) is search term, second (n) is number of tweets to be returned, third (w) is the number of word count words to be returned

        /api?t=from:elonmusk&n=100&w=50
