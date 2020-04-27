def num_square(nums):
    #comprehensive generator that generates squared nums
    num = [i * i for i in nums]

    #for loop generator that generates squared nums
    for i in nums:
        num = []
        num.append(i * i)

    #for loop generator that generates num elements from nums list
    for i in nums:
        print(i)
        #yield the squared value within the string
        yield i * i