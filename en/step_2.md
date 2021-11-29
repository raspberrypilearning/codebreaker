## Encode the alphabet

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
To start you will create a dictionary for your encoded letters. 
</div>
<div>

</div>
</div>

![A screenshot of the output of the code dictionary which is created in this step.](images/code-dictionary.PNG){:width="600px"}

--- task ---

Open the [Codebreaker starter project](https://trinket.io/python/0eb6b467c0){:target="_blank"}. Trinket will open in another browser tab. 

If you have a `Trinket account`, you can click on the **Remix button** to save a copy to your My Trinkets library.

--- /task ---
### Set up the alphabet list and the code dictionary

The codebreaker program starts with two data structures. The first data structure is a **list** of all the letters in the alphabet and the second is a `code` **dictionary**. To save typing time you can create a list from a string by using the `list()` function.  

[[[list-function]]]

--- task ---

Find the `# Set up data structures` comment in the program, then use the `list()` function to create a **list** of letters from the `alphabet`. Next, **initialise** the `code` **dictionary** so that you can populate it in a later step.  

The `alphabet` list contains spaces at the beginning and end to preserve the spaces in the message. Strong encryption would not do this, as it makes the message easier to decode. The spaces have been kept in for this project to make the messages easier to read. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 5 
line_highlights: 7-8
---
# Set up data structures 

alphabet = list(' abcdefghijklmnopqrstuvwxyz ') # List from a string
code = {}

--- /code ---

--- /task ---

### Create a new list that reverses the alphabet

You need to create a new list that holds the alphabet, but backwards. You can use the `list()` function again to help with this. You can also use the `reversed()` function to reverse an existing list. 

--- task ---

Find the `# Create the atbash code by reversing the alphabet` comment then **define** a new function called `create_code`. Next, create a **list** that holds the **reverse** of the `alphabet` list. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10 
line_highlights: 12-14
---
# Create the atbash code by reversing the alphabet

def create_code():
  
  backwards = list(reversed(alphabet)) # Reversing a list

--- /code ---

--- /task ---

### Encode the alphabet

You now have two lists. One contains the alphabet written forwards, another with the alphabet backwards. You are now going to use these two lists to populate a dictionary. The **key** will store the alphabet written forwards and the **paired value** will store the alphabet backwards. 

The code dictionary is really important because you can use it to match each letter from your message using the **key**, with its encoded **paired value**. 

--- task ---

Within your `create_code` function, **populate** the `code` dictionary with data from the two **lists**. Use a `for` loop to get the length of the `alphabet` list and populate the **dictionary** with the data. 

`len()` is a function that you can use to find out the length of an **object**, such as a list. It is used here to iterate a `for` loop, as many times as there are characters in the `alphabet` list - its length. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 12
line_highlights: 16-17
---
def create_code():
  
  backwards = list(reversed(alphabet)) # Reversing a list
  
  for i in range(len(alphabet)): # Getting length of a list
    code[alphabet[i]] = backwards[i] # Populate the code dictionary with a letter of the alphabet and its encoded letter
--- /code ---

--- /task ---

Creating a `main()` function is useful to **call** all of the required functions when your program first starts. 

--- task ---

Find the `# Start up` comment and **define** a `main()` function to call your `code()` function. Next, call the `main()` function in the main body of your code. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 39
line_highlights: 41-45
---
# Start up

def main():
  create_code()

  
main()
--- /code ---

--- /task ---

--- task ---

In order to test that your `code` dictionary has populated correctly, you can `print` the dictionary in full. Under your `for` loop in the `create_code` function, add a `print` function to display the contents. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 12
line_highlights: 19
---
def create_code():

  backwards = list(reversed(alphabet))
  
  for i in range(len(alphabet)): # Getting length of a list
    code[alphabet[i]] = backwards[i] # Populate the code dictionary with a letter of the alphabet and its encoded letter
  
  print(code)
--- /code ---

--- /task ---
--- task ---

**Test:** Run your code to see if the `code` dictionary displays correctly. You should see a pattern starting with `a` paired with `z` and `b` being paired with `y`.


![A screenshot of the output of the code dictionary which is created in this step.](images/code-dictionary.PNG){:width="600px"}

**Debug:** There are no error messages but your code dictionary is not displaying on the screen:
- make sure that `print(code)` is indented correctly within the `create_code` function
- check that you have **called** the `create_code()` and the `main()` function correctly

**Debug:** If you see a message about `code` not being defined:
- make sure that you have initialised the `code` dictionary on line 8 

**Debug:** If you see a message about an indentation error:
- check that you have indented all of your code correctly
- look back at the sample code on this page to help you check

--- /task ---

In the next step you will **encode** a message with the help of your `code` dictionary. 

--- save ---
