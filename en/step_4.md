## Create a menu 

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Now you are going to create a menu system for your user to make choices about what they would like to do. 
</div>
<div>
![The output of the code created in this step. An encoded version of a secret message is displayed.](images/encode-a-message.PNG){:width="400px"}
</div>
</div>

--- task ---

**Find** the comment in your code that says `# Create a text-based menu system` and begin by defining a function called `menu()`:

--- code ---
---
language: python
filename: main.py - menu()
line_numbers: true
line_number_start: 41
line_highlights: 42
---
# Create a text-based menu system
def menu():
--- /code ---

--- /task ---

Your menu needs a **loop** that continually asks the user what they would like to do until they have entered a valid choice. To get this started, you will create a **variable** called `choice` and set it to `''`. This will allow the **while** loop to run its first loop. 

--- task ---

Create a new variable called `choice` and set the value to `''`:

--- code ---
---
language: python
filename: main.py - menu()
line_numbers: true
line_number_start: 41
line_highlights: 43
---
# Create a text-based menu system  
def menu():
    choice = ''  # Start with a wrong answer for choice.

--- /code ---

--- /task ---

### Use a `while` loop to get user input

Now that you have set `choice` to a wrong answer, you want to create a **loop** that will only break if an `input` that matches a right answer is given. You want a **while loop** that runs as long as your answer **DOES NOT** match one you have defined. 

--- task ---

You can use a **while loop** to run a piece of code **while** a **condition** is **True**. In this instance, as long as the user **does not** choose `c` or `f`, the loop will continue to run. Enter the code that will set the **conditions** for a **while loop** and prompt the user for input:

--- code ---
---
language: python
filename: main.py - menu()
line_numbers: true
line_number_start: 42
line_highlights: 45-46
---
def menu():
    choice = ''  # Start with a wrong answer for choice

    while choice != 'c' and choice != 'f':  # Keep asking the user for the right answer
        choice = input('Please enter c to encode/decode text, or f to perform frequency analysis: ')
--- /code ---

--- /task ---

Once the user has given a correct answer, the loop will end. Next create an `if` statement that will run your `atbash` function if the user enters `c`.

You will decide what happens when a user enters `f` in a later step. 

--- task ---

Underneath the last line (making sure you still have an indent!), type:

--- code ---
---
language: python
filename: main.py - menu()
line_numbers: true
line_number_start: 42
line_highlights: 48-52
---
def menu():
    choice = ''  # Start with a wrong answer for choice

    while choice != 'c' and choice != 'f':  # Keep asking the user for the right answer
        choice = input('Please enter c to encode/decode text, or f to perform frequency analysis: ')

    if choice == 'c':
        print('Running your message through the cypher…')
        message = 'my secret message' 
        code = atbash(message)
        print(code)

--- /code ---

--- /task ---

--- task ---

Change the string that says `'my secret message'` to anything you like. This string is the message that will be encoded and decoded.

--- code ---
---
language: python
filename: main.py - menu()
line_numbers: true
line_number_start: 42
line_highlights: 50
---
def menu():
    choice = ''  # Start with a wrong answer for choice.

    while choice != 'c' and choice != 'f':  # Keep asking the user for the right answer
        choice = input('Please enter c to encode/decode text, or f to perform frequency analysis: ')

    if choice == 'c':
        print('Running your message through the cypher…')
        message = 'my secret message'
        code = atbash(message)
        print(code)

--- /code ---

--- /task ---

--- task ---

At the end of your `main()` function, type `menu()` to call the `menu` function when the program runs:

--- code ---
---
language: python
filename: main.py - main()
line_numbers: true
line_number_start: 54
line_highlights: 58
---
# Start up
def main():
    create_code()
    # print(atbash('Test'))
    menu()

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code. Type `c` and press <kbd>Enter</kbd> to encode your message string!

![The output of the code created in this step. An encoded version of a secret message is displayed.](images/encode-a-message.PNG){:width="400px"}

**Debug:** If you see a message about an indentation error:
- Check that you have indented all of your code correctly
- Look back at the sample code on this page to help you check

**Debug:** If you see the error message `c is not defined` when you run your code, check that you have used apostrophes ('') around your c in the condition `choice != 'c'`.

**Debug:** If nothing happens when you press `c`, check that you have correctly spelled `message`.
  
--- /task ---

In the next step you will use your `atbash()` function to encode the contents of a text file.

--- save ---
