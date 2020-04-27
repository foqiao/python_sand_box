def decorative_func(ori_func):
    def wrapper_func(*args, **kwargs):
        print(f'Wrapper execute this before {ori_func}')
        return ori_func(*args, **kwargs)
    return wrapper_func

class decorator_class:
    def __init__(self, ori_func):
        self.ori_func = ori_func

    def __call__(self, *args, **kwargs):
        print(f"Call method execute before {self.ori_func}")
        return self.ori_func(*args, **kwargs)

@decorative_func
def display():
    print('display function ran')