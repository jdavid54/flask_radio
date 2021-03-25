Lancer start_radio.sh dans un terminal

Ceci va lancer le serveur radio via Flask.
Flask est une application qui permet de lancer des programmes python
dans le serveur apache2 : /var/www/flask_dev/flask_dev

Ouvrir la page web : localhost:1234

Ceci va ouvrir l'interface de Flask Home FM !
Bonne écoute !

===========================================================
NOTES
===========================================================
1) radio.py
- radio.py utilise le programme mpc.exe pour écouter la radio
- la page utilise le template interface.html dans templates pour générer la page avec formulaire
- la page de style CSS styles.css est dans static
- start server : cd /var/www/flask_dev/flask_dev; sudo python radio.py
                 ou par shell : ~/Documents/divers/radio_flask/start_radio.sh
- accès à la page : localhost:1234 

2) flask_login.py
- la page utilise le template login.html dans templates
- start server :cd /var/www/flask_dev/flask_dev; sudo python flask_login.py
- accès à la page : localhost:5000/login

