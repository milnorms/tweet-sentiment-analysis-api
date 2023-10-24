# Import function to generate tweet sentiment analysis data
from tweetSentimentAnalysis import getTweetData
# Import sanic for api endpoint and handling requests
from sanic import Sanic
from sanic.response import json
# Import os for env variables
import os
# help with CORS
from cors import add_cors_headers
# Load in .env
from dotenv import load_dotenv 

#default directory for .env file is the current directory
#if you set .env in different directory, put the directory address load_dotenv("directory_of_.env)
load_dotenv()

# to run: source env/bin/activate && python app.py
# 1. source env/bin/activate
# 2. python app.py

# before deploying to save venv packages: https://stackoverflow.com/questions/8073097/how-to-freeze-packages-installed-only-in-the-virtual-environment
# pip freeze -l > requirements.txt

# Git venv guide: https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde

# Flag for dev environment
IS_DEV = bool(os.environ['IS_DEV']) == True

app = Sanic("app")

async def getData(term, numItems, numWordCount):
    '''
    Async wrapper for getTweetData()
    '''
    return getTweetData(term, numItems, numWordCount)

# webapp path defined used route decorator
@app.route("/api")
async def run(request):
    # First query arg is search term, second is number of tweets to be returned, third is the number of word count words to be returned
    # eg. http://0.0.0.0:8000/api?t=from:elonmusk&n=100&w=50
    print(request.query_args)
    term = request.query_args[0][-1]
    numItems = int(request.query_args[1][-1])
    numWordCount = int(request.query_args[2][-1])
    data = await getData(term, numItems, numWordCount)
    return json(data)

# Fill in CORS headers
app.register_middleware(add_cors_headers, "response")

# Check if running in dev environment (from .env file)
if IS_DEV:
    # Running app with env variables for development 
    app.run(
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 8000)),
    workers=int(os.environ.get('WEB_CONCURRENCY', 1)),
    debug=bool(os.environ.get('DEBUG', True)),
    auto_reload=True
    )
else:
    # Run settings for prod/ssl environment
    ssl = {
        'cert': '/home/milnorms.rocks.chained.crt',
        'key': '/home/milnorms.rocks.key'
    }

    app.run(
        host='0.0.0.0',
        port=8443,
        ssl=ssl,
        workers=int(os.environ.get('WEB_CONCURRENCY', 1)),
        debug=bool(os.environ.get('DEBUG', True)),
        auto_reload=True
    )