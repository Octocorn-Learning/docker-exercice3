# Exercice 3 - Docker compose 🐋

L'objectif de cet exercice est de créer une stack pour le service dev de votre entreprise.
Il s'agit d'une petite application permettant d'afficher une liste de bières d'un magasin.

L'application contient 3 endpoints : 
- La liste complète des bières
- Le CA des principaux fabricants
- Les variations de ventes entre 2015 et 2016.

> Le développeur en charge vous confirme que 'ça marche sur sa machine'.

Vous avez à votre disposition : 
- un répertoire `api` qui contient le code source d'une API flask
- un répertoire `sql` qui contient de quoi créer une base de données MySQL contenant des données

Vous devez réaliser un fichier docker-compose qui permet de créer les conteneurs suivants :
- un conteneur MySQL
- un conteneur flask

## Attendus

- Vous devez créer les Dockerfiles nécessaires à la création des images
- Le docker-compose doit construire les images à partir des Dockerfiles
- 

## Aides : 


### API

- Le fichier `requirements.txt` contient les dépendances python nécessaires à l'API
- Il devra être copié dans le conteneur et installé avec la commande `pip install -r requirements.txt`
- L'API doit exposer sur le port `80`.
- Le conteneur doit exposer le port `5000`
- Vous devez utiliser l'image `python` comme image de base

### BDD

- Vous devez utiliser l'image `mysql` comme image de base
- Vous devez copier le fichier `beer.sql` dans l'entrypoint du conteneur MySQL

## Aides supplémentaires

Si vous avez besoin d'indices supplémentaires, vous pouvez vous tourner vers les fichiers suivants : 
- [Aides du poulet](./consignes/poulet.md) 🐔
- [Aides du poussin](./consignes/poussin.md) 🐣