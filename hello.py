def app(environ, start_response):
    data = environ['QUERY_STRING'][2:].split('&')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

# print(app({'QUERY_STRING': '/?a=1&a=2&b=3'}))
