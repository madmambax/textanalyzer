""""
text_analyze.py: First project to Engeto Online Python Academy
author: Martin Mannsbarth
email: mann.m@seznam.cz
discord: Martin M.#4226
"""

# import library for regex
import re

# variable with text for analysis, options for text 1-3

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# registered users for text analyzer

registered = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pas123"}

# print(registered)
# app start info
print("""
Dobrý den, právě jste spustili textový analyzátor,
pro použití je nutné se autorizovat.
""")
# user credentials for verification - input
user_name = input("Zadejte prosím své uživatelské jméno: ")
user_passwd = input("Zadejte prosím své heslo: ")

# user verification
if registered.get(user_name) == user_passwd:
    print(f"Vítejte uživateli {user_name} v aplikaci textového analyzátoru")
else:
    print("Neověřený uživatel, ukončuji aplikaci ...")
    quit()

# user choice for text analysis - input
text_option = input("Prosím vyberte text - zadejte číslo textu mezi 1-3: ")

if text_option.isdigit() and 1 <= int(text_option) <= 3:
    text_opt = int(text_option) - 1
# show text according user choice
    print("Zvolili jste k analýze tento text: ")
    print(TEXTS[text_opt])
else:
    print("Špatná volba, ukončuji ...")
    quit()