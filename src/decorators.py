import math
from math import pi




def my_decorator(func):
    
    def THE_REAL_ONE_HAHAHA(*args, **kwargs):

        return func(*args, **kwargs) * pi

    return THE_REAL_ONE_HAHAHA


@my_decorator
def multiply(x, y):
    return x * y




if __name__ == '__main__':
    print(multiply(1, 2))