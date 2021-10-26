## Create a Frequency Analyser

<div style="display: flex; flex-wrap: wrap;">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step, we will code a frequency analyser function to work out how often each letter of the alphabet appears in our text. 
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Frequency Analysis measures how often something appears so we can look for patterns in that data. It is possible to decode monoalphabetic cyphers (if you know the language the message is in) by looking at how often each letter appears and matching it to the [most commonly used letters](http://letterfrequency.org/letter-frequency-by-language/) in that language.
</p>

We now need to create a function that will take our text and convert it all to one case (to avoid confusion), count the number of times each letter in the message appears, then convert that number into a percentage of the whole so we can compare it to the frequency of letters in English.

--- task ---

On line 22, beneath the comment that reads `# Calculate the frequency of all letters in a piece of text`, define a function called `frequency`, and have the first thing it does be to convert our message to lower case:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21 
line_highlights: 23-25
---
# Calculate the frequency of all letters in a piece of text

def frequency(text):
    
    text = list(text.lower()) # Lowercase the message and make it a list
--- /code ---

--- /task ---

--- task ---
On line 22, beneath the comment that reads `# Create a dict of every letter, with a count of 0`, make sure you **keep the indentation** and type:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 28-30
---
# Calculate the frequency of all letters in a piece of text

def frequency(text):
  
  text = list(text.lower()) # Lowercase the message and make it a list
  
  # Create a dict of every letter, with a count of 0
  freq = {}
  for letter in alphabet:
    freq[letter] = 0
--- /code ---

--- /task ---

--- task ---

The next thing we need our function to do is to calculate the length of the message. On line 31, beneath the comment that reads `# Count the letters in the message`, make sure you **keep the indentation** and type:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 33
---
# Calculate the frequency of all letters in a piece of text

def frequency(text):
  
  text = list(text.lower()) # Lowercase the message and make it a list
  
  # Create a dict of every letter, with a count of 0
  freq = {}
  for letter in alphabet:
    freq[letter] = 0
  
  # Count the letters in the message
  total_letters = len(text)
--- /code ---

--- /task ---

Once we know how long the message is, we can begin counting the letters in it to determine how often they appear.

--- task ---

 Leave a blank line at the end of your script, make sure you keep the indentation and add:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 35-37
---
# Calculate the frequency of all letters in a piece of text

def frequency(text):
  
  text = list(text.lower()) # Lowercase the message and make it a list
  
  # Create a dict of every letter, with a count of 0
  freq = {}
  for letter in alphabet:
    freq[letter] = 0
  
  # Count the letters in the message
  total_letters = len(text)
  
  for letter in text:
    if letter in freq: # Maybe it's punctuation? First use of in as a conditional clause
      freq[letter] += 1
--- /code ---

--- /task ---

This section of code:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights:
---
for letter in text:
    if letter in freq:
        freq[letter] += 1
--- /code ---

looks at each of the letters in our message `text`, and if the letter appears in our frequency list it adds 1 to that letter's value. The more times a letter appears, the higher that value will be. Once we know how often each letter appears, we can then convert from this count to a percentage of the whole message (since we know the length).

--- task ---

On line 38, under the comment that reads `# Convert from counts to percentages` make sure to keep the indentation and type:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 39-41
---
# Calculate the frequency of all letters in a piece of text

def frequency(text):
  
  text = list(text.lower()) # Lowercase the message and make it a list
  
  # Create a dict of every letter, with a count of 0
  freq = {}
  for letter in alphabet:
    freq[letter] = 0
  
  # Count the letters in the message
  total_letters = len(text)
  
  for letter in text:
    if letter in freq: # Maybe it's punctuation? First use of in as a conditional clause
      freq[letter] += 1
  
  # Convert from counts to percentages
  for letter in freq:
    freq[letter] = freq[letter] / total_letters * 100
  
  return freq
--- /code ---

--- /task ---

Now we have a function which can calculate the frequency of letters in our message, we need to link it to our user menu. Right now, out user can only choose the letter `c` to encode or decode a message. We're now going to add the option `f` to analyse the letter frequency of our message by calling our new function. 

--- task ---

Scroll down to your `menu` function at the bottom of your script. On line 76 and 77 add the following to your code:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 77 
line_highlights: 78-80
---
  # Keep asking the user for the right answer
  while choice != 'c' and choice != 'f':
    
    choice = input('Please enter c to encode/decode text, or f to perform frequency analysis:' )
--- /code ---

--- /task ---

Underneath your first `if` statement asking the user to select `c`, we need to add en `elif` statement so the user can choose the option to analyse and print the letter frequency by pressing `f`.

--- task ---

Leave a blank line after the `if` statement and on line 85 type:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 77
line_highlights: 88-92
---
  # Keep asking the user for the right answer
  while choice != 'c' and choice != 'f':
    
    choice = input('Please enter c to encode/decode text, or f to perform frequency analysis:' )
  
  if choice == 'c':
    print('Running your message through the cypher…')
    message = get_text('input.txt') # Take input from a file 
    code = atbash(message)
    print(code)

  elif choice == 'f':
    print('Analysing message…')
    message = get_text('input.txt') # Take input from the same file. We have a 'longer.txt' or similar containing cyphertext we know to perform reasonably well for frequency analysis
    message_freq = frequency(message) # Get the frequency of the letters in the message, as %
    print(message_freq)
--- /code ---

Save and run your code. Choose `f` at the prompt and you should see a readout of the letter frequency of your message in the console.

--- /task ---

In the next step you will display the frequency analysis data in a cool looking chart!

--- save ---
