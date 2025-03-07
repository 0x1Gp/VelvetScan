`APTDork` :

---

# APTDork - Dorking Tool

## Présentation

**APTDork** est un outil de **dorking** conçu pour effectuer des tests de présence de fichiers spécifiques ou de chemins sur des sites web. Il est particulièrement utile pour les tests de reconnaissance et l'identification de fichiers vulnérables dans le cadre d'audits de sécurité ou de reconnaissance. Ce script prend en charge la recherche de fichiers génériques (comme PHP, HTML, JS) ainsi que des chemins WordPress spécifiques.

Le script utilise la bibliothèque `requests` pour envoyer des requêtes HTTP et vérifier les réponses des fichiers cibles. Il prend en charge les erreurs HTTP courantes (404, 403, 500, etc.) et consigne les résultats dans un fichier de log pour une consultation ultérieure.

## Fonctionnalités

- Recherche de fichiers génériques (PHP, HTML, JS, XML, SQL) sur un site.
- Recherche de chemins WordPress via un fichier de chemins spécifique.
- Délai configurable entre chaque requête pour éviter de surcharger le serveur.
- Enregistrement des résultats dans un fichier de log détaillant les erreurs et succès.
- Affichage en couleur dans la console pour faciliter la lecture des résultats.

## Installation

1. Clonez le dépôt ou téléchargez les fichiers nécessaires.
2. Assurez-vous d'avoir Python installé (version 3.x recommandée).
3. Installez les dépendances avec la commande suivante :
   ```bash
   pip install requests
   ```

## Commandes



















### Description des options

Vous pouvez utiliser plusieurs options pour exécuter le script selon vos besoins. Voici les arguments disponibles pour exécuter le script :

- `-u`, `--url` : **URL du site cible** (Obligatoire)  
  L'URL du site web que vous souhaitez tester.  
  Exemple : `-u http://example.com`

- `-f`, `--file_type` : **Type de fichier à rechercher** (Optionnel)  
  Le type de fichier à tester sur le site. Vous pouvez spécifier l'un des types suivants :  
  - `php`
  - `html`
  - `js`
  - `xml`
  - `sql`  
  Exemple : `-f php`

- `-wp`, `--wordpress_file` : **Fichier de chemins WordPress** (Optionnel)  
  Chemin vers un fichier texte contenant des chemins WordPress à tester. Chaque chemin doit être sur une ligne différente.  
  Exemple : `-wp /path/to/wordpress.txt`

- `-t`, `--time` : **Temps entre les requêtes (en secondes)** (Obligatoire)  
  Le délai entre chaque requête HTTP envoyée au serveur. Cela permet de limiter la charge du serveur.  
  Exemple : `-t 2` (délai de 2 secondes)

- `-n`, `--number_of_pages` : **Nombre maximum de pages à tester** (Optionnel)  
  Le nombre maximum de pages à tester sur le site. Par défaut, le script teste jusqu'à 5 pages.  
  Exemple : `-n 10` (tester jusqu'à 10 pages)

### Exemple d'utilisation

1. **Tester un site pour des fichiers PHP** :
   ```bash
   python aptdork.py -u http://example.com -f php -t 2 -n 5
   ```

   Ce commande teste le site `http://example.com` pour des fichiers PHP, avec un délai de 2 secondes entre chaque requête et un maximum de 5 pages à tester.

2. **Tester un site avec une liste de chemins WordPress** :
   ```bash
   python aptdork.py -u http://example.com -wp /path/to/wordpress.txt -t 3 -n 10


   ADMINFile

   
   python APTDork.py -u https://www.example.com     -admin  ADMINFinder/AdminFinder.txt -t 5  -n  800
   
   API File 


   python APTDork.py -u  https://www.example.com      -api  APIJS/API.txt -t 5  -n  800


   ```

   Cette commande teste le site `http://example.com` avec les chemins spécifiés dans le fichier `wordpress.txt`, un délai de 3 secondes entre chaque requête, et un maximum de 10 pages.

3. **Tester un site pour des fichiers HTML** :
   ```bash
   python aptdork.py -u http://example.com -f html -t 1 -n 3
   ```

   Ce commande teste le site `http://example.com` pour des fichiers HTML, avec un délai de 1 seconde entre chaque requête et un maximum de 3 pages.

## Résultats

Le script affiche les résultats dans la console avec des messages colorés :

- **[Found]** : Fichier trouvé avec le code de statut 200.
- **[404 Not Found]** : Fichier non trouvé.
- **[403 Not Found]** : Accès interdit (erreur 403).
- **[405 Not Found]** : Méthode non autorisée (erreur 405).
- **[500 Internal Server Error]** : Erreur interne du serveur.
- **[504 Gateway Timeout]** : Délai d'attente de la passerelle dépassé.

Les résultats sont également consignés dans un fichier de log situé dans le répertoire `APTDorkLog` sous le nom `APTDorkLOG.txt`.

## License

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de l'adapter selon vos besoins.



---

