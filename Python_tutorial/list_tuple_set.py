courses = ["CompSci", "Math", "History", "Physics"]
courses1 = courses
courses2 = courses
courses3 = courses
courses4 = courses
courses5 = courses
courses_extension = ["Project", "Astrophysic"]
#print all elements
print(courses)
#add 'Art' to courses
courses.append('Art')
print(courses)
#add 'Art' to a specific location
courses1.insert(0, 'Art')
print(courses)
#add elements within a list to another
courses2.extend(courses_extension)
#print out a specific range of the list
print(courses3[2:])
print(courses3[:3])
print(courses3[2:4])
#add an entire list into another
courses4.append(courses_extension)
print(courses4)
#or
courses5.insert(2, courses_extension)
print(courses5)
#remove the expanded element(s) to another
courses5.remove(courses_extension)
print(courses5)
#reverse the order of a list
courses.reverse()
print(courses)

#sort a number list
num = [1, 5, 4, 2, 3]
num.sort()
print(num)
#pop the last element of the num list out
num.pop()
print(num)
#print out the popped element
popped = num.pop()
print(popped)
#reverse the sorting
num2 = [1, 2, 3, 4, 6, 7, 10, 9, 100, 98, 88]
num2.sort(reverse=True)
print(num2)

courses6 = ["History", "Math", "Compsci", "Art", "Physics"]
courses6.sort()
print(courses6)

#sorted a copy of the original function
courses7 = ["History", "Math", "Compsci", "Physics", "Art"]
sorted_courses7 = sorted(courses7)
print(courses7)
print(sorted_courses7)

#some build-in functions
num = [1, 9, 7, 18, 698]
print(min(num))
print(max(num))
print(sum(num))

#index of a specific element
print(courses7.index("History"))

#print out items through a loop
for i in courses7:
    print(i)

#print out the index with the printed items
for index, i in enumerate(courses7):
    print(index, i)

#join or split a list
course_str = ", ".join(courses7)
print(course_str)

course_split_str = course_str.split(" - ")
print(course_split_str)

#tuple and list looks same but tuple is immutable comparing to mutable list
course_list = ["COMP 1510", "COMP 1537", "COMP 1517"]
course_list[0] = "COMM 1116"
print(course_list)

#course_list = ("COMP 1510", "COMP 1537", "COMP 1517")
#course_list[0] = "COMM 1116"
#print(course_list)
#Error

#a set is an unordered and unique string
#a set can be used to check and eliminate duplicate elements and check elements overlapped between sets
num_set = {1, 2, 3, 4, 5, 6}
num_set1 = {1, 2, 4, 5, 6, 8}
print(num_set.intersection(num_set1))
print(num_set.difference(num_set1))

#to combine two sets and print out all elements in both sets, union method is needed
print(num_set.union(num_set1))

#empty sets declaration
name_set = set()