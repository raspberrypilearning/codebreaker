## Analyse the frequency

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Use a bar chart to analyse the frequency of letters in an encoded message. 
</div>
<div>
![A bar chart showing the frequency of letters in the English language compared to the frequency of letters used in the encoded message.](images/frequency-analysis.PNG){:width="400px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
In all languages, each letter in its alphabet has a 'personality' or set of traits when used in that language. One of the most obvious traits a letter has in any language is how often it appears.  **Frequency analysis** is the method of breaking codes by looking at how often letters are used in the language of the code, and comparing that to how often encoded letters show up in a message. In English, the letter **E** is the most commonly used letter (it shows up 12.8% of the time), followed by **T** (at 9.1%). The least often used letter is **Z**.
</p>
--- task ---

The `print(message_freq)` line of code on line 92 is no longer needed. Add a `#` to the beginning of it so that Python ignores it when the code is run. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 88
line_highlights: 92
---
  elif choice == 'f':
    print('Analysing message…')
    message = get_text('input.txt') # Take input from the same file. We have a 'longer.txt' or similar containing cyphertext we know to perform reasonably well for frequency analysis
    message_freq = frequency(message) # Get the frequency of the letters in the message, as %
    # print(message_freq)
--- /code ---

--- /task ---

--- task ---

Find the `# Make frequency chart` comment on line 45 and create a new function called `make_chart()`. This function needs two parameters called `text` and `language`. The frequency chart will be a **bar** chart and the **title** is `Frequency analysis`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 45
line_highlights: 47-50
---
# Make frequency chart

def make_chart(text, language):
  
  chart = Bar()
  chart.title = 'Frequency analysis'
--- /code ---

--- /task ---


--- save ---