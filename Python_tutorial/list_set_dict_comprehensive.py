num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []

for n in num:
    my_list.append(n)
print(my_list)

#or
#my_list = [n for n in num]
#print(my_list)

#n ** 2 comprehensive expression
my_list = [n * n for n in num]
print(my_list)
#even number searching expression
my_list1 = [n for n in num if n % 2 == 0]
print(my_list1)
#pairing two strings
my_list2 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list2)
#zip two strings
name = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
hero = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(zip(name, hero))

#zip strings using comprehensive expression
my_dict = {n: h for n, h in zip(name, hero)}
print(my_dict)