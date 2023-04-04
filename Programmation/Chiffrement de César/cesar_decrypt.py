shift = 3 # valeur de décalage

encryption = "FBEHULQVWLWXW"

text = ""

for c in encryption :

    # vérifie si le caractère = lettre majuscule
    if c.isupper() :

        # trouver la position en 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # effectuer le décalage (modulo)
        new_index = (c_index - shift) % 26

        # nouvelle conversion
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # ajouter à la chaîne en claire
        text = text + new_character

    else:

        # si caractère n'est pas en MAJ alors laissez tel quel
        text += c

print("Texte chiffré :",encryption)

print("Texte en clair :",text)
