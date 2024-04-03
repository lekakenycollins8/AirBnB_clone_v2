#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

#install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#create HTML file
dir="/data/web_static/releases/test"
html_file="$dir/index.html"
html_content='<!DOCTYPE html>
<html>
	<head></head>
	<body>
		<h1>Hello World!</h1>
		<p>This is a test page to for nginx configuration</p>
	</body>
</html>'

echo "$html_content" | sudo tee "$html_file" >/dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}'  /etc/nginx/sites-enabled/default

sudo service nginx restart

