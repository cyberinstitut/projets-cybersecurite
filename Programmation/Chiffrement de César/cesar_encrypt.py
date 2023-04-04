shift = 3 # valeur de décalage

text = "CYBERINSTITUT"

encryption = ""

for c in text:

    # vérifie si caractère = lettre majuscule
    if c.isupper():

        # trouve la position entre 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # effectuer le décalage (modulo)
        new_index = (c_index + shift) % 26

        # nouvelle conversion
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # ajouter à la chaîne chiffrée
        encryption = encryption + new_character

    else:

        # si caractère n'est pas en MAJ alors laissez tel quel
        encryption += c
        
print("Texte en clair :",text)

print("Texte chiffré :",encryption)
