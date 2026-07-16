import os
import sys
import time
import base64
import random
import string

# Couleurs ANSI pour le style "RedTiger"
GREEN = "\033[92m"
RED = "\033[91m"
WHITE = "\033[97m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Dictionnaire de toutes les options réorganisées
OPTIONS = {
    "01": "Générateur de Sessions (Unique)",
    "02": "Permissions de Token",
    "03": "Analyseur de Sécurité",
    "04": "Inspecteur de Profil",
    "05": "Connexion Automatique",
    "06": "Sauvegarde de Groupes",
    "07": "Restauration Groupes",
    "08": "Token Grabber (Simulateur)",
    "09": "Exportateur d'Infos",
    "10": "Générateur Invit Bot",
    "11": "Nettoyeur de Salons",
    "12": "Configuration de Bot",
    "13": "Sauvegarde Serveur",
    "14": "Restauration Serveur",
    "15": "Inspecteur de Bot",
    "16": "Changer Langue Bot",
    "17": "Changer Thème CLI",
    "18": "Extraction de Guilde",
    "19": "Vérificateur Webhook",
    "20": "Testeur de Webhook",
    "21": "Suppression Webhook",
    "22": "Générateur Webhook",
    "23": "Générateur de Clés",
    "24": "Diagnostic Réseau",
    "25": "Test Ping & Latence",
    "26": "Analyseur DNS/HTTP",
    "27": "Calculateur Réseau"
}

def generate_session_token():
    random_id = "".join(random.choice(string.digits) for _ in range(18))
    part1 = base64.b64encode(random_id.encode('utf-8')).decode('utf-8').replace('=', '')
    part2 = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    part3 = "".join(random.choice(string.ascii_letters + string.digits + "-_") for _ in range(38))
    return f"{part1}.{part2}.{part3}"

def generate_fake_grabbed_token(user_id):
    try:
        # Encodage de l'ID fourni par l'utilisateur
        part1 = base64.b64encode(user_id.encode('utf-8')).decode('utf-8').replace('=', '')
    except Exception:
        part1 = "MTUxNDcwMjI3ODQzMzU3NTEwNQ"
    part2 = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    part3 = "".join(random.choice(string.ascii_letters + string.digits + "-_") for _ in range(38))
    return f"{part1}.{part2}.{part3}"

def run_network_lookup(ip_or_domain):
    isp_list = ["Orange Business", "Free Telecom Enterprise", "SFR Business", "Bouygues Telecom Cloud"]
    city_list = ["Paris", "Lyon", "Marseille", "Lille", "Bordeaux"]
    dns_host = f"node-{random.randint(100, 999)}.{random.choice(isp_list).lower().replace(' ', '-')}.fr"
    lat = round(random.uniform(43.0, 50.0), 4)
    lon = round(random.uniform(-1.5, 6.0), 4)

    print(f"\n{CYAN}[*] Interrogation des serveurs DNS pour : {ip_or_domain}...{RESET}")
    time.sleep(1)
    print(f"{CYAN}[*] Analyse des tables de routage...{RESET}\n")
    time.sleep(1)
    
    print(f"{RED}┌─── [ RAPPORT DIAGNOSTIC : {ip_or_domain.upper()} ] ─────────────────────────{RESET}")
    print(f"{RED}│{RESET} {WHITE}Cible analysée    :{RESET} {ip_or_domain}")
    print(f"{RED}│{RESET} {WHITE}Adresse IP WAN    :{RESET} 192.168.{random.randint(1, 254)}.{random.randint(1, 254)}")
    print(f"{RED}│{RESET} {WHITE}Hôte Reverse DNS  :{RESET} {dns_host}")
    print(f"{RED}│{RESET} {WHITE}FAI Détecté       :{RESET} {random.choice(isp_list)}")
    print(f"{RED}│{RESET} {WHITE}Centre de données :{RESET} {random.choice(city_list)}")
    print(f"{RED}│{RESET} {WHITE}Coordonnées Nœud  :{RESET} Lat {lat} / Lon {lon}")
    print(f"{RED}│{RESET} {WHITE}Statut de Liaison :{RESET} Actif (100% stable)")
    print(f"{RED}└─────────────────────────────────────────────────────────────{RESET}")

def draw_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(RED + """
████╗   ███╗██╗   ██╗██╗  ████████╗██╗    ██████╗ ███████╗
████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚════██╗██╔════╝
██╔████╔██║██║   ██║██║     ██║   ██║     █████╔╝███████╗
██║╚██╔╝██║██║   ██║██║     ██║   ██║    ██╔═══╝ ╚════██║
██║ ╚═╝    ██║╚██████╔╝███████╗██║   ██║    ███████╗███████║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝    ╚══════╝╚══════╝
                                                         
                               github.com/m22sss2
    """ + RESET)
    
    print(RED + " ┌──" + WHITE + " [I] Info" + RED + " ────────────────────────────────────────────────────────────────────────" + WHITE + " Back [B] " + RED + "──┐" + RESET)
    print(RED + " │" + WHITE + "  [S] Site" + RED + "                                                                                  │" + RESET)
    print(RED + " └───" + RED + "──────────────────────────────────────" + WHITE + " ┌─────────┐ " + RED + "───────────────────────────────────────┘" + RESET)
    print(WHITE + "                                            │  MULV   │" + RESET)
    print(RED + " ┌───" + RED + "──────────────────────────────────────" + WHITE + " └────┬────┘ " + RED + "───────────────────────────────────────┐" + RESET)
    print(RED + " │" + RESET)
    
    print(f" {RED}├──{RESET} {RED}[01]{RESET} {WHITE}Générateur de Sessions{RESET}     {RED}├──{RESET} {RED}[10]{RESET} {WHITE}Générateur Invit Bot{RESET}       {RED}├──{RESET} {RED}[19]{RESET} {WHITE}Vérificateur Webhook{RESET}")
    print(f" {RED}├──{RESET} {RED}[02]{RESET} {WHITE}Permissions de Token{RESET}       {RED}├──{RESET} {RED}[11]{RESET} {WHITE}Nettoyeur de Salons{RESET}        {RED}├──{RESET} {RED}[20]{RESET} {WHITE}Testeur de Webhook{RESET}")
    print(f" {RED}├──{RESET} {RED}[03]{RESET} {WHITE}Analyseur de Sécurité{RESET}      {RED}├──{RESET} {RED}[12]{RESET} {WHITE}Configuration de Bot{RESET}       {RED}├──{RESET} {RED}[21]{RESET} {WHITE}Suppression Webhook{RESET}")
    print(f" {RED}├──{RESET} {RED}[04]{RESET} {WHITE}Inspecteur de Profil{RESET}       {RED}├──{RESET} {RED}[13]{RESET} {WHITE}Sauvegarde Serveur{RESET}         {RED}├──{RESET} {RED}[22]{RESET} {WHITE}Générateur Webhook{RESET}")
    print(f" {RED}├──{RESET} {RED}[05]{RESET} {WHITE}Connexion Automatique{RESET}      {RED}├──{RESET} {RED}[14]{RESET} {WHITE}Restauration Serveur{RESET}       {RED}├──{RESET} {RED}[23]{RESET} {WHITE}Générateur de Clés{RESET}")
    print(f" {RED}├──{RESET} {RED}[06]{RESET} {WHITE}Sauvegarde de Groupes{RESET}      {RED}├──{RESET} {RED}[15]{RESET} {WHITE}Inspecteur de Bot{RESET}          {RED}├──{RESET} {RED}[24]{RESET} {WHITE}Diagnostic Réseau{RESET}")
    print(f" {RED}├──{RESET} {RED}[07]{RESET} {WHITE}Restauration Groupes{RESET}       {RED}├──{RESET} {RED}[16]{RESET} {WHITE}Changer Langue Bot{RESET}         {RED}├──{RESET} {RED}[25]{RESET} {WHITE}Test Ping & Latence{RESET}")
    print(f" {RED}├──{RESET} {RED}[08]{RESET} {WHITE}Token Grabber (Sim){RESET}        {RED}├──{RESET} {RED}[17]{RESET} {WHITE}Changer Thème CLI{RESET}          {RED}├──{RESET} {RED}[26]{RESET} {WHITE}Analyseur DNS/HTTP{RESET}")
    print(f" {RED}└──{RESET} {RED}[09]{RESET} {WHITE}Exportateur d'Infos{RESET}        {RED}└──{RESET} {RED}[18]{RESET} {WHITE}Extraction de Guilde{RESET}       {RED}└──{RESET} {RED}[27]{RESET} {WHITE}Calculateur Réseau{RESET}")
    print(RED + " │" + RESET)
    print(RED + " └─────────────────────────────────────────────────────────────────────────────────────────────┘" + RESET)

def run_task(option_num, option_name):
    print(f"\n{CYAN}[*] Initialisation du module : {option_name} ({option_num})...{RESET}")
    time.sleep(0.8)
    
    target = input(f" {CYAN}[?] Saisir le Token, l'ID ou l'URL à traiter : {RESET}").strip()
    if not target:
        target = "SESSION_TOKEN_DEFAULT_77192"
        
    print(f"\n{CYAN}[*] Configuration des protocoles réseau...{RESET}")
    
    bar_width = 30
    for i in range(bar_width + 1):
        progress = (i / bar_width) * 100
        bar = "█" * i + "-" * (bar_width - i)
        sys.stdout.write(f"\r {RED}[{bar}] {progress:.0f}% - Traitement en cours...{RESET}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.05))
    print()
    
    print(f"\n{GREEN}[+] Connexion établie avec succès.{RESET}")
    for _ in range(3):
        time.sleep(0.2)
        log_id = "".join(random.choice(string.hexdigits) for _ in range(8))
        print(f"  {RED}[SÉCURISÉ]{RESET} Tâche exécutée sur le nœud 0x{log_id.upper()}")
        
    time.sleep(0.4)
    print(f"\n{GREEN}[✓] Terminé ! L'opération '{option_name}' s'est déroulée avec succès.{RESET}")
    input(f"\n{WHITE}Appuie sur Entrée pour revenir au menu principal...{RESET}")

def menu():
    while True:
        draw_banner()
        choice = input(f" {RED}┌──({WHITE}cacap@mulv{RED})-[{WHITE}~/Windows/Menu-3{RED}]\n └─{WHITE}$ {RESET}").strip().lower()

        formatted_choice = choice.zfill(2) if choice.isdigit() else choice

        if formatted_choice == "01":
            print()
            try:
                count_input = input(f" {CYAN}[?] Nombre de clés de session uniques à générer : {RESET}").strip()
                count = int(count_input) if count_input else 10
                if count <= 0: raise ValueError
            except ValueError:
                print(f"\n{RED}[x] Erreur : Saisissez un nombre entier valide supérieur à 0.{RESET}")
                time.sleep(2)
                continue
                
            print(f"\n{CYAN}[*] Génération en cours de {count} clés de session uniques...{RESET}")
            time.sleep(1)
            for i in range(1, count + 1):
                token = generate_session_token()
                print(f"  {GREEN}[+] Clé #{i:02d} : {RESET}{token}")
                if count <= 50:
                    time.sleep(0.03)
            print(f"\n{GREEN}[✓] Processus de génération terminé avec succès.{RESET}")
            input(f"\n{WHITE}Appuie sur Entrée pour continuer...{RESET}")
            
        elif formatted_choice == "08":
            print()
            user_id = input(f" {CYAN}[?] Saisir l'ID utilisateur de la cible : {RESET}").strip()
            if not user_id.isdigit():
                print(f"\n{RED}[x] Erreur : L'ID doit être composé uniquement de chiffres.{RESET}")
                time.sleep(2)
                continue
                
            print(f"\n{CYAN}[*] Initialisation du pont de communication...{RESET}")
            time.sleep(0.8)
            print(f"{CYAN}[*] Recherche de la correspondance réseau pour l'ID {user_id}...{RESET}")
            
            bar_width = 30
            for i in range(bar_width + 1):
                progress = (i / bar_width) * 100
                bar = "█" * i + "-" * (bar_width - i)
                sys.stdout.write(f"\r {RED}[{bar}] {progress:.0f}% - Liaison au serveur...{RESET}")
                sys.stdout.flush()
                time.sleep(0.05)
            print()
            
            fake_token = generate_fake_grabbed_token(user_id)
            print(f"\n{GREEN}[✓] Récupération réussie !{RESET}")
            print(f"  {GREEN}[+] Token détecté :{RESET} {fake_token}")
            input(f"\n{WHITE}Appuie sur Entrée pour continuer...{RESET}")

        elif formatted_choice == "24":
            print()
            target_ip = input(f" {CYAN}[?] Entrer le domaine ou l'adresse IP à analyser : {RESET}").strip()
            if not target_ip:
                target_ip = "mulv.net"
            run_network_lookup(target_ip)
            input(f"\n{WHITE}Appuie sur Entrée pour continuer...{RESET}")
            
        elif formatted_choice in OPTIONS:
            run_task(formatted_choice, OPTIONS[formatted_choice])
            
        elif choice == "i":
            print(f"\n{CYAN}[i] Informations du Système :")
            print(f"  MULV Administration Console v6.6")
            print(f"  Outil d'administration réseau et de gestion d'API.")
            print(f"  Développé sous environnement Python CLI.")
            input(f"\n{WHITE}Appuie sur Entrée pour revenir au menu...{RESET}")
            
        elif choice == "b" or choice == "0" or choice == "exit":
            print(f"\n{RED}[!] Arrêt du système de contrôle...{RESET}")
            time.sleep(1)
            sys.exit()
            
        else:
            print(f"\n{RED}[x] Option non valide ou module manquant !{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    os.system('') 
    menu()
