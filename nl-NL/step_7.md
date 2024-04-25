## Analyseer de frequentie

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Gebruik een staafdiagram om de frequentie van letters in een gecodeerd bericht te analyseren. 
</div>
<div>
![Een staafdiagram dat de frequentie van letters in de Nederlandse taal laat zien, vergeleken met de frequentie van letters die in het gecodeerde bericht worden gebruikt.](images/frequency-analysis.PNG){:width="400px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
In alle talen heeft elke letter in het alfabet een 'persoonlijkheid' of een reeks eigenschappen wanneer deze in die taal wordt gebruikt. Een van de meest voor de hand liggende kenmerken van een letter, in welke taal dan ook, is hoe vaak hij voorkomt. **Frequentieanalyse** is de methode om codes te ontcijferen door te kijken hoe vaak letters worden gebruikt in de taal van de code, en dat te vergelijken met hoe vaak gecodeerde letters in een bericht voorkomen. In het Nederlands is de letter **e** de meest gebruikte letter (deze verschijnt 18,91% van de tijd), gevolgd door **n** (met 10,03%). De minst gebruikte letter is **q**.
</p>
--- task ---

De coderegel `print(bericht_freq)` is niet langer nodig. Voeg een `#` toe aan het begin ervan, zodat Python dit negeert wanneer de code wordt uitgevoerd.

--- code ---
---
language: python
filename: main.py - menu()
line_numbers: true
line_number_start: 72
line_highlights: 76
---
    elif keuze == 'f':
        print('Bericht analyseren…')
        bericht = ophalen_tekst('input.txt')  # Neem invoer uit hetzelfde bestand. We hebben een 'longer.txt' of iets dergelijks met cijfertekst waarvan we weten dat deze redelijk goed presteert voor frequentieanalyse
        bericht_freq = frequentie(bericht)  # Haal de frequentie van de letters in het bericht op, als %
        # print(bericht_freq)
--- /code ---

--- /task ---

### Maak de frequentie grafiek functie

--- task ---

Zoek de `# Maak frequentie grafiek` opmerking en maak een nieuwe functie genaamd `maak_grafiek()`. Deze functie heeft twee parameters nodig, genaamd `tekst` en `taal`. Het frequentiediagram zal een **staaf** diagram zijn met de **titel** `Frequentie analyse` en met **x-as** labels met behulp van de **sleutels** uit de `freq` dictionary.

De `freq` dictionary waarden worden doorgegeven aan de functie wanneer deze later in de code wordt aangeroepen, via de `tekst` parameter.

--- code ---
---
language: python
filename: main.py - make_chart()
line_numbers: true
line_number_start: 36
line_highlights: 37-38
---
# Frequentiegrafiek maken
def maak_grafiek(tekst, taal):
    grafiek = Bar(width=800, height=400, title='Frequentie analyse', x_labels = list(tekst.keys()))
--- /code ---

--- /task ---

--- task ---

Label de grafiek met de **frequentie** van letters in het gecodeerde bericht en de letterfrequentie van de **taal** van het bericht. Deze gegevens zijn **aan** de **functie** doorgegeven via de `tekst` en `taal` parameters.

--- code ---
---
language: python
filename: main.py - make_chart()
line_numbers: true
line_number_start: 36
line_highlights: 39-40
---
# Frequentiegrafiek maken
def maak_grafiek(tekst, taal):
    grafiek = Bar(width=800, height=400, title='Frequentie analyse', x_labels = list(tekst.keys()))
    grafiek.add('Doelbericht', list(tekst.values()))  # Label de frequentiegegevens voor het gecodeerde bericht
    grafiek.add('Taal', list(taal.values()))  # Label de frequentiegegevens voor de taal
--- /code ---

--- /task ---

--- task ---

**Geef** de grafiek zo weer dat deze wordt getoond wanneer de functie wordt aangeroepen.

--- code ---
---
language: python
filename: main.py - make_chart()
line_numbers: true
line_number_start: 36
line_highlights: 42
---
# Frequentiegrafiek maken
def maak_grafiek(tekst, taal):
    grafiek = Bar(width=800, height=400, title='Frequentie analyse', x_labels = list(tekst.keys()))
    grafiek.add('Doelbericht', list(tekst.values()))  # Label de frequentiegegevens voor het gecodeerde bericht
    grafiek.add('Taal', list(taal.values()))  # Label de frequentiegegevens voor de taal

    grafiek.render()
--- /code ---

--- /task ---

### Roep de frequentie grafiek functie aan

--- task ---

Vind je `elif` in de `menu()` functie. Voeg een regel code toe die het **Nederlandse** frequentiewoordenboek `importeert` uit het `frequency.py` bestand. Voeg nog een regel code toe die de functie `maak_grafiek` **aanroept** om het diagram te tekenen.

--- code ---
---
language: python
filename: main.py - menu()
line_numbers: true
line_number_start: 75
line_highlights: 80-81
---

    elif keuze == 'f':
        print('Bericht analyseren…')
        bericht = ophalen_tekst('input.txt')  # Neem invoer uit hetzelfde bestand. We hebben een 'longer.txt' of iets dergelijks met cijfertekst waarvan we weten dat deze redelijk goed presteert voor frequentieanalyse
        bericht_freq = frequentie(bericht)  # Haal de frequentie van de letters in het bericht op, als %
        # print(bericht_freq)
        taal_freq = english  # Het Engelse frequentiewoordenboek importeren
        make_chart(bericht_freq, taal_freq)  # Roep de functie aan om een grafiek te maken
--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om de frequentie analyse staafdiagram weer te geven.

![Een staafdiagram dat de frequentie van letters in de Nederlandse taal weergeeft, vergeleken met de frequentie van letters die in het gecodeerde bericht worden gebruikt.](images/frequency-analysis.PNG)

**Foutopsporing:** je grafiek ziet er niet precies hetzelfde uit als de grafiek die wordt weergegeven in de afbeelding hierboven:
- Dat is normaal. Je grafiek toont de frequentie gegevens voor het geheime bericht dat je hebt ingevoerd in `input.txt`.

**Fouten opsporen:** Je ziet het volgende foutbericht `NameError: naam 'taal_freq' is not defined`:
- Controleer of je de regel code `taal_freq = nederlands` hebt toegevoegd **voor** het aanroepen van de functie `maak_grafiek()`.

**Foutopsporing:** Je ziet een `indentation error` (inspring fout) bericht:
- Controleer of je al je nieuwe code correct hebt ingesprongen. Bekijk de bovenstaande taken nogmaals om dit te controleren.

--- /task ---

### Analyseer de frequentie grafiek

Het diagram dat is gemaakt toont de frequentie van letters in de Nederlandse taal, aangeduid als **Taal**. Je kunt zien dat de letter **e** de meest gebruikte letter in de Nederlandse taal is, omdat deze de hoogste balk heeft voor alle **taal** waarden.

In de frequentiekaart staat ook de frequentie van letters in je **gecodeerde** bericht, gelabeld als **doel bericht**. Hieronder vallen ook de spaties in je bericht, die te zien zijn in de laatste balk aan de rechterkant. Om uit te zoeken wat **codering** is gebruikt voor dit bericht, kun je de balken van het gecodeerde bericht vergelijken met de Nederlandse taal. De hoogste balk (waarbij je de spaties niet meerekent) in de gecodeerde berichttekst zal hoogstwaarschijnlijk een **e** zijn. De op één na hoogste letter zal hoogstwaarschijnlijk een **n** zijn, aangezien dit de volgende meest populaire letter is.

Codekrakers kunnen de frequentie van letters gebruiken om het type codering te achterhalen dat voor het bericht is gebruikt. Ze kunnen met vallen en opstaan **voorspellen** wat een letter zou kunnen vertegenwoordigen, waarbij ze het diagram als leidraad gebruiken.

--- task ---

Je geheime bericht is vrij klein, waardoor het lastig wordt om het te analyseren met behulp van een frequentiegrafiek. Wijzig je code zodat in plaats daarvan het bericht analyseert in `longer.txt`.

Wijzig `input.txt` in `longer.txt`.

--- code ---
---
language: python
filename: main.py - menu()
line_numbers: true
line_number_start: 75
line_highlights: 77
---
    elif keuze == 'f':
        print('Bericht analyseren…')
        bericht = ophalen_tekst('longer.txt') 
        bericht_freq = frequentie(bericht)  # Haal de frequentie van de letters in het bericht op, als %
--- /code ---

--- /task ---

--- task ---

**Analyseer** het frequentiediagram door te kijken naar de **Taal** waarden en de **Doel bericht** waarden. Merk op hoe de hoogste balk voor **taal** **e** en de hoogste balk voor **Doelbericht** **v** is. Dit komt omdat met de **Atbash** code, de letter **e** gecodeerd is met de letter **v**.

![Een staafdiagram dat de frequentie van letters in de Nederlandse taal weergeeft, vergeleken met de frequentie van letters die in het gecodeerde bericht in longer.txt worden gebruikt.](images/longer-analysis.PNG)

--- /task ---

--- save ---
