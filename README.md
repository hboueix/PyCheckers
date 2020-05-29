# PyCheckers
Jeu de dames developpé en Python. Vous trouverez dans le fichier `documentation.pdf` des screens ainsi que le graphe UML de l'application.

## Prérequis

Il faut faut bien sûr Python (3.6+) installé sur votre machine.

## Installation

Il faut commencer par cloner ce dépôt bien sûr.  
Puis à la racine du dossier, tapez la commande:
```bash
make

# Si make n'est pas installé
pip install -r requirements.txt
```

Si vous avez des problèmes pour l'installation du package `mysql-connector-python-rf`, vérifiez déjà que vous avez bien MySQL ou MariaDB d'installé puis :

Linux Debian/Ubuntu :
```bash
# MySQL
sudo apt-get install libmysqlclient-dev

# MariaDB
sudo apt-get install libmariadbclient-dev
```

Windows :  
Il faut télécharger le 'mysql python connector' :
https://dev.mysql.com/downloads/connector/python/

## Utilisation

Vous pouvez désormais lancer le jeu. Pour ce faire, rendez-vous à la racine du dossier et lancez le jeu avec la commande :
```bash
python app/main.py
```
