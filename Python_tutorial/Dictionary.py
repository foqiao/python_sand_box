dictionary = {'Name': 'Ted', 'Age': 21, 'Home address': "1507-6088 Willingdon Avenue", 'Student number': 'A01027086'}
#get value using dict[index]
print(dictionary['Name'])
# get method perform same as above
print(dictionary.get('Student number'))
# check whether the element is available
print(dictionary.get('Surname'))
#assign the state for a non-exist element
print(dictionary.get('Surname', 'Not found'))

#dictionary has three different methods, keys for index, values for value, items for both
student = {'Name': 'Ted', 'Age': 21, 'Surname': 'Yuan'}
print(student.keys())
print(student.values())
for key, value in student.items():
    print(key, value)