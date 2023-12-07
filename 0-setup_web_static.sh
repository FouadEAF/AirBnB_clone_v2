#!/usr/bin/env bash
# Script that configures Nginx server with some folders and files
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello world!" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\
     \tlocation /hbnb_static/ {\
     \t\talias /data/web_static/current/;\
     \t\tautoindex off;\
     \t}\
     ' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
