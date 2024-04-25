## Codeer een bericht

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In deze stap maak je een functie waarmee je je tekst kunt omdraaien en omkeren met je atbash-coderingslijst, en deze als een gecodeerd bericht kunt terugsturen. 
</div>
<div>
![De uitvoer van de code die in deze stap is gemaakt. Er wordt een gecodeerde versie van een geheim bericht weergegeven.](images/test-encoded.PNG){:width="300px"}
</div>
</div>

--- task ---

Maak een **commentaar** van de afdrukverklaring die wordt gebruikt om te testen op lijn 17 door een hashtag aan het begin van de regel te plaatsen:

--- code ---
---
language: python
filename: main.py - create_code()
line_numbers: true
line_number_start: 14
line_highlights: 17
---
    for i in range(len(alfabet)):  # Haalt de lengte van een lijst op
        code[alfabet[i]] = andersom[i]  # Vul het code-woordenboek in met een letter van het alfabet en de bijbehorende gecodeerde letter

# print(code)
--- /code ---

--- /task ---

### Stel je atbash functie in

Je voegt nu je nieuwe **functie** toe die wat tekst codeert met behulp van de **atbash** cypher.

--- task ---

Zoek de opmerking met de tekst `# Codeer/decodeer een stuk tekst — atbash is symmetrisch`. Definieer onder de opmerking een functie met de naam `atbash`, met de **parameter** `tekst`. Met parameters kun je waardes doorgeven aan functies die binnen die functie gebruikt kunnen worden.

--- code ---
---
language: python
filename: main.py - atbash()
line_numbers: true
line_number_start: 26
line_highlights: 27
---
# Codeer/decodeer een stuk tekst — atbash is symmetrisch
def atbash(tekst):

--- /code ---

Druk op <kbd>Enter</kbd>. Je zou de volgende regel ingesprongen moeten zien.

--- /task ---

[[[parameters]]]

### Tekst omzetten naar kleine letters

Eerst moet je functie de `tekst` omzetten naar kleine letters. Een nieuwe **variabele** met de naam `uitvoer` moet dan worden aangemaakt om het gecodeerde bericht op te slaan.

--- task ---

Onder de coderegel waar je de functie `atbash()` hebt gedefinieerd, typ je:

--- code ---
---
language: python
filename: main.py - atbash()
line_numbers: true
line_number_start: 26
line_highlights: 28-29
---
# Codeer/decodeer een stuk tekst — atbash is symmetrisch
def atbash(tekst):
    tekst = tekst.lower()  # Zet tekst om naar kleine letters
    uitvoer = ''

--- /code ---

--- /task ---

### Codeer je tekst

Het volgende deel van je code **codeert** de `tekst` die **doorgegeven** is in de functie. Een `for` lus wordt gebruikt om elke letter in de `tekst` te bekijken en deze om te zetten naar een gecodeerde letter met behulp van de `code` dictionary. Ten slotte zal het het gecodeerde bericht **retourneren**.

--- task ---

Laat een lege regel open onder de laatste code die je hebt ingevoerd (zorg ervoor dat je de inspringing behoudt) en typ vervolgens:

--- code ---
---
language: python
filename: main.py - atbash()
line_numbers: true
line_number_start: 26
line_highlights: 31-35
---
# Codeer/decodeer een stuk tekst — atbash is symmetrisch
def atbash(tekst):
    tekst = tekst.lower()  # Zet tekst om naar kleine letters
    uitvoer = ''

    for letter in tekst: 
        if letter in code: 
            uitvoer += code[letter]  # Vult de uitvoer in met het gecodeerde/gedecodeerde bericht met behulp van het woordenboek
    
    return uitvoer  # Retourneer het gecodeerde/gedecodeerde bericht

--- /code ---

--- /task ---

### Testen en fouten opsporen

--- task ---

Nu je een **functie** hebt die **tekst**codeert, moet je deze uitvoeren om te controleren of deze werkt. Zoek de functie `main()` en voeg een functieaanroep toe om de functie `atbash()` uit te voeren.

De tekenreeks 'Test' wordt **doorgegeven** aan de functie, zodat deze kan worden gecodeerd.

--- code ---
---
language: python
filename: main.py - main()
line_numbers: true
line_number_start: 45
line_highlights: 48
---
# Start up
def main():
    maak_code()
    print(atbash('Test'))

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om te zien of het testbericht correct wordt weergegeven. Je zou de console-uitvoer `gvhg`moeten zien.

![De uitvoer van de gecodeerde tekst die in deze stap wordt gemaakt.](images/test-encoded.PNG){:width="200px"}

**Fouten opsporen:** Als je een bericht ziet over een inspringfout:
- Controleer of je al je code correct hebt ingesprongen
- Kijk terug naar de voorbeeldcode op deze pagina om je te helpen het controleren

--- /task ---

--- task ---

Maak een **comment** van je `print(atbash('Test'))` regel code nu je klaar bent met testen.

--- code ---
---
language: python
filename: main.py - main()
line_numbers: true
line_number_start: 45
line_highlights: 48
---
# Start up
def main():
    maak_code()
    # print(atbash('Test'))

--- /code ---

--- /task ---

In de volgende stap zul je **een bericht** coderen met behulp van je `code` dictionary.

--- save ---
