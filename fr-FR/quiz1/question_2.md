
--- question ---

---
legend: Question 2 sur 3
---

Une boucle `for` est créée pour afficher les lettres dans un mot.

```python
mot = "bonjour"

for lettre in mot:
    print(lettre)
```

Quelle sera la sortie de ce code quand il sera exécuté ?

--- choices ---

- (x)

```
b
o
n
j
o
u
r
```

  --- feedback ---

  Correct ! Chaque lettre du mot `bonjour` sera affichée sur une nouvelle ligne.

  --- /feedback ---

- ( )
```
m
o
t
```
  --- feedback ---

  Pas tout à fait, `print(lettre)` affichera ce qui est **contenu** par la variable `lettre` à ce stade de la boucle `for`.

  --- /feedback ---

- ( )

```
bonjour
bonjour
bonjour
bonjour
bonjour
```

  --- feedback ---

  Pas exactement, le code affichera chaque lettre en `bonjour`. Il n'imprimera pas le mot entier à chaque fois.

  --- /feedback ---

--- /choices ---

--- /question ---
