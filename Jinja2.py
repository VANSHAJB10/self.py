# 1. Jinja2 Expression to use the variable `name` that generates the expected output. 
The name is {{name}}

# 2. Update the jinja2 expression to display the `name` in UPPERCASE
The name is {{ name|upper }}

# 3. to replace the word 'Bourne' in dialogue with 'Bond'
{{ dialogue| replace ("Bourne", "Bond") }}
