

import argparse
from tqdm import tqdm
import time
import requests
import os
import logging
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import sys





# Ajouter un décor ASCII avec couleurs
x = '\033[0m'
R = '\033[1;91m'  # Rouge pour les erreurs
g = '\033[0;92m'  # Vert pour [Found]
y = '\033[1;93m'  # Jaune pour l'erreur 405
M = '\033[1;35m'  # Violet pour erreur 500
O = '\033[1;33m'  # Orange pour erreur 504
B = '\033[1;34m'  # Bleu ciel pour l'URL cible
P = '\033[1;35m'  # Rose pour erreur 403 (Forbidden)
D = '\033[1;36m'  # Bleu foncé pour erreur 400 (Bad Request)
L = '\033[1;33m'  # Jaune pour l'erreur 405 (Method Not Allowed)





B_BLACK = '\033[48;5;16m'  # Fond noir
RED = '\033[97m'         # Texte blanc
RESET = '\033[0m'          # Réinitialisation des couleurs
G = '\033[92m' 









# Définir les codes de couleur ANSI pour fond noir et texte rouge
B_BLACK = '\033[48;5;16m'  # Fond noir
RED = '\033[31m'           # Texte rouge
GREEN = '\033[0m'          # Réinitialisation des couleurs

# Fonction pour afficher un texte avec fond noir et texte rouge
def print_footer():
    print(f"{B_BLACK}{GREEN} By @0x1Gp {RESET}")



# Exemple d'utilisation dans votre programme
def main():
    # Affichage de l'ASCII Art
    print(ascii_art)

TOOL_VERSION = "Velvet V.1.0.0"


def print_version():
 print(f"{B_BLACK}{GREEN}{TOOL_VERSION}{RESET}\n")







# Fonction pour afficher un texte avec bordure
def print_bordered_text(text, color):
    border = f'{color}+' + '-' * (len(text) + 2) + f'{color}+'  # Bordure
    content = f'{color}| {text} |'  # Contenu avec bordure
    
    print(border)
    print(content)
    print(border)

# Fonction pour afficher les détails de la commande sous forme de tableau
def print_command_details(args):
    print(f"{PINK}\n________________________________________________________________{RESET}")
    print(     f" {GREEN}        :: URL              : {args.url}              {RESET}")
    if args.file_type:         
        print(f" {GREEN}        :: Type de fichier  :  {args.file_type}        {RESET}") 
    if args.wordpress_file:         
        print(f" {GREEN}        :: Wordlist         :  {args.wordpress_file}        {RESET}")
    if args.api_file:         
        print(f" {GREEN}        :: Wordlist         :  {args.api_file}        {RESET}")
    if args.api_file:         
        print(f" {GREEN}        :: Wordlist         :  {args.joomla_file}        {RESET}")  
      
    if args.admin_file:         
        print(f" {GREEN}        :: Wordlist         :  {args.admin_file}        {RESET}")    
    if args.time:
        print(f" {GREEN}        :: Time             :  {args.time} s           {RESET}")
    if args.number_of_pages:
        print(f"{GREEN}         :: Page             :  {args.number_of_pages}  {RESET}")
    print(f"{PINK}________________________________________________________________{RESET}")











# Color settings
GREEN = '\033[92m'
PINK = '\033[95m'
RESET = '\033[0m'
CYRILLIC = '\033[96m'
RED = '\033[91m'






# ASCII Art coloré

ascii_art = PINK + r"""
 
╔────────────────────────╗
│.------..------..------.│
│|V.--. ||E.--. ||L.--. |│
│| :(): || (\/) || :/\: |│
│| ()() || :\/: || (__) |│
│| '--'V|| '--'E|| '--'L|│
│`------'`------'`------'│
╚────────────────────────╝
╔────────────────────────╗
│.------..------..------.│
│|V.--. ||E.--. ||T.--. |│
│| :(): || (\/) || :/\: |│
│| ()() || :\/: || (__) |│
│| '--'V|| '--'E|| '--'T|│
│`------'`------'`------'│
╚────────────────────────╝


"""


# Fonction pour afficher un texte avec bordure
def print_bordered_text(text, color):
    border = f'{color}+' + '-' * (len(text) + 2) + f'{color}+'  # Bordure
    content = f'{color}| {text} |'  # Contenu avec bordure
    
    print(border)
    print(content)
    print(border)

# Créer le dossier de logs s'il n'existe pas déjà
log_directory = "VelvetLog"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Définir le chemin du fichier de log
log_file_path = os.path.join(log_directory, "VelvetLog.txt")

# Configurer le logger pour les erreurs
logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,  # Enregistre toutes les informations (y compris les infos)
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'  # Ajout des logs au fichier
)

# Fonction pour tester les fichiers génériques (php, html, etc.)
def test_file_combinations(site, file_type, delay, num_pages, max_threads=10):
     
    file_combinations = {
        "php": [
            "index.php", "admin.php", "login.php", "config.php", "contact.php", "index.php?file=1", "index.php?search=test"
        ],
        "html": [
            "index.html", "about.html", "contact.html", "home.html", "index.html?file=1"
        ],
        "js": [
            "index.js", "main.js", "app.js", "scripts.js"
        ],
        "xml": [
            "index.xml", "sitemap.xml", "config.xml"
        ],
        "sql": [
            "index.sql", "backup.sql", "database.sql"
        ],
    }

    if file_type not in file_combinations:
        print(f"{R}File type '{file_type}' not supported!{x}")
        logging.error(f"File type '{file_type}' not supported!")
        return
    
    combinations = file_combinations[file_type]
    
    ### print(f"\nstart search: {RED}{site}{x}...\n")
    found_urls = []
    
    for i, file in enumerate(combinations):
        if i >= num_pages:  
            break
        url = f"{site}/{file}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{g}[Found]{x} {url}")
                logging.info(f"[Found] {url}")
                found_urls.append(url)
            elif response.status_code == 403:
                print(f"{P}[403 Forbidden]{x} {url}")
                logging.error(f"[403 Forbidden] {url}")
            elif response.status_code == 404:
                print(f"{R}[404 Not Found]{x} {url}")
                logging.warning(f"[404 Not Found] {url}")
            elif response.status_code == 400:
                print(f"{D}[400 Bad Request]{x} {url}")
                logging.error(f"[400 Bad Request] {url}")
            elif response.status_code == 405:
                print(f"{y}[Found 405 Method Not Allowed]{x} {url}")
                logging.error(f"[Found 405 Method Not Allowed] {url}")
            elif response.status_code == 500:
                print(f"{M}[500 Internal Server Error]{x} {url}")
                logging.error(f"[500 Internal Server Error] {url}")
            elif response.status_code == 504:
                print(f"{O}[504 Gateway Timeout]{x} {url}")
                logging.error(f"[504 Gateway Timeout] {url}")
            else:
                print(f"[{response.status_code}] {url}")
                logging.info(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            print(f"{R}[Error]{x} {url} - {e}")
            logging.error(f"[Error] {url} - {e}")
        
        time.sleep(delay)
    
    if found_urls:
        print(f"\n{g}[Found {len(found_urls)} files]{x}")
        logging.info(f"[Found {len(found_urls)} files]")
    else:
        print(f"\n{R}[No files found for type '{file_type}']{x}")
        logging.warning(f"[No files found for type '{file_type}']")


# Fonction pour tester les fichiers WordPress
def test_wordpress_files(site, wp_file, delay, num_pages, max_threads=10):
    if not os.path.isfile(wp_file):
        print(f"{R}Le fichier WordPress {wp_file} n'existe pas!{x}")
        logging.error(f"Le fichier WordPress {wp_file} n'existe pas!")
        return

    with open(wp_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = file.readlines()

    paths = [path.strip() for path in paths]

    found_urls = []
    errors = 0  # Compteur d'erreurs

    # Créer la barre de progression au début, une seule fois
    progress_bar = tqdm(total=min(len(paths), num_pages), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)

    # Initialiser la barre avec un postfix pour afficher les statistiques
    progress_bar.set_postfix(found=0, errors=0)

    # Boucle de traitement des URLs
    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                found_urls.append(url)
                # Mise à jour du nombre de found et errors dans le postfix
                progress_bar.set_postfix(found=len(found_urls), errors=errors)
                print(f"{g}[Found]{x} {url}")  # Affiche les URL trouvées
            elif response.status_code == 403:
                errors += 1
                progress_bar.set_postfix(found=len(found_urls), errors=errors)
                print(f"{P}[403 Forbidden]{x} {url}")  # Affiche les 403
            elif response.status_code == 404:
                errors += 1
                progress_bar.set_postfix(found=len(found_urls), errors=errors)
                print(f"{R}[404 Not Found]{x} {url}")  # Affiche les 404
            elif response.status_code == 400:
                errors += 1
                progress_bar.set_postfix(found=len(found_urls), errors=errors)
                print(f"{D}[400 Bad Request]{x} {url}")
            elif response.status_code == 500:
                errors += 1
                progress_bar.set_postfix(found=len(found_urls), errors=errors)
                print(f"{M}[500 Internal Server Error]{x} {url}")
            else:
                errors += 1
                progress_bar.set_postfix(found=len(found_urls), errors=errors)
                print(f"[{response.status_code}] {url}")  # Affiche les autres statuts
        except requests.exceptions.RequestException as e:
            errors += 1
            progress_bar.set_postfix(found=len(found_urls), errors=errors)
            print(f"{R}[Error]{x} {url} - {e}")  # Affiche l'erreur
            logging.error(f"[Error] {url} - {e}")

        # Mise à jour de la barre après chaque requête (sans la recréer)
        progress_bar.update(1)  # Mise à jour après chaque requête
        sys.stdout.flush()  # Forcer l'affichage immédiat

        time.sleep(delay)

    # Fermer proprement la barre de progression après la boucle
    progress_bar.close()

    # Résultats finaux
    if found_urls:
        print(f"\n{g}[Found {len(found_urls)} WordPress paths]{x}")
        logging.info(f"[Found {len(found_urls)} WordPress paths]")
    else:
        print(f"\n{R}[No WordPress paths found]{x}")
        logging.warning(f"[No WordPress paths found]")










# Fonction pour tester les fichiers Joomla
def test_joomla_files(site, joomla_file, delay,number_of_pages ):
    if not os.path.exists(joomla_file):
        print(f"{RED}[Error] Le fichier Joomla spécifié n'existe pas !{RESET}")
        return
    
    with open(joomla_file, 'r') as file:
        paths = file.readlines()

    paths = [path.strip() for path in paths]
    
    ### print(f"\n\n") mettre le lien facultative 
    found_urls = []
    # Créer la barre de progression au début, une seule fois
    
    
    # Créer la barre de progression au début, une seule fois
    progress_bar = tqdm(total=min(len(paths),number_of_pages ), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)

    # Initialiser la barre avec un postfix pour afficher les statistiques
    progress_bar.set_postfix(found=0, errors=0)
   

    for i, path in enumerate(paths):
        if i >= number_of_pages:  
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            # Vérification du code de statut et affichage avec les couleurs appropriées
            if response.status_code == 200:
                print(f"{GREEN}[Found]{RESET} {url}")
                found_urls.append(url)
            elif response.status_code == 403:
                print(f"{P}[403 Forbidden]{RESET} {url}")
                
            elif response.status_code == 404:
                print(f"{R}[404 Not Found]{RESET} {url}")
            elif response.status_code == 400:
                print(f"{B}[400 Bad Request]{RESET} {url}")
            elif response.status_code == 405:
                print(f"{y}[405 Method Not Allowed]{RESET} {url}")
            elif response.status_code == 500:
                print(f"{M}[500 Internal Server Error]{RESET} {url}")
            elif response.status_code == 504:
                print(f"{M}[504 Gateway Timeout]{RESET} {url}")
            else:
                print(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            print(f"{RED}[Error]{RESET} {url} - {e}")
        

        # Mise à jour de la barre après chaque requête (sans la recréer)
        progress_bar.update(1)  # Mise à jour après chaque requête
        sys.stdout.flush()  # Forcer l'affichage immédiat

        time.sleep(delay)
    

 
        # Fermer proprement la barre de progression après la boucle
    progress_bar.close()
    
    
    
    if found_urls:
        print(f"{GREEN}[Found {len(found_urls)} Joomla paths]{RESET}")
    else:
        print(f"{RED}[No Joomla paths found]{RESET}")










# Fonction pour tester les fichiers .htaccess ####traveaux   
def test_htaccess_files(site, htaccess_file, delay, number_of_pages):
    if not os.path.exists(htaccess_file):

        return
    
    with open(htaccess_file, 'r') as file:
        paths = file.readlines()

    paths = [path.strip() for path in paths]
    
    print(f"\nDébut de la recherche des fichiers .htaccess sur {site}...\n")
    found_urls = []
    
    for i, path in enumerate(paths):
        if i >= number_of_pages:  # Limite le nombre de pages à tester
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            # Vérification du code de statut et affichage avec les couleurs appropriées
            if response.status_code == 200:
                print(f"{GREEN}[Found] {url}{RESET}")
                found_urls.append(url)
            elif response.status_code == 403:
                print(f"{RED}[403 Forbidden]{RESET} {url}")
            elif response.status_code == 404:
                print(f"{RED}[404 Not Found]{RESET} {url}")
            elif response.status_code == 400:
                print(f"{RED}[400 Bad Request]{RESET} {url}")
            elif response.status_code == 405:
                print(f"{RED}[405 Method Not Allowed]{RESET} {url}")
            elif response.status_code == 500:
                print(f"{RED}[500 Internal Server Error]{RESET} {url}")
            elif response.status_code == 504:
                print(f"{RED}[504 Gateway Timeout]{RESET} {url}")
            else:
                print(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            print(f"{RED}[Error]{RESET} {url} - {e}")
        
        time.sleep(delay)
    
    if found_urls:
        print(f"{GREEN}[Found {len(found_urls)} htaccess paths]{RESET}")
    else:
        print(f"{RED}[No htaccess paths found]{RESET}")












# Fonction pour tester les chemins d'administration
def test_admin_combinations(site, admin_file, delay, num_pages):
    if not os.path.isfile(admin_file):
        print(f"{R}Le fichier d'administration {admin_file} n'existe pas!{x}")
        logging.error(f"Le fichier d'administration {admin_file} n'existe pas!")
        return

    with open(admin_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = file.readlines()

    paths = [path.strip() for path in paths]

   
       # Créer la barre de progression au début, une seule fois
    progress_bar = tqdm(total=min(len(paths),num_pages), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)

    # Initialiser la barre avec un postfix pour afficher les statistiques
    progress_bar.set_postfix(found=0, errors=0)
   
   
   
   
    # Fonction pour tester les chemins d'administration
## print(f"\n start search: {RED}{site}{x}...\n")
    
    
    
    
    
    
    
    
    
    found_urls = []

   
   
   
    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{g}[Found]{x} {url}")
                logging.info(f"[Found] {url}")
                found_urls.append(url)
            elif response.status_code == 403:
                print(f"{P}[403 Forbidden]{x} {url}")
                logging.error(f"[403 Forbidden] {url}")
            elif response.status_code == 404:
                print(f"{R}[404 Not Found]{x} {url}")
                logging.warning(f"[404 Not Found] {url}")
            elif response.status_code == 400:
                print(f"{D}[400 Bad Request]{x} {url}")
                logging.error(f"[400 Bad Request] {url}")
            elif response.status_code == 405:
                print(f"{y}[405 Method Not Allowed]{x} {url}")
                logging.error(f"[405 Method Not Allowed] {url}")
            elif response.status_code == 500:
                print(f"{M}[500 Internal Server Error]{x} {url}")
                logging.error(f"[500 Internal Server Error] {url}")
            elif response.status_code == 504:
                print(f"{O}[504 Gateway Timeout]{x} {url}")
                logging.error(f"[504 Gateway Timeout] {url}")
            else:
                print(f"[{response.status_code}] {url}")
                logging.info(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            print(f"{R}[Error]{x} {url} - {e}")
            logging.error(f"[Error] {url} - {e}")
        # Mise à jour de la barre après chaque requête (sans la recréer)
        progress_bar.update(1)  # Mise à jour après chaque requête
        sys.stdout.flush()  # Forcer l'affichage immédiat
        time.sleep(delay)
    progress_bar.close()
    if found_urls:
        print(f"\n{g}[Found {len(found_urls)} admin paths]{x}")
        logging.info(f"[Found {len(found_urls)} admin paths]")
    else:
        print(f"\n{R}[No admin paths found]{x}")
        logging.warning(f"[No admin paths found]")







# Fonction pour tester les chemins d'API
def test_api_combinations(site, api_file, delay, num_pages):
    if not os.path.isfile(api_file):
        print(f"{R}Le fichier d'API {api_file} n'existe pas!{x}")
        logging.error(f"Le fichier d'API {api_file} n'existe pas!")
        return

    with open(api_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = file.readlines()

    paths = [path.strip() for path in paths]

   
    ### print(f"\n start search : {B}{site}{x}...\n")
    found_urls = []

   
   
    # Créer la barre de progression au début, une seule fois
    progress_bar = tqdm(total=min(len(paths), num_pages), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)

    # Initialiser la barre avec un postfix pour afficher les statistiques
    progress_bar.set_postfix(found=0, errors=0)
   
   
   
   
   
   
   
   
    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{g}[Found]{x} {url}")
                logging.info(f"[Found] {url}")
                found_urls.append(url)
            elif response.status_code == 403:
                print(f"{P}[403 Forbidden]{x} {url}")
                logging.error(f"[403 Forbidden] {url}")
            elif response.status_code == 404:
                print(f"{R}[404 Not Found]{x} {url}")
                logging.warning(f"[404 Not Found] {url}")
            elif response.status_code == 400:
                print(f"{D}[400 Bad Request]{x} {url}")
                logging.error(f"[400 Bad Request] {url}")
            elif response.status_code == 405:
                print(f"{y}[405 Method Not Allowed]{x} {url}")
                logging.error(f"[405 Method Not Allowed] {url}")
            elif response.status_code == 500:
                print(f"{M}[500 Internal Server Error]{x} {url}")
                logging.error(f"[500 Internal Server Error] {url}")
            elif response.status_code == 504:
                print(f"{O}[504 Gateway Timeout]{x} {url}")
                logging.error(f"[504 Gateway Timeout] {url}")
            else:
                print(f"[{response.status_code}] {url}")
                logging.info(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            print(f"{R}[Error]{x} {url} - {e}")
            logging.error(f"[Error] {url} - {e}")
        
        time.sleep(delay)
        # Mise à jour de la barre après chaque requête (sans la recréer)
        progress_bar.update(1)  # Mise à jour après chaque requête
        sys.stdout.flush()  # Forcer l'affichage immédiat

        time.sleep(delay)

    # Fermer proprement la barre de progression après la boucle
    progress_bar.close()
    if found_urls:
        print(f"\n{g}[Found {len(found_urls)} API paths]{x}")
        logging.info(f"[Found {len(found_urls)} API paths]")
    else:
        print(f"\n{R}[No API paths found]{x}")
        logging.warning(f"[No API paths found]")

# Fonction principale pour gérer les arguments
def main():
    parser = argparse.ArgumentParser(description="Exécuter des recherches pour des fichiers WordPress, API ou autres fichiers sur un site")
    parser.add_argument("-u", "--url", required=True, help="URL du site cible")
    parser.add_argument("-f", "--file_type", required=False, help="Type de fichier (php, html, js, etc.)")
    parser.add_argument("-ht", "--htaccess_file", required=False, default="HTaccess/htaccess.txt", help="Chemin vers le fichier de chemins .htaccess (par défaut: HTaccess/htaccess.txt)")
    parser.add_argument("-wp", "--wordpress_file", required=False, help="Chemin vers le fichier de chemins WordPress") 
    parser.add_argument("-api", "--api_file", required=False, help="Chemin vers le fichier de chemins API")
    parser.add_argument("-admin", "--admin_file", required=False, help="Chemin vers le fichier de chemins d'administration")
    parser.add_argument("-joomla", "--joomla_file", required=False, help="Chemin vers le fichier de chemins Joomla")
   
    parser.add_argument("-t", "--time", type=int, required=True, help="Temps entre les requêtes")
    parser.add_argument("-n", "--number_of_pages", type=int, default=5, help="Nombre maximum de pages à tester (par défaut: 5)") 
    parser.add_argument("-thread", "--threads", type=int, default=10, help="Nombre de threads pour l'exécution en multithreading (par défaut: 10)")
    
    
    # Vérifier si l'argument Joomla est présent
   
    
    args = parser.parse_args()

    site = args.url
    delay = args.time
    num_pages = args.number_of_pages
   
    
    
    
    
    
    
    
    
    
    
    # Afficher l'ASCII Art au démarrage du script
    print(ascii_art)
 



    # Affichage avec bordure pour "By GupS3c"   
    print_footer() 
    # Affichage de la version de l'outil
    print_version()
     
    
    print_command_details(args)
    
   


    
       
####traveaux 
    htaccess_folder = args.htaccess_file

     # Vérification si l'argument htaccess est spécifié
    if htaccess_folder:
        test_htaccess_files(site, htaccess_folder, delay, num_pages)
    else:
        print(f"{RED}[Error] Vous devez spécifier un dossier contenant le fichier htacces.txt.{RESET}")





    if args.api_file:
        api_file = args.api_file
        test_api_combinations(site, api_file, delay, num_pages)
    elif args.wordpress_file:
        wp_file = args.wordpress_file
        test_wordpress_files(site, wp_file, delay, num_pages)
     
    ##Vérification de l'option -joomla et des autres paramètres
    if args.joomla_file:
        if not args.joomla_file:
            print(f"{RED}[Error] Vous devez spécifier un fichier Joomla pour tester.{RESET}")
            return
        test_joomla_files(site, args.joomla_file, delay, num_pages)
     


     # Vérification si le fichier .htaccess existe
      
   # Vérification si le fichier .htaccess existe


    elif args.admin_file:
        admin_file = args.admin_file
        test_admin_combinations(site, admin_file, delay, num_pages)
    elif args.file_type:
        file_type = args.file_type
        test_file_combinations(site, file_type, delay, num_pages)
    else:
        print(f"{R}[Error]{x} - Vous devez spécifier soit un fichier WordPress (-wp), un fichier API (-api), un fichier admin (-admin), ou un type de fichier (-f) pour effectuer un scan.")
        logging.error(f"[Error] Vous devez spécifier soit un fichier WordPress (-wp), un fichier API (-api), un fichier admin (-admin), ou un type de fichier (-f) pour effectuer un scan.")










if __name__ == "__main__":
    main()
