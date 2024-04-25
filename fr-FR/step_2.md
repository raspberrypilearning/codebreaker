## Coder l'alphabet

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Pour commencer, tu vas créer un dictionnaire pour tes lettres codées. 
</div>
<div>
![La sortie du dictionnaire de codes créé à cette étape.](images/code-dictionary.PNG){:width="600px"}
</div>
</div>

--- task ---

Ouvre le [projet de démarrage Déchiffreur de code](https://editor.raspberrypi.org/en/projects/codebreaker-project-starter){:target="_blank"}. Le Code Editor Raspberry Pi s'ouvre dans un autre onglet du navigateur.

Si tu as un compte Raspberry Pi, tu peux cliquer sur **Save** pour enregistrer une copie du code de démarrage dans ta bibliothèque.

Si tu n'utilises pas le Code Editor dans ton navigateur, tu devras télécharger les fichiers du projet et tu devras peut-être installer `pygal` avant de pouvoir l'importer.

--- collapse ---
---
title: Installer pygal
---

### Sur Windows
Dans **l'invite de commande**, tape ce qui suit et appuie sur la touche <kbd>Entrée</kbd> :

```
pip install pygal
```

Attends que l'installation se termine, puis poursuis le projet.

### Sur Mac
Dans le **Terminal**, tape ce qui suit et appuie sur la touche <kbd>Entrée</kbd> :

```
pip3 install pygal
```

Attends que l'installation se termine, puis poursuis le projet.

### Sur Linux, y compris Raspberry Pi OS
Dans le **Terminal**, tape ce qui suit et appuie sur la touche <kbd>Entrée</kbd> :

```
pip install pygal
```

Attends que l'installation se termine, puis poursuis le projet.

--- /collapse ---

--- /task ---

### Définir la liste alphabétique et le dictionnaire des codes

Le programme Déchiffreur de code commence par deux structures de données. La première structure de données est une **liste** de toutes les lettres de l'alphabet et la seconde est un `code` **dictionnaire**. Pour gagner du temps de saisie, tu peux créer une liste à partir d'une chaîne en utilisant la fonction `list()`.

[[[list-function]]]

--- task ---

Trouve le commentaire `# Configurer les structures de données` du programme, puis utilise la fonction `list()` pour créer une **liste** de lettres à partir de l'`alphabet`. Ensuite, **initialise** le `code` **dictionnaire** afin que tu puisses le remplir dans une étape ultérieure.

La liste `alphabet` contient des espaces au début et à la fin pour préserver les espaces dans le message. Un cryptage fort n'aurait pas cet effet, car il rend le message plus facile à décoder. Les espaces ont été conservés pour ce projet afin de faciliter la lecture des messages.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 5
line_highlights: 6-7
---
# Mise en place des structures de données
alphabet = list(' abcdefghijklmnopqrstuvwxyz ')  # List from a string code = {}

--- /code ---

--- /task ---

### Créer une nouvelle liste qui inverse l'alphabet

Tu dois créer une nouvelle liste qui contient l'alphabet, mais à l'envers. Tu peux à nouveau utiliser la fonction `list()` pour t'aider dans cette tâche. Tu peux aussi utiliser la fonction `reversed()` pour inverser une liste existante.

--- task ---

Trouve le commentaire `# Crée le code atbash en inversant l'alphabet` puis **définis** une nouvelle fonction appelée `creer_code`. Ensuite, crée une **liste** qui contient l'**inverse** de la liste `alphabet`.

--- code ---
---
language: python filename: main.py - create_code() line_numbers: true line_number_start: 10
line_highlights: 11-12
---
# Créer le code atbash en inversant l'alphabet
def create_code(): backwards = list(reversed(alphabet))  # Reverses a list

--- /code ---

--- /task ---

### Coder l'alphabet

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Le codage consiste à convertir des données d'une forme à une autre. Dans un cryptogramme atbash par exemple, la lettre "e" serait **codée** comme un "v". 
</p>

Tu as maintenant deux listes. L'une contient l'alphabet écrit à l'endroit, l'autre l'alphabet à l'envers. Tu vas maintenant utiliser ces deux listes pour remplir un dictionnaire. La **clé** mémorise l'alphabet écrit à l'endroit et la **valeur appariée** mémorise l'alphabet à l'envers.

Le dictionnaire de codes est vraiment important car tu peux l'utiliser pour faire correspondre chaque lettre de ton message à l'aide de la **clé**, avec sa **valeur appariée** codée.

--- task ---

Dans ta fonction `creer_code`, **remplis** le dictionnaire `code` avec les données des deux **listes**. Utilise une boucle `for` pour obtenir la longueur de la liste `alphabet` et remplir le **dictionnaire** avec les données.

`len()` est une fonction que tu peux utiliser pour connaître la longueur d'un **objet**, comme une liste. Elle est utilisée ici pour itérer une boucle `for`, autant de fois qu'il y a de caractères dans la liste `alphabet` - sa longueur.

--- code ---
---
language: python filename: main.py - create_code() line_numbers: true line_number_start: 11
line_highlights: 14-15
---
def create_code(): backwards = list(reversed(alphabet))  # Reverses a list

    for i in range(len(alphabet)):  # Gets the length of a list
        code[alphabet[i]] = backwards[i]  # Populate the code dictionary with a letter of the alphabet and its encoded letter
--- /code ---

--- /task ---

La création d'une fonction `main()` est utile pour **appeler** toutes les fonctions nécessaires au premier démarrage de ton programme.

--- task ---

Trouve le commentaire `# Démarrage` et **définis** une fonction `main()` pour appeler ta fonction `code()`. Appelle ensuite la fonction `main()` dans le corps de ton code.

--- code ---
---
language: python filename: main.py - main() line_numbers: true line_number_start: 37
line_highlights: 38-41
---
# Start up
def main(): create_code()

main() --- /code ---

--- /task ---

### Test et débogage

--- task ---

Pour tester que ton dictionnaire `code` s'est correctement rempli, tu peux `imprimer` le dictionnaire dans son intégralité. Sous ta boucle `for` dans la fonction `creer_code`, ajoute une fonction `print` pour afficher le contenu.

--- code ---
---
language: python filename: main.py - create_code() line_numbers: true line_number_start: 11
line_highlights: 17
---
def create_code(): backwards = list(reversed(alphabet))

    for i in range(len(alphabet)):  #  Gets length of a list
        code[alphabet[i]] = backwards[i]  #  Populates the code dictionary with a letter of the alphabet and its encoded letter
    
    print(code)
--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton code pour voir si le dictionnaire `code` s'affiche correctement. Tu devrais voir un motif commençant par la lettre `a` combinée à `z` et la lettre `b` combinée à `y`.


![La sortie du dictionnaire de codes créé dans cette étape.](images/code-dictionary.PNG){:width="600px"}

**Débogage :** il n'y a pas de message d'erreur mais ton dictionnaire de code ne s'affiche pas à l'écran :
- Assure-toi que `print(code)` est indenté correctement au sein de la fonction `creer_code`
- Vérifie que tu as **appelé** correctement la fonction `creer_code()` et la fonction `main()`

**Débogage :** si tu vois un message indiquant que `code` n'est pas défini, assure-toi d'avoir initialisé le dictionnaire `code`.

**Débogage :** si tu vois un message concernant une erreur d'indentation :
- Vérifie que tu as correctement indenté tout ton code
- Reporte-toi à l'exemple de code de cette page pour t'aider à vérifier

--- /task ---

Dans l'étape suivante, tu vas **coder** un message à l'aide de ton dictionnaire `code` .

--- save ---
