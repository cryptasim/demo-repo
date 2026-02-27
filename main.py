import os,sys
from utils import helper_function


def   greet(name ):
    print(  "Hello, "+ name )


def calculate_sum(a,b ):
    return a+b


if __name__=="__main__":
    greet("World")
    print( calculate_sum(10,20))
