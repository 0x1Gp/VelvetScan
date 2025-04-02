import socket
import argparse
from tqdm import tqdm
import time
import requests
import os
import logging
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import psutil
from colorama import Fore, Style
from fake_useragent import UserAgent
import random
from ftplib import FTP
import html
import re 
ua = UserAgent()


#Pour obtenir les informations sur la mémoire
import datetime  # Pour afficher l'heure à la fin du scan
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
    print(f"{B_BLACK}{GREEN} By @0x1Gp 🍉{RESET}")



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
        print(f" {GREEN}        :: Type de fichier   :  {args.file_type}        {RESET}") 
    if args.wordpress_file:         
        print(f" {GREEN}        :: Wordlist          :  {args.wordpress_file}        {RESET}")
    if args.api_file:         
        print(f" {GREEN}        :: Wordlist          :  {args.api_file}        {RESET}")
    if args.joomla_file:         
        print(f" {GREEN}        :: Wordlist          :  {args.joomla_file}        {RESET}")
    
      
    if args.admin_file:         
        print(f" {GREEN}        :: Wordlist          :  {args.admin_file}        {RESET}")  
    if args.panel:
        print(f" {GREEN}        :: Wordlist          : {args.panel}        {RESET}")
    

    if args.javascript:  
        print(f" {GREEN}        :: JS Wordlist       : {args.javascript}        {RESET}")

    if args.ht_file:
        print(f" {GREEN}        :: Wordlist          : {args.ht_file}        {RESET}")



    if args.time:
        print(f" {GREEN}        :: Time             :  {args.time} s           {RESET}")
    if args.number_of_pages:
        print(f"{GREEN}         :: Page              :  {args.number_of_pages}  {RESET}")
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





#################################################################
# Liste des fichiers à vérifier pour la version de WordPress
"""
files_to_check = [
    "wp-includes/js/jquery/jquery.js",
    "wp-includes/js/jquery/jquery.min.js",
    "wp-includes/js/wp-emoji-release.min.js",
    "wp-includes/js/wp-emoji-release.js",
    "wp-includes/js/wp-pointer.js",
    "wp-includes/js/wp-pointer.min.js",
    "wp-includes/js/mediaelement/mediaelement-and-player.js",
    "wp-includes/js/mediaelement/mediaelement-and-player.min.js",
    "wp-includes/js/mediaelement/wp-mediaelement.js",
    "wp-includes/js/mediaelement/wp-mediaelement.min.js",
    "wp-includes/js/wp-util.js",
    "wp-includes/js/wp-util.min.js",
    "wp-includes/js/twemoji.js",
    "wp-includes/js/twemoji.min.js",
    "wp-includes/js/admin-bar.js",
    "wp-includes/js/admin-bar.min.js",
    "wp-includes/js/core.min.js",
    "wp-includes/js/core.js",
    "wp-includes/js/plupload/plupload.js",
    "wp-includes/js/plupload/plupload.min.js",
    "wp-includes/js/customize-preview.js",
    "wp-includes/js/customize-preview.min.js",
    "wp-includes/js/jquery-ui/jquery-ui.js",
    "wp-includes/js/jquery-ui/jquery-ui.min.js",
    "wp-includes/js/underscore.js",
    "wp-includes/js/underscore.min.js",
    "wp-includes/js/backbone.js",
    "wp-includes/js/backbone.min.js",
    "wp-includes/js/push.js",
    "wp-includes/js/push.min.js",
    "wp-includes/js/wp-embed.js",
    "wp-includes/js/wp-embed.min.js"
]################################"""
#################################################################





#######################################################################################################☑️Wordpress Scan Tool ☑️
# Constantes pour la mise en forme des couleurs
R, G, P, B, M, Y, X, C = '\033[31m', '\033[32m', '\033[35m', '\033[34m', '\033[33m', '\033[33m', '\033[0m', '\033[36;1m'
#######recherche dans la liste d'user agent pour en pioché un aléatoirement
# Fonction pour tester les ports critiques FTP, SSH, Telnet, RDP, VNC
def check_critical_ports(target_host):
    ports = {21: "FTP", 22: "SSH", 23: "Telnet", 3389: "RDP", 5900: "VNC"}
    port_status = {}

    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout de 2 secondes
        result = sock.connect_ex((target_host, port))

        if result == 0:
            # Le port est ouvert
            port_status[port] = {"name": service, "status": f"{G}🟢 Open{X}", "info": ""}
            try:
                if port == 21:
                    ftp = FTP(target_host, timeout=2)
                    ftp.login()  # Test de connexion anonyme
                    port_status[port]["info"] = "Anonymous Login Allowed"
                    ftp.quit()
                else:
                    sock.send(b'\n')
                    banner = sock.recv(1024).decode().strip()
                    if banner:
                        port_status[port]["info"] = f"{G}Banner: {banner}{X}"
            except Exception as e:
                port_status[port]["info"] = f"Error: {str(e)}"
        sock.close()

    return port_status

def is_port_open(host, port=80, timeout=2):
    """Vérifie si un port est ouvert sur une cible."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def check_ports(target_host):
    """ Vérifie l'état des ports 80 et 443 """
    port_80_status = f"{G}[+]🟢 Open🟢[+] {X}" if is_port_open(target_host, 80) else f"{R}[+]🔴 Closed🔴[+]{X}"
    port_443_status = f"{G}[+]🟢 Open🟢[+] {X}" if is_port_open(target_host, 443) else f"{R}[+]🔴 Closed🔴 [+]{X}"
    return port_80_status, port_443_status



#####Func de l'user agent lists 
def load_user_agents(file_path="Agent/user_agents.txt"):
    """Charge les User-Agents depuis un fichier et les retourne sous forme de liste."""
    if not os.path.isfile(file_path):
        print(f"[ERROR] Le fichier '{file_path}' n'existe pas!")
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        user_agents = [line.strip() for line in f if line.strip()]  # Enlever les lignes vides et espaces
    return user_agents

def get_headers(use_random_ua, browser_type=None, ua_file="Agent/user_agents.txt"):
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    user_agents = load_user_agents(ua_file)  # Charger les UA depuis le fichier
    
    if use_random_ua and user_agents:  # Vérifie si la liste d'UA n'est pas vide
        headers["User-Agent"] = random.choice(user_agents)  # Prend un UA au hasard
    else:
        headers["User-Agent"] = "Mozilla/5.0 (compatible; VelvetScanner/1.0; +https://example.com/bot)"

    return headers
# Fonction pour tester les fichiers WordPress
def test_wordpress_files(site, wp_file, delay, num_pages, max_threads=10):
    wp_version = check_wordpress_version(site)  # Récupérer la version de WP mais ne pas l'afficher ici
    
    # Récupérer l'IP du site cible
    try:
        site_ip = socket.gethostbyname(site.replace("http://", "").replace("https://", "").split('/')[0])
    except socket.gaierror:
        site_ip = "Unknown"
    
    #Extraction du domaine cible
    target_host = site.replace("http://", "").replace("https://", "").split('/')[0]
    
     # Vérifier les ports au début et les garder en mémoire
    port_80_status, port_443_status = check_ports(target_host)
    
    if not os.path.isfile(wp_file):
        print(f"{R}Le fichier WordPress {wp_file} n'existe pas!{X}")
        return

    with open(wp_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = file.readlines()

    paths = [path.strip() for path in paths]

    found_urls = []
    errors = 0  # Compteur d'erreurs
    requests_done = 0  # Compteur de requêtes
    data_sent = 0  # Taille des données envoyées (en octets)
    data_received = 0  # Taille des données reçues (en octets)

    # Créer la barre de progression au début, une seule fois
    progress_bar = tqdm(total=min(len(paths), num_pages), desc="Loading", unit="req", ncols=80, dynamic_ncols=True, leave=True)

    # Initialiser la barre avec un postfix pour afficher les statistiques
    #Mise à jour initiale avec les ports (ils resteront affichés)
    progress_bar.set_postfix(found=0, errors=0, version="N/A")
    

    
    

    start_time = time.time()  # Pour mesurer le temps écoulé
    


    




    # Boucle de traitement des URLs #####Couleur porgress barre
    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            requests_done += 1
            data_sent += len(response.request.body or b'')  # Calcul des données envoyées
            data_received += len(response.content)  # Calcul des données reçues
            if response.status_code == 200:
                found_urls.append(url)
                progress_bar.bar_format = f"{G}{{l_bar}}{{bar}}{{r_bar}}{X}"  # Barre verte
                progress_bar.set_postfix(found=len(found_urls), errors=errors, version=wp_version if wp_version else "N/A")
                print(f"{G}[+]✅ [Found] ✅ [+]{X} {url}")  # Affiche les URL trouvées
            elif response.status_code == 403:
                errors += 1
                progress_bar.bar_format = f"{P}{{l_bar}}{{bar}}{{r_bar}}{X}"  # Barre pourpre pour 403
                progress_bar.set_postfix(found=len(found_urls), errors=errors, version=wp_version if wp_version else "N/A")
                print(f"{P}[+][403 Forbidden][+]{X} {url}")  # Affiche 403 Forbidden
            elif response.status_code == 404:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"  # Barre rouge pour 404
                progress_bar.set_postfix(found=len(found_urls), errors=errors, version=wp_version if wp_version else "N/A")
                print(f"{R}[+] ❌ [404 Not Found] ❌ [+]{X} {url}")  # Affiche 404 Not Found
            elif response.status_code == 400:
                errors += 1
                progress_bar.bar_format = f"{B}{{l_bar}}{{bar}}{{r_bar}}{X}"  # Barre bleue pour 400
                progress_bar.set_postfix(found=len(found_urls), errors=errors, version=wp_version if wp_version else "N/A")
                print(f"{B}[+][400 Bad Request][+]{X} {url}")  # Affiche 400 Bad Request
            elif response.status_code == 405:
                errors += 1
                progress_bar.bar_format = f"{Y}{{l_bar}}{{bar}}{{r_bar}}{X}"  # Barre jaune pour 405
                progress_bar.set_postfix(found=len(found_urls), errors=errors, version=wp_version if wp_version else "N/A")
                print(f"{Y}[+][405 Method Not Allowed][+]{X} {url}")  # Affiche 405 Method Not Allowed
            elif response.status_code == 500:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"  # Barre marron pour 500
                progress_bar.set_postfix(found=len(found_urls), errors=errors, version=wp_version if wp_version else "N/A")
                print(f"{M}[+][500 Internal Server Error][+]{X} {url}")  # Affiche 500 Internal Server Error
            elif response.status_code == 504:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"  # Barre marron pour 504
                progress_bar.set_postfix(found=len(found_urls), errors=errors, version=wp_version if wp_version else "N/A")
                print(f"{M}[+][504 Gateway Timeout][+]{X} {url}")  # Affiche 504 Gateway Timeout
            ######
            else:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"  # Barre rouge pour autres erreurs
                progress_bar.set_postfix(found=len(found_urls), errors=errors, version=wp_version if wp_version else "N/A")
                print(f"[{response.status_code}] {url}")  # Affiche les autres erreurs

        except requests.exceptions.RequestException as e:
            errors += 1
            progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"  # Barre rouge pour erreurs
            progress_bar.set_postfix(found=len(found_urls), errors=errors, version=wp_version if wp_version else "N/A")
            print(f"{R}[Error]{X} {url} - {e}")  # Affiche l'erreur

        # Mise à jour de la barre après chaque requête
        progress_bar.set_postfix(found=len(found_urls), errors=errors, version="N/A", p80=port_80_status, p443=port_443_status)
        progress_bar.update(1)
        
        sys.stdout.flush()  # Forcer l'affichage immédiat
        time.sleep(delay)

    # Fermer proprement la barre de progression après la boucle
    progress_bar.close()
    
    

    use_random_ua = True  # Définir la valeur en fonction de votre logique
    headers = get_headers(use_random_ua=use_random_ua, browser_type="chrome")
    
    
    # Temps écoulé
    elapsed_time = time.time() - start_time
    

    
    ##date Finish
    print("\n"f"{C}[+] Finished:", datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"))
    # Résultats finaux
    if found_urls:
        print(f"\n{G}[+] Found {len(found_urls)} WordPress paths{X}")
        logging.info(f"{G}[+] Found {len(found_urls)} WordPress paths")
    else:
        print(f"\n{R}[+] No WordPress paths found{X}")
        logging.warning(f"[+] No WordPress paths found[+]")
    
    
     
    # Afficher la version à la fin du scan
    if wp_version != "N/A":
        print(f"\n{G}[+] WordPress Version Found [+]{X} {wp_version}")
    else:
        print(f"\n{R}[+]WordPress Version Not Found at the End[+]{X}")
    
   

    headers = get_headers(use_random_ua=True)  # Assurez-vous que 'True' ou 'False' est passé en fonction de la commande
    server_type = response.headers.get("Server", "Unknown")  # Récupérer l'info du serveur
    
    
    # Ajouter l'affichage pour FTP, SSH, Telnet, RDP, VNC
    port_status = {
    21: {"name": "FTP", "status": "", "info": ""},
    22: {"name": "SSH", "status": "", "info": ""},
    23: {"name": "Telnet", "status": "", "info": ""},
    3389: {"name": "RDP", "status": "", "info": ""},
    5900: {"name": "VNC", "status": "", "info": ""}
    }
       
    
    
    # Après avoir exécuté la fonction check_critical_ports
    port_status = check_critical_ports(target_host)


    # Afficher les statistiques finales
    print(f"{C}[+] User-Agent Used: {X}{G}{headers['User-Agent']}{X}")#user agent 
    print(f"{C}[+] Server: {server_type} | target :{X} {G}{url} {X}")
    print(f"{C}[+] Target IP:{X} {G}{site_ip}{X}")
    print(f"{C}[+] Ports Scannés: 80 -> {port_80_status} | 443 -> {port_443_status}{X}")
    # Affichage de l'état de chaque port
    
    ####Port status RDP/ssh/ftp etc...
    print(f"{C}[+] Port 80 Status: {port_80_status}{X}")
    if port_status:  # Si le dictionnaire n'est pas vide
       for port, status_info in port_status.items():
        print(f"{C}[+] Port {port} ({status_info['name']}): {status_info['status']} - {status_info['info']}{X}")
    else:
       print(f"{R}[+] Aucun port critique ouvert sur ce site.{X}")
    

    



    print(f"{C}[+] Requests Done: {G}{requests_done}{X}")
    print(f"{C}[+] Cached Requests:{G} {requests_done - len(found_urls)}{X}")  # Estimation des requêtes mises en cache
    ###print(f"{G}[+] Data Sent: {data_sent / 1024:.3f} KB")
    print(f"{C}[+] Data Received: {G}{data_received / (1024 * 1024):.3f} MB{X}")
    print(f"{C}[+] Memory used: {G}{psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024):.2f} MB{X}")
    print(f"{C}[+] Elapsed time: {G}{str(datetime.timedelta(seconds=elapsed_time))}{X}")
    # Afficher seulement les ports ouverts
    
    
    ###for port, status_info in port_status.items():
    #### print(f"{C}[+] Port {port} ({status_info['name']}): {status_info['status']} - {status_info['info']}{X}")
    
    
# Fonction pour vérifier la version de WordPress
# Safe Detections Headers
def check_wordpress_version(site):
    try:
        response = requests.get(site)
        if response.status_code == 200:
            # Recherche dans le meta tag "generator"
            if 'generator' in response.text.lower():
                start_index = response.text.lower().find('generator')
                end_index = response.text.find('"', start_index)
                version_tag = response.text[start_index:end_index]
                if 'content="' in version_tag:
                    version = version_tag.split('content="')[1]
                    version = html.unescape(version)  # Convertir les entités HTML
                    return version

            # Recherche dans les headers HTTP
            if 'X-Powered-By' in response.headers:
                header = response.headers['X-Powered-By']
                if 'WordPress' in header:
                    version = header.split('WordPress/')[1]
                    version = html.unescape(version)  # Convertir les entités HTML
                    return version

            # Recherche de la version dans les commentaires HTML
            if '<!-- WordPress version' in response.text:
                version_tag = response.text.split('<!-- WordPress version')[1].split('-->')[0]
                version = version_tag.split()[1]
                version = html.unescape(version)  # Convertir les entités HTML
                return version

            # Vérification dans le fichier /license.txt
            license_url = f"{site}/license.txt"
            license_response = requests.get(license_url)
            if license_response.status_code == 200:
                # Recherche de la version dans le fichier license.txt
                if "WordPress" in license_response.text:
                    version_tag = license_response.text.split("WordPress")[1].split()[0]
                    version = html.unescape(version_tag)  # Convertir les entités HTML
                    return version

            # Vérification dans le fichier /readme.html
            readme_url = f"{site}/readme.html"
            readme_response = requests.get(readme_url)
            if readme_response.status_code == 200:
                # Recherche de la version dans le fichier readme.html
                if "WordPress" in readme_response.text:
                    # Extraire la version après la mention "WordPress"
                    start_index = readme_response.text.find("WordPress")
                    version_tag = readme_response.text[start_index:]
                    version = version_tag.split()[1]  # Prendre la version juste après "WordPress"
                    version = html.unescape(version)  # Convertir les entités HTML
                    return version

            #####aggressive detections .js Wp versions
            # (la partie agressive peut aussi être modifiée si nécessaire)

            # Si aucune version n'est trouvée, renvoyer "N/A"
            return "N/A"
        return "N/A"
    except requests.exceptions.RequestException:
        return "N/A"

############################################################################################☑️ 🔝Wordpress🔝 ☑️









#######################################☑️ detections Joomla ☑️ 
# Constantes pour la mise en forme des couleurs

R, G, P, B, M, Y, X, C = '\033[31m', '\033[32m', '\033[35m', '\033[34m', '\033[33m', '\033[33m', '\033[0m', '\033[36;1m'

def check_critical_ports(target_host):
    ports = {21: "FTP", 22: "SSH", 23: "Telnet", 3389: "RDP", 5900: "VNC"}
    port_status = {}

    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout de 2 secondes
        result = sock.connect_ex((target_host, port))

        if result == 0:
            # Le port est ouvert
            port_status[port] = {"name": service, "status": f"{G}🟢 Open{X}", "info": ""}
            try:
                if port == 21:
                    ftp = FTP(target_host, timeout=2)
                    ftp.login()  # Test de connexion anonyme
                    port_status[port]["info"] = "Anonymous Login Allowed"
                    ftp.quit()
                else:
                    sock.send(b'\n')
                    banner = sock.recv(1024).decode().strip()
                    if banner:
                        port_status[port]["info"] = f"{G}Banner: {banner}{X}"
            except Exception as e:
                port_status[port]["info"] = f"Error: {str(e)}"
        sock.close()

    return port_status

def is_port_open(host, port=80, timeout=2):
    """Vérifie si un port est ouvert sur une cible."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False



#######recherche dans la liste d'user agent pour en pioché un aléatoirement
def load_user_agents(file_path="Agent/user_agents.txt"):
    """Charge les User-Agents depuis un fichier et les retourne sous forme de liste."""
    if not os.path.isfile(file_path):
        print(f"[ERROR] Le fichier '{file_path}' n'existe pas!")
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        user_agents = [line.strip() for line in f if line.strip()]  # Enlever les lignes vides et espaces
    return user_agents

def get_headers(use_random_ua, browser_type=None, ua_file="Agent/user_agents.txt"):
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    user_agents = load_user_agents(ua_file)  # Charger les UA depuis le fichier
    
    if use_random_ua and user_agents:  # Vérifie si la liste d'UA n'est pas vide
        headers["User-Agent"] = random.choice(user_agents)  # Prend un UA au hasard
    else:
        headers["User-Agent"] = "Mozilla/5.0 (compatible; VelvetScanner/1.0; +https://example.com/bot)"

    return headers
# Fonction pour tester les fichiers Joomla
def test_joomla_files(site, joomla_file, delay, num_pages):
    target_host = site.replace("http://", "").replace("https://", "").split('/')[0]

    # Récupérer l'IP du site cible
    try:
        site_ip = socket.gethostbyname(site.replace("http://", "").replace("https://", "").split('/')[0])
    except socket.gaierror:
        site_ip = "Unknown"
    
    
    
    
    if not os.path.exists(joomla_file):
        print(f"{R}[Error] Le fichier Joomla spécifié n'existe pas !{X}")
        return
    
    with open(joomla_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = [path.strip() for path in file.readlines()]
    
    found_urls = []
    errors = 0  # Compteur d'erreurs
    requests_done = 0  # Compteur de requêtes
    data_sent = 0  # Taille des données envoyées (en octets)
    data_received = 0  # Taille des données reçues (en octets)

    progress_bar = tqdm(total=min(len(paths), num_pages), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)
    progress_bar.set_postfix(found=0, errors=0)
    start_time = time.time()
    use_random_ua = True  # Définir la valeur en fonction de votre logique
    headers = get_headers(use_random_ua=use_random_ua, browser_type="chrome")
    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            requests_done += 1
            data_sent += len(response.request.body or b'')
            data_received += len(response.content)
            
            if response.status_code == 200:
                found_urls.append(url)
                progress_bar.bar_format = f"{G}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{G}[+]✅ [Found] ✅ [+]{X} {url}")
            elif response.status_code == 403:
                errors += 1
                progress_bar.bar_format = f"{P}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{P}[+][403 Forbidden][+]{X} {url}")
            elif response.status_code == 404:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{R}[+] ❌ [404 Not Found] ❌ [+]{X} {url}")
            elif response.status_code == 400:
                errors += 1
                progress_bar.bar_format = f"{B}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{B}[+][400 Bad Request][+]{X} {url}")
            elif response.status_code == 405:
                errors += 1
                progress_bar.bar_format = f"{Y}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{Y}[+][405 Method Not Allowed][+]{X} {url}")
            elif response.status_code == 500:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{M}[+][500 Internal Server Error][+]{X} {url}")
            elif response.status_code == 504:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{M}[+][504 Gateway Timeout][+]{X} {url}")
            else:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            errors += 1
            progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
            print(f"{R}[Error]{X} {url} - {e}")
        
        progress_bar.update(1)
        sys.stdout.flush()
        time.sleep(delay)
    
    progress_bar.close()
    elapsed_time = time.time() - start_time

    print("\n"f"{C}[+] Finished: {datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')}")


    ####affichage
    if found_urls:
        print(f"\n{G}[+] Found {len(found_urls)} Joomla paths {X}")
    else:
        print(f"\n{R}[+] No Joomla paths found[+] {X}")
      # Statistiques finales
    end_time = time.time()  # Heure de fin
    elapsed_time = end_time - start_time  # Temps écoulé

     # Affichage des statistiques finales
    memory_info = psutil.Process().memory_info()
    memory_used = memory_info.rss / (1024 * 1024)  # Converti en Mo
     

    headers = get_headers(use_random_ua=True)  # Assurez-vous que 'True' ou 'False' est passé en fonction de la commande
    server_type = response.headers.get("Server", "Unknown") 
    # Ajouter l'affichage pour FTP, SSH, Telnet, RDP, VNC
    port_status = {
    21: {"name": "FTP", "status": "", "info": ""},
    22: {"name": "SSH", "status": "", "info": ""},
    23: {"name": "Telnet", "status": "", "info": ""},
    3389: {"name": "RDP", "status": "", "info": ""},
    5900: {"name": "VNC", "status": "", "info": ""}
    }
       
    
    
    # Après avoir exécuté la fonction check_critical_ports
    port_status = check_critical_ports(target_host)

    


   
    print(f"{C}[+] User-Agent Used: {headers['User-Agent']}{X}")
    print(f"{C}[+] Server: {server_type} | target :{X} {G}{url} {X}")
    print(f"{C}[+] Target IP:{X} {G}{site_ip}{X}")
    #####Scan ssh/rdp/ftp 
    ###nt(f"{C}[+] Port 80 Status: {port_80_status}{X}")
    if port_status:  # Si le dictionnaire n'est pas vide
       for port, status_info in port_status.items():
        print(f"{C}[+] Port {port} ({status_info['name']}): {status_info['status']} - {status_info['info']}{X}")
    else:
       print(f"{R}[+] Aucun port critique ouvert sur ce site.{X}")


    
    print(f"{C}[+] Requests Done: {G}{requests_done}{X}")
    print(f"{C}[+] Data Received: {G}{data_received / (1024 * 1024):.3f} MB{X}")
    print(f"{C}[+] Memory used:{G} {memory_used:.2f} MB{X}")
    print(f"{C}[+] Elapsed time: {G}{str(datetime.timedelta(seconds=elapsed_time))}{X}")
    logging.info(f"[Found {len(found_urls)} admin paths]")
    logging.info(f"[Elapsed time: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}]")
    logging.info(f"[Memory used: {memory_used:.2f} MB]")
    logging.info(f"[Requests Done: {len(found_urls) + errors}]")
    logging.info(f"[Errors: {errors}]")


"""# Fonction pour tester les fichiers Joomla
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


 """
############################################🔝joomla🔝 



#######################################################################


############################################ ☑️JS Detection ☑️

# Constantes pour la mise en forme des couleurs
R, G, P, B, M, Y, X, C = '\033[31m', '\033[32m', '\033[35m', '\033[34m', '\033[33m', '\033[33m', '\033[0m', '\033[36;1m'

def check_critical_ports(target_host):
    ports = {21: "FTP", 22: "SSH", 23: "Telnet", 3389: "RDP", 5900: "VNC"}
    port_status = {}

    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout de 2 secondes
        result = sock.connect_ex((target_host, port))

        if result == 0:
            # Le port est ouvert
            port_status[port] = {"name": service, "status": f"{G}🟢 Open{X}", "info": ""}
            try:
                if port == 21:
                    ftp = FTP(target_host, timeout=2)
                    ftp.login()  # Test de connexion anonyme
                    port_status[port]["info"] = "Anonymous Login Allowed"
                    ftp.quit()
                else:
                    sock.send(b'\n')
                    banner = sock.recv(1024).decode().strip()
                    if banner:
                        port_status[port]["info"] = f"{G}Banner: {banner}{X}"
            except Exception as e:
                port_status[port]["info"] = f"Error: {str(e)}"
        sock.close()

    return port_status

def is_port_open(host, port=80, timeout=2):
    """Vérifie si un port est ouvert sur une cible."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False



#######recherche dans la liste d'user agent pour en pioché un aléatoirement
def load_user_agents(file_path="Agent/user_agents.txt"):
    """Charge les User-Agents depuis un fichier et les retourne sous forme de liste."""
    if not os.path.isfile(file_path):
        print(f"[ERROR] Le fichier '{file_path}' n'existe pas!")
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        user_agents = [line.strip() for line in f if line.strip()]  # Enlever les lignes vides et espaces
    return user_agents

def get_headers(use_random_ua, browser_type=None, ua_file="Agent/user_agents.txt"):
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    user_agents = load_user_agents(ua_file)  # Charger les UA depuis le fichier
    
    if use_random_ua and user_agents:  # Vérifie si la liste d'UA n'est pas vide
        headers["User-Agent"] = random.choice(user_agents)  # Prend un UA au hasard
    else:
        headers["User-Agent"] = "Mozilla/5.0 (compatible; VelvetScanner/1.0; +https://example.com/bot)"

    return headers
# Fonction pour tester les fichiers JavaScript
def test_js_files(site, js_file, delay, num_pages):
    target_host = site.replace("http://", "").replace("https://", "").split('/')[0]
    # Récupérer l'IP du site cible
    try:
        site_ip = socket.gethostbyname(site.replace("http://", "").replace("https://", "").split('/')[0])
    except socket.gaierror:
        site_ip = "Unknown"
    
    
    
    if not os.path.exists(js_file):
        print(f"{R}[Error] Le fichier JS spécifié n'existe pas !{X}")
        return
    
    with open(js_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = [path.strip() for path in file.readlines()]
    
    found_urls = []
    errors = 0  # Compteur d'erreurs
    requests_done = 0  # Compteur de requêtes
    data_sent = 0  # Taille des données envoyées (en octets)
    data_received = 0  # Taille des données reçues (en octets)

    progress_bar = tqdm(total=min(len(paths), num_pages), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)
    progress_bar.set_postfix(found=0, errors=0)
    start_time = time.time()

    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            requests_done += 1
            data_sent += len(response.request.body or b'')
            data_received += len(response.content)
            
            if response.status_code == 200:
                found_urls.append(url)
                progress_bar.bar_format = f"{G}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{G}[+]✅ [Found] ✅ [+]{X} {url}")
            elif response.status_code == 403:
                errors += 1
                progress_bar.bar_format = f"{P}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{P}[+][403 Forbidden][+]{X} {url}")
            elif response.status_code == 404:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{R}[+] ❌ [404 Not Found] ❌ [+]{X} {url}")
            elif response.status_code == 400:
                errors += 1
                progress_bar.bar_format = f"{B}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{B}[+][400 Bad Request][+]{X} {url}")
            elif response.status_code == 405:
                errors += 1
                progress_bar.bar_format = f"{Y}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{Y}[+][405 Method Not Allowed][+]{X} {url}")
            elif response.status_code == 500:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{M}[+][500 Internal Server Error][+]{X} {url}")
            elif response.status_code == 504:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{M}[+][504 Gateway Timeout][+]{X} {url}")
            else:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            errors += 1
            progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
            print(f"{R}[Error]{X} {url} - {e}")
        
        progress_bar.update(1)
        sys.stdout.flush()
        time.sleep(delay)
    
    progress_bar.close()
    elapsed_time = time.time() - start_time
    
    print("\n"f"{C}[+] Finished: {datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')}")




    if found_urls:
        print(f"\n{G}[+] Found {len(found_urls)} JavaScript paths{X}")
    else:
        print(f"\n{R}[+] No JavaScript paths found[+]{X}")

    # Statistiques finales
    end_time = time.time()  
    elapsed_time = end_time - start_time  

    memory_info = psutil.Process().memory_info()
    memory_used = memory_info.rss / (1024 * 1024)  # Converti en Mo
    
    headers = get_headers(use_random_ua=True)  # Assurez-vous que 'True' ou 'False' est passé en fonction de la commande
    server_type = response.headers.get("Server", "Unknown") 
    port_status = {
    21: {"name": "FTP", "status": "", "info": ""},
    22: {"name": "SSH", "status": "", "info": ""},
    23: {"name": "Telnet", "status": "", "info": ""},
    3389: {"name": "RDP", "status": "", "info": ""},
    5900: {"name": "VNC", "status": "", "info": ""}
    }
       
    
    
    # Après avoir exécuté la fonction check_critical_ports
    port_status = check_critical_ports(target_host)
    
    
   
    print(f"{C}[+] User-Agent Used:{X} {G}{headers['User-Agent']}{X}")
    print(f"{C}[+] Server: {server_type} | URL: {url}{X}")
    print(f"{C}[+] Target IP: {site_ip}")
    
    ####scan ssh /rdp/ftp
    if port_status:  # Si le dictionnaire n'est pas vide
       for port, status_info in port_status.items():
        print(f"{C}[+] Port {port} ({status_info['name']}): {status_info['status']} - {status_info['info']}{X}")
    else:
       print(f"{R}[+] Aucun port critique ouvert sur ce site.{X}")

    print(f"{C}[+] Requests Done: {G}{requests_done}{X}")
    print(f"{C}[+] Data Received: {G}{data_received / (1024 * 1024):.3f} MB{X}")
    print(f"{C}[+] Memory used:{G} {memory_used:.2f} MB{X}")
    print(f"{C}[+] Elapsed time: {G}{str(datetime.timedelta(seconds=elapsed_time))}{X}")
    logging.info(f"[Found {len(found_urls)} JS paths]")
    logging.info(f"[Elapsed time: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}]")
    logging.info(f"[Memory used: {memory_used:.2f} MB]")
    logging.info(f"[Requests Done: {len(found_urls) + errors}]")
    logging.info(f"[Errors: {errors}]")


#######################################################🔝js Agressive Detections🔝 

###########################htacces  traveaux 
# Définition des couleurs
# Définition des couleurs
R, G, P, B, M, Y, X, C = '\033[31m', '\033[32m', '\033[35m', '\033[34m', '\033[33m', '\033[33m', '\033[0m', '\033[36;1m'
def check_critical_ports(target_host):
    ports = {21: "FTP", 22: "SSH", 23: "Telnet", 3389: "RDP", 5900: "VNC"}
    port_status = {}

    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout de 2 secondes
        result = sock.connect_ex((target_host, port))

        if result == 0:
            # Le port est ouvert
            port_status[port] = {"name": service, "status": f"{G}🟢 Open{X}", "info": ""}
            try:
                if port == 21:
                    ftp = FTP(target_host, timeout=2)
                    ftp.login()  # Test de connexion anonyme
                    port_status[port]["info"] = "Anonymous Login Allowed"
                    ftp.quit()
                else:
                    sock.send(b'\n')
                    banner = sock.recv(1024).decode().strip()
                    if banner:
                        port_status[port]["info"] = f"{G}Banner: {banner}{X}"
            except Exception as e:
                port_status[port]["info"] = f"Error: {str(e)}"
        sock.close()

    return port_status

def is_port_open(host, port=80, timeout=2):
    """Vérifie si un port est ouvert sur une cible."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False
# Définition des couleurs pour la mise en forme
# Définition des couleurs
R, G, P, B, M, Y, X, C = '\033[31m', '\033[32m', '\033[35m', '\033[34m', '\033[33m', '\033[33m', '\033[0m', '\033[36;1m'
#######recherche dans la liste d'user agent pour en pioché un aléatoirement
def load_user_agents(file_path="Agent/user_agents.txt"):
    """Charge les User-Agents depuis un fichier et les retourne sous forme de liste."""
    if not os.path.isfile(file_path):
        print(f"[ERROR] Le fichier '{file_path}' n'existe pas!")
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        user_agents = [line.strip() for line in f if line.strip()]  # Enlever les lignes vides et espaces
    return user_agents

def get_headers(use_random_ua, browser_type=None, ua_file="Agent/user_agents.txt"):
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    user_agents = load_user_agents(ua_file)  # Charger les UA depuis le fichier
    
    if use_random_ua and user_agents:  # Vérifie si la liste d'UA n'est pas vide
        headers["User-Agent"] = random.choice(user_agents)  # Prend un UA au hasard
    else:
        headers["User-Agent"] = "Mozilla/5.0 (compatible; VelvetScanner/1.0; +https://example.com/bot)"

    return headers
def test_htaccess_files(site, ht_file, delay, num_pages):
    target_host = site.replace("http://", "").replace("https://", "").split('/')[0]
    try:
        site_ip = socket.gethostbyname(site.replace("http://", "").replace("https://", "").split('/')[0])
    except socket.gaierror:
        site_ip = "Unknown"

    if not os.path.isfile(ht_file):
        print(f"{R}Le fichier {ht_file} n'existe pas!{X}")
        return

    with open(ht_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = [line.strip() for line in file if line.strip()]

    found_urls = []
    errors = 0
    requests_done = 0
    data_received = 0

    progress_bar = tqdm(total=min(len(paths), num_pages), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)

    start_time = time.time()
    
    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            requests_done += 1
            data_received += len(response.content)

           
            if response.status_code == 200:
                found_urls.append(url)
                progress_bar.colour = "green"
                print(f"{G}[+]✅ [Found] {url}{X}")
            elif response.status_code == 403:
                errors += 1
                progress_bar.colour = "magenta"
                print(f"{P}[403 Forbidden] {url}{X}")
            elif response.status_code == 404:
                errors += 1
                progress_bar.colour = "red"
                print(f"{R}[404 Not Found] {url}{X}")
            else:
                errors += 1
                progress_bar.colour = "red"
                print(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            errors += 1
            progress_bar.colour = "red"
            print(f"{R}[Error] {url} - {e}{X}")

        progress_bar.update(1)
        time.sleep(delay)
    
    

    progress_bar.close()
    elapsed_time = time.time() - start_time
    headers = get_headers(use_random_ua=True)  # Assurez-vous que 'True' ou 'False' est passé en fonction de la commande
    server_type = response.headers.get("Server", "Unknown")  # Récupérer l'info du serveur  "apache/ngnix/"
    port_status = {
    21: {"name": "FTP", "status": "", "info": ""},
    22: {"name": "SSH", "status": "", "info": ""},
    23: {"name": "Telnet", "status": "", "info": ""},
    3389: {"name": "RDP", "status": "", "info": ""},
    5900: {"name": "VNC", "status": "", "info": ""}
    }
       
    
    
    # Après avoir exécuté la fonction check_critical_ports
    port_status = check_critical_ports(target_host)
     

    print("\n"f"\n{C}[+] Finished: {datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')}") 
    if found_urls:
        print(f"\n{G}[+] Found {len(found_urls)} Htacces paths{X}")
    else:
        print(f"\n{R}[+] No HTacces paths found[+]{X}")


    print(f"{C}[+] User-Agent Used:{X} {G}{headers['User-Agent']}{X}")
    print(f"{C}[+] Server: {server_type} | target :{X} {G}{url} {X}")
    print(f"{C}[+] Target IP:{X} {G}{site_ip}{X}")
    
    ####scan ssh /rdp/ftp
    if port_status:  # Si le dictionnaire n'est pas vide
       for port, status_info in port_status.items():
        print(f"{C}[+] Port {port} ({status_info['name']}): {status_info['status']} - {status_info['info']}{X}")
    else:
       print(f"{R}[+] Aucun port critique ouvert sur ce site.{X}")
    print(f"{C}[+] Requests Done: {G}{requests_done}{X}")
    print(f"{C}[+] Data Received: {G}{data_received / (1024 * 1024):.3f} MB{X}")
    print(f"{C}[+] Memory used:  {G}{psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024):.2f} MB {X}")
    print(f"{C}[+] Elapsed time:  {G}{str(datetime.timedelta(seconds=elapsed_time))}{X}")


"""R, G, P, B, M, Y, X, C = '\033[31m', '\033[32m', '\033[35m', '\033[34m', '\033[33m', '\033[33m', '\033[0m', '\033[36;1m'

# Chargement des User-Agents
def load_user_agents(file_path="Agent/user_agents.txt"):
    if not os.path.isfile(file_path):
        print(f"[ERROR] Le fichier '{file_path}' n'existe pas!")
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        user_agents = [line.strip() for line in f if line.strip()]
    print(f"{Y}[DEBUG] {len(user_agents)} User-Agents chargés{X}")  # Debug
    return user_agents

def get_headers(use_random_ua, ua_file="Agent/user_agents.txt"):
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    user_agents = load_user_agents(ua_file)
    if use_random_ua and user_agents:
        headers["User-Agent"] = random.choice(user_agents)
    else:
        headers["User-Agent"] = "Mozilla/5.0 (compatible; VelvetScanner/1.0; +https://example.com/bot)"
    print(f"{C}[DEBUG] User-Agent utilisé: {headers['User-Agent']}{X}")  # Debug
    return headers

def test_htaccess_files(site, ht_file, delay, num_pages):
    try:
        site_ip = socket.gethostbyname(site.replace("http://", "").replace("https://", "").split('/')[0])
    except socket.gaierror:
        site_ip = "Unknown"

    if not os.path.isfile(ht_file):
        print(f"{R}[ERROR] Le fichier {ht_file} n'existe pas!{X}")
        return

    with open(ht_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = [path.strip() for path in file.readlines()]

    print(f"{Y}[DEBUG] {len(paths)} chemins chargés depuis {ht_file}{X}")  # Debug

    if not paths:
        print(f"{R}[ERROR] Aucun chemin trouvé dans {ht_file}!{X}")
        return

    found_urls, errors, requests_done = [], 0, 0
    data_sent, data_received = 0, 0
    progress_bar = tqdm(total=min(len(paths), num_pages), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)
    progress_bar.set_postfix(found=0, errors=0)
    start_time = time.time()

    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        print(f"{B}[DEBUG] Test URL: {url}{X}")  # Debug
        try:
            headers = get_headers(use_random_ua=True)
            response = requests.get(url, headers=headers)
            requests_done += 1
            data_sent += len(response.request.body or b'')
            data_received += len(response.content)
            
            if response.status_code == 200:
                found_urls.append(url)
                progress_bar.set_postfix(found=len(found_urls), errors=errors)
                print(f"{G}[+]✅ [Found] ✅ [+]{X} {url}")
            else:
                errors += 1
                progress_bar.set_postfix(found=len(found_urls), errors=errors)
                print(f"[{response.status_code}] {url}")
        
        except requests.exceptions.RequestException as e:
            errors += 1
            progress_bar.set_postfix(found=len(found_urls), errors=errors)
            print(f"{R}[Error]{X} {url} - {e}")
        
        progress_bar.update(1)
        sys.stdout.flush()
        time.sleep(delay)

    progress_bar.close()
    elapsed_time = time.time() - start_time
    
    print(f"{C}[+] Finished: {datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')}")
    print(f"{C}[+] Target IP: {site_ip}")
    print(f"{C}[+] Requests Done: {requests_done}")
    print(f"{C}[+] Data Received: {data_received / (1024 * 1024):.3f} MB")
    print(f"{C}[+] Memory used: {psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024):.2f} MB")
    print(f"{C}[+] Elapsed time: {str(datetime.timedelta(seconds=elapsed_time))}")
"""



"""
# Fonction pour tester les fichiers .htaccess ####traveaux    a finir 
def test_htaccess_files(site, htaccess_file, delay, number_of_pages):
    if not os.path.exists(htaccess_file):

        return
    
    with open(htaccess_file, 'r') as file:
        paths = file.readlines()

    paths = [path.strip() for path in paths]
    
    print(f"\nDébut de la recherche des fichiers .htaccess sur {site}...\n")
    found_urls = []
    

    # Créer la barre de progression au début, une seule fois
    progress_bar = tqdm(total=min(len(paths),number_of_pages ), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)

    # Initialiser la barre avec un postfix pour afficher les statistiques
    progress_bar.set_postfix(found=0, errors=0)




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
        


    
        # Mise à jour de la barre après chaque requête (sans la recréer)
        progress_bar.update(1)  # Mise à jour après chaque requête
        sys.stdout.flush()  # Forcer l'affichage immédiat

        time.sleep(delay)
    

    # Fermer proprement la barre de progression après la boucle
    progress_bar.close()


    if found_urls:
        print(f"{GREEN}[Found {len(found_urls)} htaccess paths]{RESET}")
    else:
        print(f"{RED}[No htaccess paths found]{RESET}")"""

###########################htacces  func





#######################################################☑️Panel Agressive detections ////Done☑️

# Constantes pour la mise en forme des couleurs
R, G, P, B, M, Y, X, C = '\033[31m', '\033[32m', '\033[35m', '\033[34m', '\033[33m', '\033[33m', '\033[0m', '\033[36;1m'

def check_critical_ports(target_host):
    ports = {21: "FTP", 22: "SSH", 23: "Telnet", 3389: "RDP", 5900: "VNC"}
    port_status = {}

    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout de 2 secondes
        result = sock.connect_ex((target_host, port))

        if result == 0:
            # Le port est ouvert
            port_status[port] = {"name": service, "status": f"{G}🟢 Open{X}", "info": ""}
            try:
                if port == 21:
                    ftp = FTP(target_host, timeout=2)
                    ftp.login()  # Test de connexion anonyme
                    port_status[port]["info"] = "Anonymous Login Allowed"
                    ftp.quit()
                else:
                    sock.send(b'\n')
                    banner = sock.recv(1024).decode().strip()
                    if banner:
                        port_status[port]["info"] = f"{G}Banner: {banner}{X}"
            except Exception as e:
                port_status[port]["info"] = f"Error: {str(e)}"
        sock.close()

    return port_status




#######recherche dans la liste d'user agent pour en pioché un aléatoirement
def load_user_agents(file_path="Agent/user_agents.txt"):
    """Charge les User-Agents depuis un fichier et les retourne sous forme de liste."""
    if not os.path.isfile(file_path):
        print(f"[ERROR] Le fichier '{file_path}' n'existe pas!")
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        user_agents = [line.strip() for line in f if line.strip()]  # Enlever les lignes vides et espaces
    return user_agents

def get_headers(use_random_ua, browser_type=None, ua_file="Agent/user_agents.txt"):
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    user_agents = load_user_agents(ua_file)  # Charger les UA depuis le fichier
    
    if use_random_ua and user_agents:  # Vérifie si la liste d'UA n'est pas vide
        headers["User-Agent"] = random.choice(user_agents)  # Prend un UA au hasard
    else:
        headers["User-Agent"] = "Mozilla/5.0 (compatible; VelvetScanner/1.0; +https://example.com/bot)"

    return headers
# Fonction pour tester les panels d'administration
def test_panel_files(site, panel_file, delay, num_pages):
    target_host = site.replace("http://", "").replace("https://", "").split('/')[0]    
      # Récupérer l'IP du site cible
    try:
        site_ip = socket.gethostbyname(site.replace("http://", "").replace("https://", "").split('/')[0])
    except socket.gaierror:
        site_ip = "Unknown"


    
    if not os.path.exists(panel_file):
        print(f"{R}[Error] Le fichier Panel spécifié n'existe pas !{X}")
        return
    
    with open(panel_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = [path.strip() for path in file.readlines()]
    
    found_urls = []
    errors = 0  # Compteur d'erreurs
    requests_done = 0  # Compteur de requêtes
    data_sent = 0  # Taille des données envoyées (en octets)
    data_received = 0  # Taille des données reçues (en octets)

    progress_bar = tqdm(total=min(len(paths), num_pages), desc="Scanning Panels", unit="req", ncols=80, dynamic_ncols=True, leave=True)
    progress_bar.set_postfix(found=0, errors=0)
    start_time = time.time()

    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            requests_done += 1
            data_sent += len(response.request.body or b'')
            data_received += len(response.content)
            
            if response.status_code == 200:
                found_urls.append(url)
                progress_bar.bar_format = f"{G}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{G}[+]✅ [Found] ✅ [+]{X} {url}")
            elif response.status_code == 403:
                errors += 1
                progress_bar.bar_format = f"{P}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{P}[+][403 Forbidden][+]{X} {url}")
            elif response.status_code == 404:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{R}[+] ❌ [404 Not Found] ❌ [+]{X} {url}")
            elif response.status_code == 400:
                errors += 1
                progress_bar.bar_format = f"{B}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{B}[+][400 Bad Request][+]{X} {url}")
            elif response.status_code == 405:
                errors += 1
                progress_bar.bar_format = f"{Y}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{Y}[+][405 Method Not Allowed][+]{X} {url}")
            elif response.status_code == 500:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{M}[+][500 Internal Server Error][+]{X} {url}")
            elif response.status_code == 504:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{M}[+][504 Gateway Timeout][+]{X} {url}")
            else:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            errors += 1
            progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
            print(f"{R}[Error]{X} {url} - {e}")
        
        progress_bar.update(1)
        sys.stdout.flush()
        time.sleep(delay)
    
    progress_bar.close()
    elapsed_time = time.time() - start_time
    print("\n"f"{C}[+] Finished: {datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')}") 
    if found_urls:
        print(f"\n{G}[+] Found {len(found_urls)} Panel paths{X}")
    else:
        print(f"\n{R}[No Panel paths found[+] {X}")

    # Statistiques finales
    end_time = time.time()  
    elapsed_time = end_time - start_time  

    memory_info = psutil.Process().memory_info()
    memory_used = memory_info.rss / (1024 * 1024)  # Converti en Mo
    headers = get_headers(use_random_ua=True)  # Assurez-vous que 'True' ou 'False' est passé en fonction de la commande
    server_type = response.headers.get("Server", "Unknown") 
    port_status = {
    21: {"name": "FTP", "status": "", "info": ""},
    22: {"name": "SSH", "status": "", "info": ""},
    23: {"name": "Telnet", "status": "", "info": ""},
    3389: {"name": "RDP", "status": "", "info": ""},
    5900: {"name": "VNC", "status": "", "info": ""}
    }
       
    
    
    # Après avoir exécuté la fonction check_critical_ports
    port_status = check_critical_ports(target_host)



    print(f"{C}[+] User-Agent Used:{X} {G}{headers['User-Agent']}{X}")
    print(f"{C}[+] Server: {server_type} | target :{site_ip} {X}")
    print(f"{C}[+] Target IP: {site_ip}") 
    ####scan ssh /rdp/ftp
    if port_status:  # Si le dictionnaire n'est pas vide
       for port, status_info in port_status.items():
        print(f"{C}[+] Port {port} ({status_info['name']}): {status_info['status']} - {status_info['info']}{X}")
    else:
       print(f"{R}[+] Aucun port critique ouvert sur ce site.{X}")
    
    print(f"{C}[+] Requests Done: {G}{requests_done}{X}")
    print(f"{C}[+] Data Received: {G}{data_received / (1024 * 1024):.3f} MB{X}")
    print(f"{C}[+] Memory used:{G} {memory_used:.2f} MB{X}")
    print(f"{C}[+] Elapsed time: {G}{str(datetime.timedelta(seconds=elapsed_time))}{X}")
    logging.info(f"[Found {len(found_urls)} Panel paths]")  
    logging.info(f"[Elapsed time: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}]")  
    logging.info(f"[Memory used: {memory_used:.2f} MB]")  
    logging.info(f"[Requests Done: {len(found_urls) + errors}]")  
    logging.info(f"[Errors: {errors}]")  
#######################################################🔝Panel Detections🔝 





#☑️ADMIN FINDER CHAIn ////////Done☑️ 



R, G, P, B, M, Y, X, C = '\033[31m', '\033[32m', '\033[35m', '\033[34m', '\033[33m', '\033[33m', '\033[0m', '\033[36;1m'

R, G, P, B, M, Y, X, C = '\033[31m', '\033[32m', '\033[35m', '\033[34m', '\033[33m', '\033[33m', '\033[0m', '\033[36;1m'

def check_critical_ports(target_host):
    ports = {21: "FTP", 22: "SSH", 23: "Telnet", 3389: "RDP", 5900: "VNC"}
    port_status = {}

    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout de 2 secondes
        result = sock.connect_ex((target_host, port))

        if result == 0:
            # Le port est ouvert
            port_status[port] = {"name": service, "status": f"{G}🟢 Open{X}", "info": ""}
            try:
                if port == 21:
                    ftp = FTP(target_host, timeout=2)
                    ftp.login()  # Test de connexion anonyme
                    port_status[port]["info"] = "Anonymous Login Allowed"
                    ftp.quit()
                else:
                    sock.send(b'\n')
                    banner = sock.recv(1024).decode().strip()
                    if banner:
                        port_status[port]["info"] = f"{G}Banner: {banner}{X}"
            except Exception as e:
                port_status[port]["info"] = f"Error: {str(e)}"
        sock.close()

    return port_status



#######recherche dans la liste d'user agent pour en pioché un aléatoirement
def load_user_agents(file_path="Agent/user_agents.txt"):
    """Charge les User-Agents depuis un fichier et les retourne sous forme de liste."""
    if not os.path.isfile(file_path):
        print(f"[ERROR] Le fichier '{file_path}' n'existe pas!")
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        user_agents = [line.strip() for line in f if line.strip()]  # Enlever les lignes vides et espaces
    return user_agents

def get_headers(use_random_ua, browser_type=None, ua_file="Agent/user_agents.txt"):
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    user_agents = load_user_agents(ua_file)  # Charger les UA depuis le fichier
    
    if use_random_ua and user_agents:  # Vérifie si la liste d'UA n'est pas vide
        headers["User-Agent"] = random.choice(user_agents)  # Prend un UA au hasard
    else:
        headers["User-Agent"] = "Mozilla/5.0 (compatible; VelvetScanner/1.0; +https://example.com/bot)"

    return headers

# Fonction pour tester les fichiers ADLmin ### a finir l'add -verbose PATH 
def test_admin_combinations(site, admin_file, delay, num_pages):
   #Extraction du domaine cible
    target_host = site.replace("http://", "").replace("https://", "").split('/')[0]
   # Récupérer l'IP du site cible
    try:
        site_ip = socket.gethostbyname(site.replace("http://", "").replace("https://", "").split('/')[0])
    except socket.gaierror:
        site_ip = "Unknown"

   
   
   
   
    if not os.path.exists(admin_file):
        print(f"{R}[Error] Le fichier ADMIN spécifié n'existe pas !{X}")
        return
    
    
    with open(admin_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = [path.strip() for path in file.readlines()]
    
    found_urls = []
    errors = 0  # Compteur d'erreurs
    requests_done = 0  # Compteur de requêtes
    data_sent = 0  # Taille des données envoyées (en octets)
    data_received = 0  # Taille des données reçues (en octets)

    progress_bar = tqdm(total=min(len(paths), num_pages), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)
    progress_bar.set_postfix(found=0, errors=0)
    start_time = time.time()

    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            requests_done += 1
            data_sent += len(response.request.body or b'')
            data_received += len(response.content)
            
            if response.status_code == 200:
                found_urls.append(url)
                progress_bar.bar_format = f"{G}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{G}[+]✅ [Found] ✅ [+]{X} {url}")
            elif response.status_code == 403:
                errors += 1
                progress_bar.bar_format = f"{P}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{P}[+][403 Forbidden][+]{X} {url}")
            elif response.status_code == 404:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{R}[+] ❌ [404 Not Found] ❌ [+]{X} {url}")
            elif response.status_code == 400:
                errors += 1
                progress_bar.bar_format = f"{B}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{B}[+][400 Bad Request][+]{X} {url}")
            elif response.status_code == 405:
                errors += 1
                progress_bar.bar_format = f"{Y}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{Y}[+][405 Method Not Allowed][+]{X} {url}")
            elif response.status_code == 500:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{M}[+][500 Internal Server Error][+]{X} {url}")
            elif response.status_code == 504:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{M}[+][504 Gateway Timeout][+]{X} {url}")
            else:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            errors += 1
            progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
            print(f"{R}[Error]{X} {url} - {e}")
        
        progress_bar.update(1)
        sys.stdout.flush()
        time.sleep(delay)
    
    progress_bar.close()
    elapsed_time = time.time() - start_time
    
    
    print("\n"f"{C}[+] Finished: {datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')}")
    if found_urls:
        print(f"\n{G}[+] Found {len(found_urls)} ADMIN Path {X}")
    else:
        print(f"\n{R}[+] No Admin paths found{X}")
    
    



    # Statistiques finales
    memory_info = psutil.Process().memory_info()
    memory_used = memory_info.rss / (1024 * 1024)  # Converti en Mo
    headers = get_headers(use_random_ua=True)
    server_type = response.headers.get("Server", "Unknown") 
    port_status = {
    21: {"name": "FTP", "status": "", "info": ""},
    22: {"name": "SSH", "status": "", "info": ""},
    23: {"name": "Telnet", "status": "", "info": ""},
    3389: {"name": "RDP", "status": "", "info": ""},
    5900: {"name": "VNC", "status": "", "info": ""}
    }
       
    
    
    # Après avoir exécuté la fonction check_critical_ports
    port_status = check_critical_ports(target_host)




    print(f"{C}[+] User-Agent Used:{X} {G}{headers['User-Agent']}{X}")
    print(f"{C}[+] Server: {server_type} | target :{X} {G}{url} {X}")
    print(f"{C}[+] Target IP:{X} {G}{site_ip}{X}")
    ####Port status RDP/ssh/ftp etc...
    ##print(f"{C}[+] Port 80 Status: {port_80_status}{X}")
    if port_status:  # Si le dictionnaire n'est pas vide
       for port, status_info in port_status.items():
        print(f"{C}[+] Port {port} ({status_info['name']}): {status_info['status']} - {status_info['info']}{X}")
    else:
       print(f"{R}[+] Aucun port critique ouvert sur ce site.{X}")
    
    print(f"{C}[+] Requests Done: {G}{requests_done}{X}")
    print(f"{C}[+] Data Received: {G}{data_received / (1024 * 1024):.3f} MB{X}")
    print(f"{C}[+] Memory used:{G} {memory_used:.2f} MB{X}")
    print(f"{C}[+] Elapsed time: {G}{str(datetime.timedelta(seconds=elapsed_time))}{X}")
    
    logging.info(f"[Found {len(found_urls)} admin paths]")
    logging.info(f"[Elapsed time: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}]")
    logging.info(f"[Memory used: {memory_used:.2f} MB]")
    logging.info(f"[Requests Done: {requests_done}]")
    logging.info(f"[Errors: {errors}]")


"""
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
        logging.warning(f"[No admin paths found]")"""




############################## 🔝ADMIN chain a  add certaine options ///Done 🔝

#☑️API agressive Detections☑️ 
# Fonction pour tester les chemins d'API# Constantes pour la mise en forme des couleurs
R, G, P, B, M, Y, X, C = '\033[31m', '\033[32m', '\033[35m', '\033[34m', '\033[33m', '\033[33m', '\033[0m', '\033[36;1m'




def check_critical_ports(target_host):
    ports = {21: "FTP", 22: "SSH", 23: "Telnet", 3389: "RDP", 5900: "VNC"}
    port_status = {}

    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout de 2 secondes
        result = sock.connect_ex((target_host, port))

        if result == 0:
            # Le port est ouvert
            port_status[port] = {"name": service, "status": f"{G}🟢 Open{X}", "info": ""}
            try:
                if port == 21:
                    ftp = FTP(target_host, timeout=2)
                    ftp.login()  # Test de connexion anonyme
                    port_status[port]["info"] = "Anonymous Login Allowed"
                    ftp.quit()
                else:
                    sock.send(b'\n')
                    banner = sock.recv(1024).decode().strip()
                    if banner:
                        port_status[port]["info"] = f"{G}Banner: {banner}{X}"
            except Exception as e:
                port_status[port]["info"] = f"Error: {str(e)}"
        sock.close()

    return port_status





#######recherche dans la liste d'user agent pour en pioché un aléatoirement
def load_user_agents(file_path="Agent/user_agents.txt"):
    """Charge les User-Agents depuis un fichier et les retourne sous forme de liste."""
    if not os.path.isfile(file_path):
        print(f"[ERROR] Le fichier '{file_path}' n'existe pas!")
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        user_agents = [line.strip() for line in f if line.strip()]  # Enlever les lignes vides et espaces
    return user_agents

def get_headers(use_random_ua, browser_type=None, ua_file="Agent/user_agents.txt"):
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    user_agents = load_user_agents(ua_file)  # Charger les UA depuis le fichier
    
    if use_random_ua and user_agents:  # Vérifie si la liste d'UA n'est pas vide
        headers["User-Agent"] = random.choice(user_agents)  # Prend un UA au hasard
    else:
        headers["User-Agent"] = "Mozilla/5.0 (compatible; VelvetScanner/1.0; +https://example.com/bot)"

    return headers

# Fonction pour tester les chemins d'API
def test_api_combinations(site, api_file, delay, num_pages):
       #Extraction du domaine cible
    target_host = site.replace("http://", "").replace("https://", "").split('/')[0]
    # Récupérer l'IP du site cible
    try:
        site_ip = socket.gethostbyname(site.replace("http://", "").replace("https://", "").split('/')[0])
    except socket.gaierror:
        site_ip = "Unknown"
    if not os.path.isfile(api_file):
        print(f"{R}Le fichier d'API {api_file} n'existe pas!{X}")
        logging.error(f"Le fichier d'API {api_file} n'existe pas!")
        return

    with open(api_file, 'r', encoding='utf-8', errors='ignore') as file:
        paths = file.readlines()

    paths = [path.strip() for path in paths]

    # Initialisation des variables pour les statistiques
    found_urls = []
    errors = 0
    requests_done = 0
    data_sent = 0
    data_received = 0

    # Créer la barre de progression
    progress_bar = tqdm(total=min(len(paths), num_pages), desc="Scanning", unit="req", ncols=80, dynamic_ncols=True, leave=True)
    progress_bar.set_postfix(found=0, errors=0)
    start_time = time.time()

    # Boucle principale pour tester les chemins d'API
    for i, path in enumerate(paths):
        if i >= num_pages:
            break
        url = f"{site}/{path}"
        try:
            response = requests.get(url)
            requests_done += 1
            data_sent += len(response.request.body or b'')
            data_received += len(response.content)

            # Gestion des codes de réponse
            if response.status_code == 200:
                found_urls.append(url)
                progress_bar.bar_format = f"{G}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{G}[Found]{X} {url}")
                logging.info(f"[Found] {url}")
            elif response.status_code == 403:
                errors += 1
                progress_bar.bar_format = f"{P}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{P}[403 Forbidden]{X} {url}")
                logging.error(f"[403 Forbidden] {url}")
            elif response.status_code == 404:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{R}[404 Not Found]{X} {url}")
                logging.warning(f"[404 Not Found] {url}")
            elif response.status_code == 400:
                errors += 1
                progress_bar.bar_format = f"{B}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{B}[400 Bad Request]{X} {url}")
                logging.error(f"[400 Bad Request] {url}")
            elif response.status_code == 405:
                errors += 1
                progress_bar.bar_format = f"{Y}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{Y}[405 Method Not Allowed]{X} {url}")
                logging.error(f"[405 Method Not Allowed] {url}")
            elif response.status_code == 500:
                errors += 1
                progress_bar.bar_format = f"{M}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{M}[500 Internal Server Error]{X} {url}")
                logging.error(f"[500 Internal Server Error] {url}")
            elif response.status_code == 504:
                errors += 1
                progress_bar.bar_format = f"{O}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"{O}[504 Gateway Timeout]{X} {url}")
                logging.error(f"[504 Gateway Timeout] {url}")
            else:
                errors += 1
                progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
                print(f"[{response.status_code}] {url}")
                logging.info(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            errors += 1
            progress_bar.bar_format = f"{R}{{l_bar}}{{bar}}{{r_bar}}{X}"
            print(f"{R}[Error]{X} {url} - {e}")
            logging.error(f"[Error] {url} - {e}")

        progress_bar.update(1)
        sys.stdout.flush()
        time.sleep(delay)

    progress_bar.close()
    
    # Statistiques finales
    elapsed_time = time.time() - start_time
    memory_info = psutil.Process().memory_info()
    memory_used = memory_info.rss / (1024 * 1024)  # Converti en Mo
    headers = get_headers(use_random_ua=True)
    server_type = response.headers.get("Server", "Unknown") 
    port_status = {
    21: {"name": "FTP", "status": "", "info": ""},
    22: {"name": "SSH", "status": "", "info": ""},
    23: {"name": "Telnet", "status": "", "info": ""},
    3389: {"name": "RDP", "status": "", "info": ""},
    5900: {"name": "VNC", "status": "", "info": ""}
    }
       
    
    
    # Après avoir exécuté la fonction check_critical_ports
    port_status = check_critical_ports(target_host)
    
    print("\n"f"{C}[+] Finished: {datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')}")
    
    if found_urls:
        print(f"\n{G}[+] Found {len(found_urls)} API {X}")
        logging.info(f"[+] Found {len(found_urls)} API ")
    else:
        print(f"\n{R}[+] No API paths found[+] {X}")
        logging.warning(f"{R}[+] No API paths found [+] ")
     
    # Affichage des statistiques finales
    print(f"{C}[+] User-Agent Used:{X} {G}{headers['User-Agent']}{X}")
    print(f"{C}[+] Server: {server_type} | target :{X} {G}{url} {X}")
    print(f"{C}[+] Target IP:{X} {G}{site_ip}{X}")
    ####Port status RDP/ssh/ftp etc...
    ##print(f"{C}[+] Port 80 Status: {port_80_status}{X}")
    if port_status:  # Si le dictionnaire n'est pas vide
       for port, status_info in port_status.items():
        print(f"{C}[+] Port {port} ({status_info['name']}): {status_info['status']} - {status_info['info']}{X}")
    else:
       print(f"{R}[+] Aucun port critique ouvert sur ce site.{X}")
    
    print(f"{C}[+] Requests Done: {G}{requests_done}{X}")
    print(f"{C}[+] Data Received: {G}{data_received / (1024 * 1024):.3f} MB{X}")
    print(f"{C}[+] Memory used:{G} {memory_used:.2f} MB{X}")
    print(f"{C}[+] Elapsed time: {G}{str(datetime.timedelta(seconds=elapsed_time))}{X}")
    
    # Enregistrement des statistiques dans un fichier de logs
    logging.info(f"[Elapsed time: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}]")
    logging.info(f"[Memory used: {memory_used:.2f} MB]")
    logging.info(f"[Requests Done: {requests_done}]")
    logging.info(f"[Errors: {errors}]")
###############################################################################🔝API end🔝 


#☑️ Fonction principale pour gérer les arguments☑️
def main():
    parser = argparse.ArgumentParser(description="Exécuter des recherches pour des fichiers WordPress, API ou autres fichiers sur un site")
    parser.add_argument("-u", "--url", required=True, help="URL du site cible")
    
    parser.add_argument("-f", "--file_type", required=False, help="Type de fichier (php, html, js, etc.)")
    
    parser.add_argument("-wp", "--wordpress_file", required=False, help="Chemin vers le fichier de chemins WordPress") 
    parser.add_argument("-api", "--api_file", required=False, help="Chemin vers le fichier de chemins API")
    parser.add_argument("-admin", "--admin_file", required=False, help="Chemin vers le fichier de chemins d'administration")
    parser.add_argument("-joomla", "--joomla_file", required=False, help="Chemin vers le fichier de chemins Joomla")
    parser.add_argument('-js', '--javascript', metavar='JS_FILE', help='Fichier contenant la wordlist des fichiers JavaScript')
    parser.add_argument("-ht", "--ht_file", help="Fichier contenant les chemins .htaccess")  # Correction ici
    #### commande a rajouté : 
    #### parser.add_argument('-ht', '--ht_file', required=True, help="Chemin vers le fichier .htaccess")
    #### parser.add_argument('-ht', '--ht_file', required=True, help="Chemin vers le fichier .htaccess")
    ######parser.add_argument("--random-user-agent", action="store_true", help="Utiliser un User-Agent aléatoire") ##### a finir en boléen browser func
    ######parser.add_argument("--random-user-agent", "-ua", nargs="?", const="random", choices=["firefox", "chrome", "safari", "random"], help="Utiliser un User-Agent aléatoire (firefox, chrome, safari, ou random)") ##### a finir  en booléen  user agent random mode 
    parser.add_argument("--browser", choices=["firefox", "chrome", "safari"], help="Specify browser type for User-Agent")
    parser.add_argument('-panel', '--panel', metavar='PANEL_FILE', help='Fichier contenant les chemins des panels')
    parser.add_argument("-v", "--version", action="store_true", help="Vérifier la version de WordPress")
    parser.add_argument("-t", "--time", type=int, required=True, help="Temps entre les requêtes")
    parser.add_argument("-n", "--number_of_pages", type=int, default=5, help="Nombre maximum de pages à tester (par défaut: 5)") 
    parser.add_argument("-thread", "--threads", type=int, default=10, help="Nombre de threads pour l'exécution en multithreading (par défaut: 10)")
    ##################################################################################################################################################🔝
    
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
    



    

####traveaux a  finir HT acess Fuzzer 
# #### htaccess_folder = args.htaccess_file

# Vérification si l'argument htaccess est spécifié
    ###if htaccess_folder:
###  test_htaccess_files(site, htaccess_folder, delay, num_pages)
    ###else:
### print(f"{RED}[Error] Vous devez spécifier un dossier contenant le fichier htacces.txt.{RESET}")


    


    ####### API file☑️
    if args.api_file:
        api_file = args.api_file
        test_api_combinations(site, api_file, delay, num_pages)
    ####### WP file ☑️
    elif args.wordpress_file:
        wp_file = args.wordpress_file
        test_wordpress_files(site, wp_file, delay, num_pages)
    
    
    if args.ht_file:  # Vérifier args.ht_file au lieu de args.ht
        test_htaccess_files(args.url, args.ht_file, args.time, args.number_of_pages)
    
    ##Vérification de l'option -joomla et des autres paramètres
    if args.joomla_file:
        if not args.joomla_file:
            print(f"{RED}[Error] Vous devez spécifier un fichier Joomla pour tester.{RESET}")
            return
        test_joomla_files(site, args.joomla_file, delay, num_pages)
    if args.javascript:
        js_file = args.javascript
        test_js_files(args.url, js_file, args.time, args.number_of_pages)


    

    ######admin file ☑️
    elif args.admin_file:
        admin_file = args.admin_file
        test_admin_combinations(site, admin_file, delay, num_pages)
    elif args.file_type:
        file_type = args.file_type
        test_file_combinations(site, file_type, delay, num_pages)
    
    ######☑️Panel 
    
    if args.panel:
        test_panel_files(args.url, args.panel, args.time, args.number_of_pages)
    

    """if len(sys.argv) != 9:
        print("Usage: python3 Velvet.py -u <target> -ht htacces/htacces.txt -t <delay> -n <num_pages>")
        sys.exit(1)
    
    target = sys.argv[2]
    ht_file = sys.argv[4]
    delay = float(sys.argv[6])
    num_pages = int(sys.argv[8])
    
    test_htaccess_files(target, ht_file, delay, num_pages)"""

    
    
    ####################### a finir 
    # Utiliser le fichier avec un chemin approprié
    """ht_file = f"htacces/{file_type}.txt"
    
    # Vérification de l'existence du fichier
    if not os.path.exists(ht_file):
        print(f"[ERROR] Le fichier {ht_file} n'existe pas!")
    else:
        print(f"[INFO] Fichier trouvé: {ht_file}")
        test_htaccess_files(args.url, ht_file, args.delay, args.num_pages)
    if args.file_type:
    file_type = args.file_type
    ht_file = f"Access/{file_type}.txt"  # Assurez-vous que ce chemin est correct
    
    if not os.path.exists(ht_file):
        print(f"[ERROR] Le fichier {ht_file} n'existe pas!")
    else:
        test_htaccess_files(site, ht_file, delay, num_pages)"""


    """else:
        print(f"{R}[Error]{x} - Vous devez spécifier soit un fichier WordPress (-wp), un fichier API (-api), un fichier admin (-admin), ou un type de fichier (-f) pour effectuer un scan.")
        logging.error(f"[Error] Vous devez spécifier soit un fichier WordPress (-wp), un fichier API (-api), un fichier admin (-admin), ou un type de fichier (-f) pour effectuer un scan.")
    else:
        print(f"{R}[Error]{x} - Vous devez spécifier soit un fichier WordPress (-wp), un fichier API (-api), un fichier admin (-admin), ou un type de fichier (-f) pour effectuer un scan.")
        logging.error(f"[Error] Vous devez spécifier soit un fichier WordPress (-wp), un fichier API (-api), un fichier admin (-admin), ou un type de fichier (-f) pour effectuer un scan.") """








if __name__ == "__main__":
    main()
