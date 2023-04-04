from pynput import keyboard #Importation de la classe keyboard de la bibliothèque pynput

def on_press(key): #Définition de la fonction on_press(key) qui affiche la touche appuyée
    try:
        print(f'Key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

with keyboard.Listener(on_press=on_press) as listener: #Création d'un objet Listener pour détecter les touches du clavier et les traiter avec la fonction on_press
    listener.join() #Utilisation de listener.join() pour attendre indéfiniment que l'utilisateur appuie sur les touches