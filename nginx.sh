
# How to config
# https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/

# How to config for Gunicorn
# http://docs.gunicorn.org/en/stable/deploy.html

# Config example
# https://www.nginx.com/resources/wiki/start/topics/examples/full/


# Start a nginx server
sudo nginx

# For mac OS
ls /usr/local/etc/nginx

# Create a symbolic link if not exists
ln -sfn /usr/local/etc/nginx $(pwd)  
# Edit the nginx.conf file
# type sudo nginx 

# stop nginx 
sudo nginx -s stop

# restart nginx 
sudo nginx -s reload