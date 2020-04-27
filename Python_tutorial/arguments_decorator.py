#first layer of the decorated function
def prefix_decorator(prefix):
    #second layer of the decorated function
    def decorator_function(original_function):
        #third layer of the decorated function
        def wrapper(*args, **kwargs):
            print(prefix, 'Executed before', original_function.name)
            result = original_function(*args, **kwargs)
            return result
        return wrapper_function
    return decorator_function

#decorated function annotation
@prefix_decorator('TESTING: ')
def display_info(name, age):
    print(f'Display info ran with arguments ({name}, {age})')

#run the function with display_info(name, age) along with the three layers of decorators
#annotated with '@'
display_info('John', 25)
display_info('Travis', 30)