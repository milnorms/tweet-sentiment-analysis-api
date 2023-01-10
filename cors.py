from typing import Iterable


def _add_cors_headers(response, methods: Iterable[str], origin) -> None:
    allow_methods = list(set(methods))
    if "OPTIONS" not in allow_methods:
        allow_methods.append("OPTIONS")
    print(f'Provided origin ===>>> {origin}')
    # Allowed origins to access api. Local dev host and deployment host
    allow_origins = ["http://localhost:3000", "https://tweet-sentiment-webapp.vercel.app"]
    # If the origin isnt found, set default access to local dev origin
    if origin not in allow_origins:
            origin = "http://localhost:3000"
    print(f'ALLOWED ORIGIN ===>>> {origin}')
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
    # print(f'URLLL => {request.url}')
    # print(f'PATHHHH => {request.path}')
    # Getting origin from request header
    origin = request.headers.get_all('origin')[0]
    print(f'ORIGIN => {origin}')
    if request.method != "OPTIONS":
        methods = [method for method in request.route.methods]
        _add_cors_headers(response, methods, origin)
