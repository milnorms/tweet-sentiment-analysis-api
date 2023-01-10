from typing import Iterable


def _add_cors_headers(response, methods: Iterable[str], host) -> None:
    allow_methods = list(set(methods))
    if "OPTIONS" not in allow_methods:
        allow_methods.append("OPTIONS")
    # Allowed origins to access api. Local dev host and deployment host
    allow_origins = ["http://localhost:3000", "https://tweet-sentiment-webapp.vercel.app"]
    # If the host isnt found, set default access to local dev host
    if host not in allow_origins:
            host = "http://localhost:3000"

    print(f'ALLOWED HOST ===>>> {host}')
    headers = {
        "Access-Control-Allow-Methods": ",".join(allow_methods),
        "Access-Control-Allow-Origin": host,
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Headers": (
            "origin, content-type, accept, "
            "authorization, x-xsrf-token, x-request-id"
        ),
    }
    response.headers.extend(headers)


def add_cors_headers(request, response):
    # print(f'THINGGGGG => {request.host}')
    host = request.host
    if request.method != "OPTIONS":
        methods = [method for method in request.route.methods]
        _add_cors_headers(response, methods, host)
