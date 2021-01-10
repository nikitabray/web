sudo nginx -c /home/box/web/etc/nginx.conf && cd ask && gunicorn --bind 0.0.0.0:8000 ask.wsgi
