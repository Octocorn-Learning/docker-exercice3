# Exercice 3 - Docker compose : Aides du poussin

Les responsabilités des différents fichiers : 

- Les `Dockefile` permettent de construire les images. Ils copient les contenus et installent les dépendances
- Le `docker-compose.yml` permet de créer les conteneurs à partir des images construites précédemment. Il définit les ports à exposer et les variables d'environnement, ainsi que les dépendances entre les conteneurs.

## Les Dockerfiles

Vous devrez constituer deux `Dockerfile`, un pour chaque service (API et BDD).
Vous placerez ces fichiers dans les répertoires `api` et `sql`.

### API

- Vous déclarerez l'image de base `python`
- Vous définirez le répertoire de travail
- Vous exposerez le port `5000`
- Vous copierez les éléments du répertoire
- Vous installerez les dépendances avec `pip install -r requirements.txt`
- Vous démarrerez le serveur flask avec la commande `flask run --host=[0.0.0.0]`

> NB : La commande CMD utilise un tableau !

### BDD

- Vous déclarerez l'image de base `mysql`
- La documentation précise l'**entrypoint** du conteneur

> La documentation de l'image mysql est disponible [ici](https://hub.docker.com/_/mysql)

## Le docker-compose

Vous définirez deux services :
- `api` : le service flask
- `db` : le service mysql

### API

- Vous définirez le nom du conteneur.
- Vous indiquerez l'emplacement de votre Dockerfile.
- Vous exposerez le port `80` coté hôte.
- Vous définirez une dépendance avec le service `db`.

### BDD

- Vous définirez le nom du conteneur : `db-beers`.
- Vous préciserez les variables d'environnement.