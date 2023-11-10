# Exercice 3 - Docker compose : Aides du poussin

## Les Dockerfiles

Vous devrez constituer deux `Dockerfile`, un pour chaque service (API et BDD).
Vous placerez ces fichiers dans les répertoires `api` et `sql`.

### API

- Vous déclarerez l'image de base `python`
- Vous définirez le répertoire de travail `/app`
- Vous exposerez le port `5000`
- Vous copierez les éléments du répertoire courant (`./app`) dans le répertoire de travail
- Vous installerez les dépendances avec `pip install -r requirements.txt`
- Vous démarrerez le serveur flask avec la commande `flask run --host=[0.0.0.0]`

> NB : La commande CMD a la syntaxe suivante : `CMD [<instruction>, <instruction>, ...]`

### BDD

- Vous déclarerez l'image de base `mysql`

- La documentation précise que tous les fichiers `.sh`, `.sql` et `.sql.gz` présents dans le répertoire `docker-entrypoint-initdb.d` sont automatiquement exécutés au démarrage du conteneur. Placez donc le fichier `beer.sql` dans ce répertoire.

> La documentation de l'image mysql est disponible [ici](https://hub.docker.com/_/mysql)

## Le docker-compose

Vous définirez deux services :
- `api` : le service flask
- `db` : le service mysql

### API

- Vous définirez le nom du conteneur : `api-beers` avec l'instruction `container_name`
- Vous indiquerez l'emplacement de votre Dockerfile avec l'instruction `build`
- Vous exposerez le port `5000` avec l'instruction `ports`
- Vous définirez une dépendance avec le service `db` avec l'instruction `depends_on`

### BDD

La documentation précise aussi que les variables d'environnement suivantes sont nécessaires :
- `MYSQL_ROOT_PASSWORD` : spécifie le mot de passe qui sera défini pour le compte MySQL root (c'est une variable obligatoire).
- `MYSQL_DATABASE` : spécifie le nom de la base de données à créer au démarrage de l'image.

- Vous définirez le nom du conteneur : `db-beers` avec l'instruction `container_name`
- Vous préciserez les variables d'environnement avec l'instruction `environment`
- Le port par défaut est précisé sur la documentation : `3307`