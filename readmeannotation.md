# Segmentation to Polygon Labels

Ce projet automatise la conversion des masques binaires de segmentation en fichiers .txt contenant des labels sous forme de coordonnées de polygones normalisées. Cette approche est conçue pour simplifier et accélérer les processus d'annotation dans des frameworks de vision par ordinateur.
## Avantages
Gain de Temps :Automatisation complète du processus, évitant l'annotation manuelle fastidieuse dans des outils comme Roboflow.
Compatibilité : Les fichiers générés sont compatibles avec de nombreux frameworks d'entraînement et d'annotation d'images.
Facilité d'Utilisation : Intégration avec Google Colab et Google Drive pour une gestion simplifiée des fichiers.
Précision : Génération automatique de coordonnées précises, réduisant les erreurs humaines.

## But du Projet
Transformer des masques de segmentation en coordonnées de polygones normalisées dans des fichiers txt  pour des tâches de labellisation dans le domaine de la vision par ordinateur pour des modèles d'apprentissage supervisé.Ces fichiers .txt sont essentiels pour les applications nécessitant des annotations basées sur des polygones

## Technologies Utilisées

- **Python** : Langage principal.
- **OpenCV** : Pour le traitement des images et l'extraction des contours.
- **Google Drive** : Pour gérer les fichiers d'entrée et de sortie via Google Colab.

## Comment l'Exécuter

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/yasmine1log/annotation_project
   cd annotation_project

2. Assurez-vous que les répertoires masks et labels existent dans votre Google Drive

3. Exécutez le script dans Google Colab: 

Chargez le fichier annotation_data.py

Modifiez les chemins d'accès input_dir et output_dir pour qu'ils pointent vers vos répertoires sur Google Drive.

Exécutez le script.


## Résultats

Fichiers texte générés : Chaque masque génère un fichier .txt contenant les coordonnées du polygone.
