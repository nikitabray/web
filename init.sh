cd /home/box/web  
sudo nginx -c /home/box/web/etc/nginx.conf  
sudo gunicorn -c /home/box/web/etc/gunicorn_hello.conf --bind 0.0.0.0:8080 hello:app &
cd ask 
sudo gunicorn -c /home/box/web/etc/gunicorn_django.conf ask.wsgi:application &
