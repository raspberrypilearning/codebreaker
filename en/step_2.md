## Encode the alphabet

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will define a function named <kbd>create_code</kbd> which will make a <b>list</b> with the letters of the alphabet and then create a dictionary you can use in your cypher.
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Open the [Codebreaker starter project](https://trinket.io/python/0eb6b467c0){:target="_blank"}. Trinket will open in another browser tab. 

If you have a `Trinket account`, you can click on the **Remix button** to save a copy to your My Trinkets library.

--- /task ---

--- task ---

Find the `# Set up data structures` comment then use the `list()` function to create a **list** of letters from the `alphabet`. Next, **initialise** the `code` dictionary so that you can populate it in a later step.  

<!--- I want an ingredient here that describes how the list function works. I don't know how to make one -->

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

--- task ---

**Define** the `create_code()` function on line 9 of your script. 

--- /task ---

--- save ---
