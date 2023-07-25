
--- question ---

---
legend: Question 3 of 3
---

A line of code is needed to create a **bar chart** using `pygal`. The code must select the x-axis labels from the **keys** used in the `text` **dictionary**. Which is the correct line of code that can be used for this purpose?

--- choices ---

- ( ) 

chart.x_labels = keys()

  --- feedback ---

Not quite, Python needs to know **which** dictionary to select the keys from. 

  --- /feedback ---

- ( ) 

chart.x_labels = list(text)

  --- feedback ---

  Not exactly, Python needs to know which part of the dictionary it should use to display as the labels. 

  --- /feedback ---

- ( ) 

chart.x_labels = list(keys.text())

  --- feedback ---

  Almost, this line of code contains the right parts but they aren't in the correct order. 

  --- /feedback ---

- (x) 

chart.x_labels = list(text.keys())

  --- feedback ---

Correct! This line of code will add the x-axis labels based on the **keys** held in the `text` dictionary. 

  --- /feedback ---

--- /choices ---

--- /question ---
