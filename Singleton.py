"""
In Singleton design pattern, only one single object of class can be created. 
The singleton pattern is a design pattern that restricts the instantiation of a class to one object.
It is used in cases where exactly one object is needed.

Ref: https://python-course.eu/oop/metaclasses.php

Actually I am using the example given in the referenced link
"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
    
class SingletonClass(metaclass=Singleton):
    pass


class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x == y)
# output: True
# So x and y are the same object. 

x = RegularClass()
y = RegularClass()
print(x == y)
# Output: False
# So, x and y are not same here

"""
In the example above, we can see how the singleton class creates an object if there's none. But
if there's an object, it only returns that. That's why, no matter how many time we cerate object
of this class, we will get the same object

On the other hand, the regular class creates different object each time we instantiate an object of 
this class. 
"""

"""
The above example uses singleton as metaclass. We can do the same by inheriting a singleton class.
See the bellow example.
"""
print(f"\n")
print("#"*50)
print(f"\n")

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    
class SingletonClass(Singleton):
    pass

class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x == y)
# Output: True

x = RegularClass()
y = RegularClass()
print(x == y)
# Output: False