import random

def prime_search(input_num):
    divisor = [2, 3, 5, 7]
    i = random.choice(divisor)
    if input_num % i != 0:
        print('Prime Number')

input_num1 = int(input("Please enter an integer less than 100: "))
prime_search(input_num1)