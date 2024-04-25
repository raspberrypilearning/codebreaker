#!/bin/python3
from pygal import Bar
from frequency import francais

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
    # Convertir le message en minuscules et en faire une liste
    texte = list(texte.lower())

    freq = {} # Créer un dictionnaire pour chaque lettre, avec un compte de 0
    for lettre in alphabet:
        freq[lettre] = 0

    total_lettres = len(texte)  # Compter les lettres du message

    for lettre in texte:
        if lettre in freq:
            freq[lettre] += 1

    for lettre in freq:
        freq[lettre] = freq[lettre] / total_lettres * \
            100 # Convertir les comptages en pourcentages

    return freq

# Faire un diagramme de fréquence
def faire_graphique(texte, langue):
    graphique = Bar(width=800, height=400, title='Analyse fréquentielle',
                x_labels=list(texte.keys()))
    # Étiqueter les données de fréquence pour le message codé
    graphique.add('Message cible', list(texte.values()))
    # Étiqueter les données de fréquence pour la langue
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

    while choix != 'c' and choix != 'f':  # Continuer à demander à l'utilisateur la bonne réponse
        choix = input(
            'Saisis c pour coder/décoder du texte, ou f pour effectuer une analyse fréquentielle : ')

    if choix == 'c':
        print('Nous passons ton message dans le cryptogramme…')
        message = obtenir_texte('longer.txt')  # Prendre l'entrée d'un fichier
        code = atbash(message)
        print(code)

    elif choix == 'f':
        print('Analyse du message…')
        message = obtenir_texte('longer.txt')
        message_freq = frequence(message)
        # print(message_freq)
        lang_freq = francais  # Importation du dictionnaire de fréquence français
        # Appeler la fonction pour faire un graphique
        faire_graphique(message_freq, lang_freq)

# Démarrage
def main():
    creer_code()
    # print(atbash('Test'))
    menu()


main()
