#Scope has four different types
#LEGB
#Local, Enclosing, Global, Built-in

#global example
x = 'global x'

#local example
def local():
    y = 'local y'
    print(y)

local()

#global vs local
x1 = 1

def local1():
    y1 = 2
    print(y1)
    print(x1)

#globalize local variable
def local2():
    global z
    z = 25

print(z)

#Builtins example
m = min([25, 549, 23, 22, 17])
print(m)

#show all builtins
import builtins
print(dir(builtins))

#encapsulation example
def outer():
    #local variable for outer function
    #global variable for inner function
    i = 'local i'
    def inner():
        #local variable for inner function
        j = 'local j'
        print(j)
    print(i)

outer()

#nonlocal or globalize encapsulation variable
def outer1():
    j1 = 'local i1'
    def inner1():
        nonlocal j1
        j1 = 'local j1'
        print(j1)
    print(j1)

outer1()
#output j1 value within the inner1 function