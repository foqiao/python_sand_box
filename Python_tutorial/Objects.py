#file object with context manager
f = open('text.txt')

print(f.read())

f.close()

#context manager syntax
with open('text.txt', 'r') as f:
    F = f.read()
    print(F, end='')

#use loop to list out the content
with open('text.txt', 'r') as f1:
    for l in f1:
        print(l, end='')

#restrict the output bits
with open('text.txt', 'r') as f2:
    F1 = f2.read(5)
    #print out first 5 bits of the content
    print(F1)
    #print out the NEXT 5 BITS of the content
    print(F1)
    #the read with begin at a predefined location
    #below will begin at the start
    f2.seek(0)

#create the file
with open('text2.txt', 'w') as file:
    #write the word test
    file.write('test')
    print(file.read())
    #over write the previous word
    file.seek(0)
    file.write('text')
    print(file.read())