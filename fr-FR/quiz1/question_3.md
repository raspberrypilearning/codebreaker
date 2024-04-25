
--- question ---

---
legend: Question 3 sur 3
---

Une ligne de code est nécessaire pour créer un **histogramme** en utilisant `pygal`. Le code doit sélectionner les étiquettes de l'axe des x à partir des **clés** utilisées dans le `texte` **dictionnaire**. Quelle ligne de code peut être utilisée à cet effet ?

--- choices ---

- ( )

graphique.x_labels = keys()

  --- feedback ---

Pas tout à fait, Python a besoin de savoir **de quel** dictionnaire sélectionner les clés.

  --- /feedback ---

- ( )

graphique.x_labels = list(texte)

  --- feedback ---

  Pas exactement, Python a besoin de savoir quelle partie du dictionnaire il doit utiliser pour afficher les étiquettes.

  --- /feedback ---

- ( )

graphique.x_labels = list(keys.texte())

  --- feedback ---

  Presque, cette ligne de code contient les bonnes parties mais elles ne sont pas dans le bon ordre.

  --- /feedback ---

- (x)

graphique.x_labels = list(texte.keys())

  --- feedback ---

Correct ! Cette ligne de code ajoute les étiquettes de l'axe des x en fonction des **clés** contenues dans le dictionnaire `texte`.

  --- /feedback ---

--- /choices ---

--- /question ---
