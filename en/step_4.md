## Encode contents from a text file

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Its time to encode a message from a text file. 
</div>
<div>
![A screenshot of the output of the code displaying an encoded message. ](images/encoded-message.PNG){:width="400px"}
</div>
</div>

--- task ---

Find the `# Fetch and return text from a file` comment on line 70 then define a `get_text()` function. This function has one parameter called `filename`. Use the `filename` to open the file and read it into the `text` variable, then **return** the `text` variable.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 70
line_highlights: 72-76
---
# Fetch and return text from a file

def get_text(filename):
    with open(filename, 'r') as f:
      text = f.read().replace('\n','') # Need to strip the newline characters
    
    return text
--- /code ---


--- /task ---

--- task ---

The `menu()` function needs to encode a secret message from a text file. Find line 64 and **replace** `message = 'my secret message'` with the `get_text()` function call. Enter the name of the file `input.txt` as an **argument**.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 62
line_highlights: 64
---
  if choice == 'c':
    print('Running your message through the cypher…')
    message = get_text('input.txt') # Take input from a file 
    code = atbash(message)
    print(code)
--- /code ---


--- /task ---

You can now **add** your own secret message to the `input.txt` file. 

--- task ---

Find the `input.txt` tab in Trinket to access the contents of the text file. You will see this just above your code window. Delete the `replace with your message` text and enter your own secret message. 

![Animation demonstrating how to find the input.txt tab at the top of the trinket window.](images/input.gif)

<!-- Does this need any instructions for offline use?-->

--- /task ---

--- task ---

**Test:** Run your code to see if it displays your encoded message after entering the letter c when prompted. 

![A screenshot displaying the encoded secret message](images/input-text-test.gif)

**Debug:** 

--- /task ---


--- save ---