def app(environ, start_response):
    data = [bytes(i + '\n', 'utf8')
            for i in environ['QUERY_STRING'].split('&')]
    start_response("200 OK", [
        ("Content-Type", "text/plain")
    ])
    return iter(data)
