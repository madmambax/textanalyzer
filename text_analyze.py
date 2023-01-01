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

# delimeter
delimiter = "-" * 64

# registered users for text analyzer

registered = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pas123"}

# print(registered)
# app start info

print("""
Hello, you have just launched the text analyzer,
authorization is required for use.
""")

# user credentials for verification - input

user_name = input("Please, insert your name: ")
user_passwd = input("Please, insert your password: ")

# user verification

if registered.get(user_name) == user_passwd:
    print(delimiter)
    print(f"Welcome user {user_name} in the application text analyzer.\nWe have 3 texts to be analyzed. ")
    print(delimiter)
else:
    print("Unregistered user, terminating the program...")
    quit()

# user choice for text analysis - input

text_option = input("Please, choose the text - insert number from the range 1-3: ")
# print(delimiter)
if text_option.isdigit() and 1 <= int(text_option) <= 3:
    text_opt = int(text_option) - 1
      
# show text according user choice

    print("You choose this text for analysis: ")
    print(TEXTS[text_opt],"\n")
    print(delimiter)
# count and print the number of words in the text
# words = re.findall(r'\w+', TEXTS[text_opt])

    words_count = len(re.findall(r'\w+', TEXTS[text_opt]))
    print(f"Number of words: {words_count}")
    
# count numerics kind of words and numerics sum
    words_numerics = len(re.findall(r'\b\d+\b', TEXTS[text_opt]))
    numerics = re.findall(r'\b\d+\b', TEXTS[text_opt])
    sum = 0
    for num in numerics:
        sum += int(num)
        
    print("Number of numerics:", words_numerics)
    print("Summary for numerics strings", sum)
    
# count title words
    words_title = len(re.findall(r'\b[A-Z]{1}[a-z]+\b', TEXTS[text_opt]))
    print("Number of title words:", words_title)
    
# count upper case words
    words_uppercase = len(re.findall(r'\b[A-Z]+[A-Z]+\b', TEXTS[text_opt]))
    print("Number of uppercase words:", words_uppercase)
    
# count lower case words
    words_lowercase = len(re.findall(r'\b[a-z]+\b', TEXTS[text_opt]))
    print("Number of lowercase words:", words_lowercase )  
    print(delimiter)  
    
# word length frequency and simple graph
    graph = "*"
    frequence = []
    words_frequence = re.findall(r'\w+', TEXTS[text_opt])
   
    for word in words_frequence:
        frequence.append(len(word))
     
    occured = {}
    for item in frequence:
        if item in occured:
            occured[item] = occured.get(item)+1
        else:
            occured[item] = 1

    
    print(f"{'LEN |':^4}{'OCCURENCIES':^17}{'|NR.':^9}")
    print(delimiter)
    for k,v in sorted(occured.items()):
    		print(f"{str(k) : ^4}{('|' + graph * v ).ljust(16): ^17}{'|' + str(v) : ^9}")
      
else:
    print("Incorrect option, terminating ...")
    quit()