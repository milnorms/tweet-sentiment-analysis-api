from typing import Iterable

# Use environment variables
import os

# Load in .env
from dotenv import load_dotenv 

#default directory for .env file is the current directory
#if you set .env in different directory, put the directory address load_dotenv("directory_of_.env)
load_dotenv()


def _add_cors_headers(response, methods: Iterable[str], origin) -> None:
    DEV_ORIGIN = os.environ['DEV_ORIGIN']
    PROD_ORIGIN = os.environ['PROD_ORIGIN']

    allow_methods = list(set(methods))
    if "OPTIONS" not in allow_methods:
        allow_methods.append("OPTIONS")
    # Allowed origins to access api. Local dev host and deployment host
    allow_origins = [DEV_ORIGIN, PROD_ORIGIN]
    # If the origin isnt found, set default access to local dev origin
    if origin not in allow_origins:
            origin = DEV_ORIGIN

    headers = {
        "Access-Control-Allow-Methods": ",".join(allow_methods),
        "Access-Control-Allow-Origin": origin,
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Headers": (
            "origin, content-type, accept, "
            "authorization, x-xsrf-token, x-request-id"
        ),
    }
    response.headers.extend(headers)


def add_cors_headers(request, response):
    # Getting origin from request header
    origin = request.headers.get_all('origin')[0]
    if request.method != "OPTIONS":
        methods = [method for method in request.route.methods]
        _add_cors_headers(response, methods, origin)
