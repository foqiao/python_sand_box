class duck:
    def quack(self):
        print('quack!!')

    def fly(self):
        print('fly!!')

class person:
    def quack(self):
        print('I am a duck')

    def fly(self):
        print('I am a flying duck')

def duck_and_person(things):
    #duck type example
    things.quack()
    things.fly()

    print()

#duck type means no matter what the names are, if the functions behave the same, treat them the same.
#class duck and class person behave the same
#then treat both classes the same