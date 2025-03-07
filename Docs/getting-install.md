--
## Installation

### Prérequis

Avant d'installer et d'utiliser **APTDork**, assurez-vous que vous avez **Python** installé sur votre système. Ce projet fonctionne avec **Python 3.x**. Si vous n'avez pas Python installé, suivez les étapes ci-dessous pour l'installer en fonction de votre système d'exploitation.

### Installation de Python

#### Sur Windows

1. Téléchargez la dernière version de Python 3.x depuis le site officiel :  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Lors de l'installation, **assurez-vous de cocher l'option** `Add Python to PATH` avant de cliquer sur "Install Now".

3. Vérifiez l'installation en ouvrant l'invite de commande (CMD) et en tapant :
   ```bash
   python --version
   ```

#### Sur macOS

1. Si vous n'avez pas Python installé, vous pouvez le télécharger depuis :  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Si vous avez déjà installé Homebrew, vous pouvez installer Python via la commande suivante :
   ```bash
   brew install python
   ```

3. Vérifiez l'installation en ouvrant un terminal et en tapant :
   ```bash
   python3 --version
   ```

#### Sur Linux

1. La plupart des distributions Linux ont déjà Python installé. Pour vérifier la version de Python installée, ouvrez un terminal et tapez :
   ```bash
   python3 --version
   ```

2. Si Python n'est pas installé, vous pouvez l'installer avec les commandes suivantes selon votre distribution :

   - Pour **Ubuntu/Debian** :
     ```bash
     sudo apt update
     sudo apt install python3
     ```

   - Pour **Fedora** :
     ```bash
     sudo dnf install python3
     ```

   - Pour **Arch Linux** :
     ```bash
     sudo pacman -S python
     ```

### Installation des dépendances

1. Clonez le dépôt du projet ou téléchargez les fichiers nécessaires :

   ```bash
   git clone https://github.com/votre-utilisateur/APTDork.git
   ```

2. Accédez au répertoire du projet :
   ```bash
   cd APTDork
   ```

3. Installez les dépendances requises via `pip`. Si vous avez Python 3 installé, utilisez `pip3` pour vous assurer que vous installez les packages pour la bonne version de Python :

   ```bash
   pip3 install -r requirements.txt
   ```

   Si vous utilisez **Windows**, vous pouvez utiliser la commande suivante pour vous assurer que vous utilisez `pip` pour Python 3 :

   ```bash
   pip install -r requirements.txt
   ```

### Vérification de l'installation

1. Une fois l'installation terminée, vous pouvez vérifier que les dépendances sont correctement installées en exécutant le script sans arguments supplémentaires pour voir s'il affiche l'ASCII art :

   ```bash
   python3 aptdork.py
   ```

2. Si l'installation est réussie, vous verrez l'ASCII art et le message de bienvenue dans la console.

---

Cela couvre l'installation de Python ainsi que l'installation des dépendances pour toutes les versions courantes de Python (Python 3.x). Vous pouvez adapter ces instructions si nécessaire, selon l'environnement spécifique dans lequel vous souhaitez installer **APTDork**.
