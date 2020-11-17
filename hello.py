def app(environ, start_response):
    data = [bytes(i + '\n', 'utf8')
            for i in environ['QUERY_STRING'][2:].split('&')]
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return data

# print(app({'QUERY_STRING': '/?a=1&a=2&b=3'}))
