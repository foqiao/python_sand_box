num = [24, 39, 78, 986, 12203]
#just for loop
for i in num:
    print(i)
#for loop with break
for i in num:
    if i < 100:
        print('found')
        break
    print(i)
#for loop with continue
for i in num:
    if i < 100:
        print('found')
        continue
    print(i)

#nest for loop
for i in num:
    for j in 'abc':
        print("%d:%s" % (i, j))

#x = 0
#while x < 0:
#print(x)
#Above is a infinite loop

#while loop will continue output x as long as the condition matches
#for loop will continue output x within a predefined range