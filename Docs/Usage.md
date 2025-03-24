# Velvet - Fuzzer Tool

## Présentation

**Velvet** est un outil de **fuzzing** conçu pour effectuer des tests de présence de fichiers spécifiques ou de chemins sur des sites web. Il est particulièrement utile pour les tests de reconnaissance et l'identification de fichiers vulnérables dans le cadre d'audits de sécurité ou de reconnaissance. Ce script prend en charge la recherche de fichiers génériques (comme PHP, HTML, JS) ainsi que des chemins spécifiques pour des CMS populaires comme **WordPress** et **Joomla**.

Le script utilise la bibliothèque `requests` pour envoyer des requêtes HTTP et vérifier les réponses des fichiers cibles. Il prend en charge les erreurs HTTP courantes (404, 403, 500, etc.) et consigne les résultats dans un fichier de log pour une consultation ultérieure.

## Fonctionnalités

- Recherche de fichiers génériques (PHP, HTML, JS, XML, SQL) sur un site.
- Recherche de chemins spécifiques pour **WordPress** et **Joomla** via un fichier de chemins spécifique.
- Délai configurable entre chaque requête pour éviter de surcharger le serveur.
- Enregistrement des résultats dans un fichier de log détaillant les erreurs et succès.
- Affichage en couleur dans la console pour faciliter la lecture des résultats.

## Installation

1. Clonez le dépôt ou téléchargez les fichiers nécessaires.
2. Assurez-vous d'avoir Python installé (version 3.x recommandée).
3. Installez les dépendances avec la commande suivante :
   ```bash
   pip install requests

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
  Chemin vers un fichier texte contenant des chemins spécifiques à **WordPress** à tester. Chaque chemin doit être sur une ligne différente.  
  Exemple : `-wp /path/to/wordpress.txt`

- `-joomla`, `--joomla_file` : **Fichier de chemins Joomla** (Optionnel)  
  Chemin vers un fichier texte contenant des chemins spécifiques à **Joomla** à tester. Chaque chemin doit être sur une ligne différente.  
  Exemple : `-joomla /path/to/joomla.txt`

- `-t`, `--time` : **Temps entre les requêtes (en secondes)** (Obligatoire)  
  Le délai entre chaque requête HTTP envoyée au serveur. Cela permet de limiter la charge du serveur.  
  Exemple : `-t 2` (délai de 2 secondes)

- `-n`, `--number_of_pages` : **Nombre maximum de pages à tester** (Optionnel)  
  Le nombre maximum de pages à tester sur le site. Par défaut, le script teste jusqu'à 5 pages.  
  Exemple : `-n 10` (tester jusqu'à 10 pages)

### Exemple d'utilisation avec Python 3

**Tester un site pour des fichiers PHP** :
   ```bash
   python3 velvet.py -u http://example.com -f php -t <time> -n 5



**Tester un site avec une liste de chemins WordPress** :

```bash
python3 velvet.py -u http://example.com -wp /path/to/wordpress.txt -t <time> -n 1000



Tester un site avec une liste de chemins Joomla :

```bash 
python3 velvet.py -u http://example.com -joomla /path/to/joomla.txt -t <time> -n 1000



Tester un site pour des fichiers HTML :


```bash 
python3 velvet.py -u http://example.com -f html -t <time> -n 1000



Tester un site pour des fichiers JS :

```bash

python3 velvet.py -u http://example.com -f js -t <time> -n 1000




Tester un site pour des fichiers XML :
```bash
python3 velvet.py -u http://example.com -f xml -t <time> -n 1000




Tester un site pour des fichiers SQL :
```bash
python3 velvet.py -u http://example.com -f sql -t <time> -n 1000



