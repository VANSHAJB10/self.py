# 1. Jinja2 Expression to use the variable `name` that generates the expected output. 
The name is {{name}}

# 2. Update the jinja2 expression to display the `name` in UPPERCASE
The name is {{ name|upper }}

# 3. to replace the word 'Bourne' in dialogue with 'Bond'
{{ dialogue| replace ("Bourne", "Bond") }}

#4. expression to join them to form a single sentence. {  "words": ["we","are","meant","to","be","together"]   }
{{ words|join(' ') }}
Output --> we are meant to be together
