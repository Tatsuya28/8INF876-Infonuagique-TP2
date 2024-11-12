# Application de Gestion de Tâches

Il s'agit d'un projet réalisé en collaboration avec Thomas FRIDBLATT dans le cadre du cours **[8INF876] Conception et
Architecture des systèmes infonuagique** pour le TP2 à l'UQAC.
Cette application de gestion de tâches est une application web simple construite avec Django et MySQL.
Elle permet aux utilisateurs de créer, visualiser, mettre à jour et supprimer des tâches.
Le projet utilise Docker et Kubernetes pour le déploiement.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
- [Prérequis](#prérequis)
- [Installation en local](#installation-en-local)
- [Construction de l'image Docker](#construction-de-limage-docker)
- [Déploiement sur Kubernetes avec Minikube](#déploiement-sur-kubernetes-avec-minikube)
- [Accès à l'application](#accès-à-lapplication)
- [Structure du Projet](#structure-du-projet)

## Fonctionnalités

- Ajouter, visualiser, modifier et supprimer des tâches.
- Enregistrer des informations telles que le titre, la description, la date d'échéance, et le statut de chaque tâche.
- Gestion des utilisateurs avec authentification.

## Technologies utilisées

- **Backend** : Django (Python)
- **Base de données** : MySQL
- **Conteneurisation** : Docker
- **Orchestration** : Kubernetes (Minikube pour le développement local)
- **Interface utilisateur** : HTML/CSS
- **Outils de développement** : Git, GitHub

Pour plus d'informations sur les technologies utilisées, veuillez consulter les fichiers `requirements.txt`,
`Dockerfile` et `k8s/*.yaml`.

## Prérequis

- **Docker** : [Instructions d'installation](https://docs.docker.com/get-started/get-docker/)
- **Minikube** : [Instructions d'installation](https://minikube.sigs.k8s.io/docs/start/)
- **kubectl** : [Instructions d'installation](https://kubernetes.io/docs/tasks/tools/)

## Installation en local

1. Clonez le dépôt du projet :
   ```bash
   git clone https://github.com/Tatsuya28/8INF876-Infonuagique-TP2.git
   cd 8INF876-Infonuagique-TP2
    ```

2. Créez un environnement virtuel et installez les dépendances :

   Sous linux :
   ```bash
   python3 -m venv venv
   source venv/bin/activate # Pour activer l'environnement virtuel sur Linux
   pip install -r requirements.txt
   ```
   Sous Windows :
   ```bash
   python -m venv venv
   .\venv\Scripts\activate # Pour activer l'environnement virtuel sur Windows
   pip install -r requirements.txt
    ```

3. Créez une base de données MySQL nommée `gestion_taches_db`et configurez les paramètres dans le fichier
   `task_manager/settings.py` pour se connecter à MySQL:

4. Appliquez les migrations :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```
    L'application sera accessible à l'adresse `http://127.0.0.1:8000/`.

## Construction de l'image Docker

   ```bash
   docker build -t gestion-taches-frontend .
   ```

## Déploiement sur Kubernetes avec Minikube

1. Démarrez Minikube (si ce n'est pas déjà fait) :
   ```bash
   minikube start
   ```
   S'assurez que Minikube utilise l'environnement Docker :
   ```bash
   # Sous Linux
    eval $(minikube docker-env)
   ```
   ```bash
   # Sous Windows
   minikube docker-env
   @FOR /f "tokens=*" %i IN ('minikube -p minikube docker-env --shell cmd') DO @%i
    ```

2. Chargez l'image Docker dans Minikube :
   ```bash
   minikube image load gestion-taches-frontend
   ```

3. Appliquez les fichiers de configuration Kubernetes :
   ```bash
   kubectl apply -f k8s/
   ```
   Les ressources suivantes seront créées :
    - Un déploiement pour l'application Django
    - Un service pour exposer l'application
    - Un déploiement pour la base de données MySQL
    - Un service pour exposer la base de données

4. Obtenir l'url du service pour accéder à l'application :
   ```bash
   minikube service gestion-taches-frontend-service
   ```
   Suivez l'URL pour accéder à l'application Django déployée sur Kubernetes.

## Accès à l'application

Selon votre configuration, l'application sera accessible à l'une des adresses suivantes :
- En local : `http://127.0.0.1:8000/`
- Sur Minikube : URL obtenue avec `minikube service gestion-taches-frontend-service`

## Structure du Projet

```
8INF876-Infonuagique-TP2
    ├── TasksManager       # Dossier principal de l'application Django
    ├── k8s                # Fichiers de configuration Kubernetes
    ├── static             # Fichiers statiques (CSS, JS, images) pour l'interface utilisateur
    ├── tasks              # Application principale, contient les modèles, vues et formulaires
    ├── templates          # Modèles HTML pour l'interface utilisateur
    ├── Dockerfile         # Fichier pour construire l'image Docker de l'application
    ├── README.md          # Fichier README (que vous lisez actuellement)
    ├── manage.py          # Fichier principal de l'application Django
    └── requirements.txt   # Fichier contenant les dépendances Python requises

```