##!/bin/python3
from pygal import Bar
from frequency import engels, frans, nederlands

# Datastructuren opzetten
alfabet = list(' abcdefghijklmnopqrstuvwxyz ') # Lijst uit een string
code = {}

# Maak de atbash-code door het alfabet om te draaien
def maak_code():
    andersom = list(reversed(alfabet)) # Draait een lijst om

    for i in range(len(alfabet)): # Haalt de lengte van een lijst op
        # Vul de code dictionary in met een letter van het alfabet en de bijbehorende gecodeerde letter
        code[alfabet[i]] = andersom[i]

    # print(code)

# Bereken de frequentie van alle letters in een stuk tekst
def frequentie(tekst):
    tekst = list(tekst.lower()) # Zet het bericht om in kleine letters en maak er een lijst van

    freq = {} # Maak een dictionary van elke letter, met een telling van 0
    for letter in alfabet:
        freq[letter] = 0

    totaal_letters = len(tekst) #Tel de letters in het bericht

    for letter in tekst:
        if letter in freq:
            freq[letter] += 1

    for letter in freq: # Converteren van tellingen naar percentages
        freq[letter] = freq[letter] / totaal_letters * 100

    return freq

# Frequentiegrafiek maken
def maak_grafiek(tekst, taal):
    grafiek = Bar(width=800, title='Frequentie analyse',
                x_labels=list(tekst.keys()))
    # Eerste expliciete gebruik van waarden
    grafiek.add('Doel bericht', list(tekst.values()))
    grafiek.add('Taal', list(taal.values()))

    grafiek.render()


# Codeer/decodeer een stuk tekst — atbash is symmetrisch
def atbash(tekst):
    tekst = tekst.lower() # Converteert tekst naar kleine letters
    uitvoer = ''

    for letter in tekst:
        if letter in code:
            # Vult de uitvoer in met het gecodeerde/gedecodeerde bericht met behulp van de dictionary
            uitvoer += code[letter]

    return uitvoer # Retourneert het gecodeerde/gedecodeerde bericht


# Tekst uit een bestand ophalen en retourneren
def ophalen_tekst(bestandsnaam):
    with open(bestandsnaam) as f:
        tekst = f.read().replace('\n', '') # De tekens voor de nieuwe regel moeten worden verwijderd

    return tekst

# Maak een tekst-gebaseerd menu systeem
def menu():
    keuze = '' # Begin met een verkeerd antwoord voor keuze.

    while keuze != 'c' and keuze != 'f' and keuze != 'm': # Blijf aan de gebruiker het juiste antwoord vragen
        keuze = input(
            'Voer c in om een tekst bestand te coderen/decoderen, f om frequentie analyse uit te voeren in drie talen, of m om je eigen bericht in te voeren om:')

    if keuze == 'c':
        print('Je bericht door de code halen…')
        bericht = ophalen_tekst('longer.txt') # Neem input van een bestand
        code = atbash(bericht)
        print(code)

    elif keuze == 'f':
        print('Bericht analyseren…')
        # Neem invoer uit hetzelfde bestand. We hebben een 'longer.txt' met een tekst waarvan we weten dat deze redelijk goed presteert voor frequentieanalyse
        bericht = ophalen_tekst('longer.txt')
        # Haal de frequentie van de letters in het bericht op, als %
        bericht_freq = frequentie(bericht)
        # print(bericht_freq)
        taal = input(
            'In welke taal is jouw bericht? \n1. Engels \n2. Frans \n3. Nederlands')

        if taal == '1':
            taal_freq = engels # Importeer het Engelse frequentiewoordenboek
        elif taal == '2':
            taal_freq = frans
        elif taal == '3':
            taal_freq = nederlands

        # Roep de functie aan om een grafiek te maken
        maak_grafiek(bericht_freq, taal_freq)

    elif keuze == 'm':
        bericht = input('Welke tekst wil je coderen?')
        code = atbash(bericht)
        print(code)

# Opstart
def main():
    maak_code()
    menu()


main()
