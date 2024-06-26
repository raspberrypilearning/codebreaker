##!/bin/python3
from pygal import Bar
from frequency import anglais, francais, espagnol

# Mise en place des structures de données
alphabet = list(' abcdefghijklmnopqrstuvwxyz ')  # Liste à partir d'une chaîne de caractères
code = {}

# Créer le code atbash en inversant l'alphabet
def creer_code():
    inverses = list(reversed(alphabet))  # Inverse une liste

    for i in range(len(alphabet)):  # Obtenir la longueur d'une liste
        # Remplir le dictionnaire de codes avec une lettre de l'alphabet et sa lettre codée
        code[alphabet[i]] = inverses[i]

    # print(code)

# Calculer la fréquence de toutes les lettres d'un texte
def frequence(texte):
    texte = list(texte.lower())  # Mettre le message en minuscules et en faire une liste

    freq = {} # Créer un dictionnaire pour chaque lettre, avec un compte de 0
    for lettre in alphabet:
        freq[lettre] = 0

    total_lettres = len(texte)  # Compter les lettres du message

    for lettre in texte:
        if lettre in freq:
            freq[lettre] += 1

    for lettre in freq:  # Convertir les comptages en pourcentages
        freq[lettre] = freq[lettre] / total_lettres * 100

    return freq

# Faire un diagramme de fréquence
def faire_graphique(texte, langue):
    graphique = Bar(width=800, title='Analyse fréquentielle',
                x_labels=list(texte.keys()))
    # Première utilisation explicite des valeurs
    graphique.add('Message cible', list(texte.values()))
    graphique.add('Langue', list(langue.values()))

    graphique.render()


# Coder/décoder un morceau de texte - atbash est symétrique
def atbash(texte):
    texte = texte.lower()  #  Convertit le texte en minuscules
    sortie = ''

    for lettre in texte:
        if lettre in code:
            # Remplit la sortie avec le message codé/décodé en utilisant le dictionnaire
            sortie += code[lettre]

    return sortie  # Retourner le message codé/décodé


# Récupérer et renvoyer le texte d'un fichier
def obtenir_texte(filename):
    with open(filename) as f:
        texte = f.read().replace('\n', '')  # Nécessité de supprimer les caractères de retour à la ligne

    return texte

# Créer un système de menu basé sur du texte
def menu():
    choix = ''  # Commence par une mauvaise réponse pour le choix.

    while choix != 'c' and choix != 'f' and choix != 'm':  # Continuer à demander à l'utilisateur la bonne réponse
        choix = input(
            'Saisis c pour coder/décoder un fichier texte, f pour effectuer une analyse fréquentielle en trois langues, ou m pour saisir ton propre message à coder :')

    if choix == 'c':
        print('Nous passons ton message dans le cryptogramme…')
        message = obtenir_texte('longer.txt')  # Prendre l'entrée d'un fichier
        code = atbash(message)
        print(code)

    elif choix == 'f':
        print('Analyse du message…')
        # Prend l'entrée du même fichier. Nous disposons d'un fichier 'longer.txt' ou d'un fichier similaire contenant un texte crypté dont nous savons qu'il se prête assez bien à l'analyse fréquentielle
        message = obtenir_texte('longer.txt')
        # Obtenir la fréquence des lettres dans le message, en %.
        message_freq = frequence(message)
        # print(message_freq)
        langue = input(
            'Dans quelle langue ton message est-il rédigé ? \n1. Anglais \n2. Français \n3. Espagnol')

        if langue == '1':
            lang_freq = anglais  # Importation du dictionnaire de fréquence anglais
        elif langue == '2':
            lang_freq = francais
        elif langue == '3':
            lang_freq = espagnol

        # Appeler la fonction pour faire un graphique
        faire_graphique(message_freq, lang_freq)

    elif choix == 'm':
        message = input('Quel texte veux-tu coder ?')
        code = atbash(message)
        print(code)

# Démarrage
def main():
    creer_code()
    menu()


main()
