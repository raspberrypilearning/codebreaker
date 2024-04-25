
--- question ---

---
legend: Vraag 3 van 3
---

Er is een regel code nodig om een **staafdiagram** te maken met behulp van `pygal`. De code moet de x-aslabels selecteren uit de **keys** die worden gebruikt in de `tekst` **dictionary**. Welke coderegel kan hiervoor worden gebruikt?

--- choices ---

- ( )

grafiek.x_labels = keys()

  --- feedback ---

Niet helemaal, Python moet weten uit **welke** dictionary hij de sleutels moet selecteren.

  --- /feedback ---

- ( )

grafiek.x_labels = list(tekst)

  --- feedback ---

  Niet precies, Python moet weten welk deel van de dictionary het moet gebruiken om als labels weer te geven.

  --- /feedback ---

- ( )

grafiek.x_labels = list(keys.tekst())

  --- feedback ---

  Bijna bevat deze coderegel de juiste onderdelen, maar ze staan niet in de juiste volgorde.

  --- /feedback ---

- (x)

grafiek.x_labels = list(tekst.keys())

  --- feedback ---

Juist! Deze coderegel voegt de x-aslabels toe op basis van de **keys** in de `tekst` dictionary.

  --- /feedback ---

--- /choices ---

--- /question ---
