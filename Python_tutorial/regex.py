import re

text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPRQSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ % $ # @ [] () {} *

coreyms.com

321-555-4321
123.555.1234

Mr. Schefer
Mr. Smith
Ms. Davis
Mr. T
"""

#raw string output the pre-processed string especially when it comes to special characters
print('\tTab')
#vs
print(r'\tTab')

#pattern matching procedure
pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#to find only the period of the string
pattern1 = re.compile(r'\.')
matches1 = pattern1.finditer(text_to_search)

for match1 in matches1:
    print(match1)