
--- question ---

---
legend: Vraag 3 van 3
---

Er is een regel code nodig om een **staafdiagram** te maken met behulp van `pygal`. De code moet de x-aslabels selecteren uit de **sleutels** die worden gebruikt in de `tekst` **dictionary**. Welke coderegel kan hiervoor worden gebruikt?

--- choices ---

- ( )

chart.x_labels = keys()

  --- feedback ---

Niet helemaal, Python moet weten uit **welke** dictionary hij de sleutels moet selecteren.

  --- /feedback ---

- ( )

chart.x_labels = list(tekst)

  --- feedback ---

  Niet precies, Python moet weten welk deel van de dictionary het moet gebruiken om als labels weer te geven.

  --- /feedback ---

- ( )

chart.x_labels = list(sleutels.tekst())

  --- feedback ---

  Bijna bevat deze coderegel de juiste onderdelen, maar ze staan niet in de juiste volgorde.

  --- /feedback ---

- (x)

chart.x_labels = list(tekst.sleutels())

  --- feedback ---

Juist! Deze coderegel voegt de x-aslabels toe op basis van de **sleutels** in de `tekst` dictionary.

  --- /feedback ---

--- /choices ---

--- /question ---
