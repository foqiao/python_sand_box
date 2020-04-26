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
123*555*1234
800-555-1234
900-555-1234

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

#match coreyms.com except the dot before 'com'
pattern2 = re.compile(r'coreyms\.com')
matches2 = pattern2.finditer(text_to_search)

for match2 in matches2:
    print(match2)

#special character
#\. anything matches except dot
#\w word characters matching
#\W no word characters matching
#\D digits matching
#\d no digits matching
#\s whitespace matching
#\S no whitespace matching
#\b boundary matching
#\B no boundary matching
#^ beginning of the matching string
#$ end of the matching string
#[] empty bracket matching
#[^] non-empty bracket matching, ^ can be any character

#match the phone number within the double string separated by dot instead of hyphen
pattern3 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches3 = pattern3.finditer(text_to_search)

#match all the phone number within the double string separated by anything
pattern4 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches4 = pattern4.finditer(text_to_search)

#match only the phone number starts with 800 and 900
pattern5 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches5 = pattern5.finditer(text_to_search)