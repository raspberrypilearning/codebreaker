## Create an atbash cypher

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
The next step is to create a function which can take our text, flip it and reverse it with our atbash cypher list, and return it as an encoded message. 
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

 
--- task ---

Find the comment which says `# Encrypt/decrypt a pice of text — atbash is symetrical` on line 30. Underneath the comment, define a function called `atbash` with the parameter `text`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 30 
line_highlights: 31
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
line_number_start: 30 
line_highlights: 32-34
---
# Encrypt/decrypt a pice of text — atbash is symetrical
def atbash(text):
  text = text.lower() # Converting text to lowercase
  text = list(text)
  output = []
--- /code ---

--- /task ---



--- task ---

Step content... 
Can use:
**Test:**
**Choose:**
**Tip:**

--- /task ---

--- save ---