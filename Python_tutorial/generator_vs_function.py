import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineer', 'CompSci', 'Arts', 'Business']

def people_function(people_num):
    result = []
    for i in range(people_num):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(people_num):
    result = []
    for i in range(people_num):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    yield result

t1 = time.clock()
print(people_function(1000000))
t2 = time.clock()

t3 = time.clock()
print(people_generator(1000000))
t4 = time.clock()