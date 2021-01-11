sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
python3 ~/web/ask/manage.py makemigrations
python3 ~/web/ask/manage.py migrate
