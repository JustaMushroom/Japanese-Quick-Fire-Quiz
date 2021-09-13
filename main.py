# Import modules
from kanatest import kanatest
from terminaltables import AsciiTable

# Define clear function - clears the terminal display
def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")

# Define main menu data
body_data = [
    ['Selection', 'Option'],
    ['1', 'Take Hiragana Test'],
    ['2', 'Take Katakana Test'],
    ['3', 'Take Mixed Test'],
    ['q', 'quit']
    ]

# Build the ASCII Table based on the main menu data
body = AsciiTable(body_data)

# Clear the terminal display
clear()

# Display the main menu data as a table
print(body.table)

# Listen for user input
# TODO: add user input cleaning
selection = input("menu>")

# Check if the input matches a specific pattern
# TODO: add an else case
if selection == "1":    
    kanatest(1)
elif selection == "2":
    kanatest(2)
elif selection == "3":
    kanatest(0)
elif selection.upper() == "Q":
    quit()
