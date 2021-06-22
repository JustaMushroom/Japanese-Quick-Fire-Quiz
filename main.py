from kanatest import kanatest
from terminaltables import AsciiTable

body_data = [
    ['Selection', 'Option'],
    ['1', 'Take Hiragana Test'],
    ['2', 'Take Katakana Test'],
    ['3', 'Take Mixed Test'],
    ['q', 'quit']
    ]

body = AsciiTable(body_data)
print(body.table)

selection = input("menu>")
if selection == "1":    
    kanatest(1)
elif selection == "2":
    kanatest(2)
elif selection == "3":
    kanatest(0)
elif selection.upper() == "Q":
    quit()