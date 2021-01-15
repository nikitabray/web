sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install gunicorn
sudo pip3 install django==2.0
sudo pip3 install mysqlclient

cd /home/box/web  
sudo nginx -c /home/box/web/etc/nginx.conf  
python3 /home/box/web/ask/manage.py runserver 0.0.0.0:8000

sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
python3 ~/web/ask/manage.py makemigrations
python3 ~/web/ask/manage.py migrate
