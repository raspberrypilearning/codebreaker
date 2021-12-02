## Encode a message

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create a function which can take your text, flip it and reverse it with your atbash cypher list, and return it as an encoded message. 
</div>
<div>
![A screenshot of the output of the code created in this step. An encoded version of a secret message is displayed.](images/test-encoded.PNG){:width="300px"}
</div>
</div>

--- task ---
 
**Comment out** the print statement used for testing on line 17 by placing a hashtag at the beginning of the line:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 14
line_highlights: 17
---
  for i in range(len(alphabet)): # Getting length of a list
    code[alphabet[i]] = backwards[i] # Populate the code dictionary with a letter of the alphabet and its encoded letter
  
#  print(code)
--- /code ---
 
--- /task ---

### Setup your atbash function

You will now add your new **function** that will encode some text using the **atbash** cypher.

--- task ---

Find the comment which says `# Encode/decode a piece of text — atbash is symmetrical` on line 26. Underneath the comment; define a function called `atbash`, with the **parameter** `text`. Parameters allow you to pass values into functions that can be used within that function.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 26 
line_highlights: 27
---
# Encode/decode a piece of text — atbash is symmetrical
def atbash(text):

--- /code ---

Press Enter. You should see the next line indented. 

--- /task ---

[[[parameters]]]

### Convert text to lowercase 

First your function needs to convert the `text` to lowercase. A new **variable** called `output` will then need to be created to hold the encoded message.

--- task ---

 Beneath the line of code when you have defined the `atbash()` function, type: 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 27 
line_highlights: 29-30
---
# Encode/decode a piece of text — atbash is symmetrical
def atbash(text):
  text = text.lower() # Converting text to lowercase
  output = ''

--- /code ---

--- /task ---

### Encode your text

The next part of your code will **encode** the `text` that has been **passed** into the function. A `for` loop will need to be used to go through each letter in the `text` and convert it to an encoded letter using the `code` dictionary. Finally, it will **return** the encoded message.   

--- task ---

Leave a blank line under the last code you entered (make sure you keep the indent), then type:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 28
line_highlights: 33-37
---
# Encode/decode a piece of text — atbash is symmetrical
def atbash(text):
  text = text.lower() # Converting text to lowercase
  output = ''
  
  for letter in text: 
    if letter in code: 
      output += code[letter] # Populate output with the encoded/decoded message using the dictionary
  
  return output # Return the encoded/decoded message

--- /code ---

--- /task ---

### Test and Debug

--- task ---

Now that you have a **function** which will **encode text**, you need to run it to make sure it works. Find your `main()` function on line 47 and add in a function call to run the `atbash()` function. 

The 'Test' string is **passed** into the function so that it can be encoded. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 48
line_highlights: 51
---
# Start up
def main():
  create_code()
  print(atbash('Test'))

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see if the test message displays correctly. You should see the console output `gvhg`.

![A screenshot of the output of the encoded text which is created in this step.](images/test-encoded.PNG){:width="600px"}

**Debug:** If you see a message about an indentation error:
- check that you have indented all of your code correctly
- look back at the sample code on this page to help you check

--- /task ---

--- task ---

**Comment out** your `print(atbash('Test'))` line of code now that you have finished testing. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 48
line_highlights: 51
---
# Start up
def main():
  create_code()
  #print(atbash('Test'))

--- /code ---

--- /task ---

In the next step you will **encode** a message with the help of your `code` dictionary. 

--- save ---