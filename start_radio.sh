#!/bin/bash

# run method 1
export FLASK_ENV=developement
cd /var/www/flask_dev/flask_dev
sudo python radio.py 
# http://localhost:1234/

# run method 2
#cd /var/www/flask_dev/flask_dev
#export FLASK_APP=radio.py
#env
#flask run
# http://localhost:5000/ls -