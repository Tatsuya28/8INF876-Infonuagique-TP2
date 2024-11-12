# Utiliser l'image officielle de Python 3.13 comme image de base
FROM python:3.13-slim

# Mettre à jour les paquets et installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libmariadb-dev-compat \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le contenu du répertoire local dans le répertoire de travail
COPY . .

# Exposer le port sur lequel notre application Django s'exécute
EXPOSE 8000

# Exécuter les commandes de migrations et démarrer le serveur
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]