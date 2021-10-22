## Create an atbash cypher

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
The next step is to create a function which can take our text, flip it and reverse it with our atbash cypher list, and return it as an encoded message. 
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

 First, we will remove the print statement in our previous function, because we won't need it now we know our dictionary is working. 

--- task ---
 
**Comment out** the print statement on line 19 by placing a hashtag at the beginning of the line:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 16
line_highlights: 19
---
  for i in range(len(alphabet)): # Getting length of a list
    code[alphabet[i]] = backwards[i] # Populate the code dictionary with a letter of the alphabet and its encoded letter
  
#  print(code)
--- /code ---
 
--- /task ---

We will now add our new function that will reverse the dictionary we have created.

--- task ---

Find the comment which says `# Encrypt/decrypt a pice of text — atbash is symetrical` on line 53. Underneath the comment, define a function called `atbash` with the parameter `text`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 53 
line_highlights: 54
---
# Encrypt/decrypt a pice of text — atbash is symetrical
def atbash(text):

--- /code ---

Press Enter. You should see the next line indented. 

--- /task ---

We will need this new function to take our text, convert it to lower case, then add it all to another list. Then, we want it to swap out the letters in the list for the letters in our cypher - thus creating an encoded message! First, we need to create the list of our text.

--- task ---

 Beneath your definition, keep the indent and type: 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 53 
line_highlights: 55-57
---
# Encrypt/decrypt a piece of text — atbash is symmetrical
def atbash(text):
    text = text.lower() # Converting text to lowercase
    text = list(text)
    output = []
--- /code ---

--- /task ---

The next part of our code will encode the text by looking through our newly created list, matching each letter in the text to it's atbash partner, then create a new list made of the atbash letters and output it. 

--- task ---

Leave a blank line under the last code you entered (make sure you keep the indent), then type:
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 57 
line_highlights: 59-61
---
    output = []

    for letter in text:
        if letter in code:
            output.append(code[letter]) # list append

    return ''.join(output)

--- /code ---

--- /task ---

Now that we have a function which will encode text we give it and output a new encoded message, we need to run it to make sure it works. To do that, we will create a menu by coding a **loop** that will repeatedly ask our user which function they would like to use. As we only have one function at the moment, it's pretty simple. 

--- task ---

**Find** the comment in your script that says `# Create a text-based menu system` on line 46 and begin by defining a function called `menu`:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 46
line_highlights: 47
---
# Create a text-based menu system
def menu():

--- /code ---

--- /task ---

Now we are going to set the `choice` when the program first runs to `None`. Because the loop we are about to write requires a 'correct' answer (one we have defined) to break the loop, storing an initial wrong answer will keep the menu loop running until another 'correct' answer is entered. 

--- task ---

**Find** the comment in your script that says `# Start with a wrong answer for choice`. Underneath this line (making sure you have an indent!) type:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 46
line_highlights: 50
---
# Create a text-based menu system
def menu():

    # Start with a wrong answer for choice.
    choice = None
--- /code ---

--- /task ---

Now that we have set choice to a wrong answer, we want to create a loop that will only break if an `input` that matches a right answer is given. We want a while loop, that runs as long as our answers are NOT one we have defined. 

--- task ---

**Find** the comment in your script that says `# Keep asking the user for the right answer`. Underneath this line (making sure you have an indent!) type:
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 46
line_highlights: 50
---
# Create a text-based menu system
def menu():

    # Start with a wrong answer for choice.
    choice = None
--- /code ---
--- /task ---


--- save ---