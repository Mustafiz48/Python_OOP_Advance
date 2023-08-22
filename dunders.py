'''
Dunders are sometimes called magic methods in python. The most of the popular magic methods are related
to classes. Another use of dunders are operator overloading. Let's see some of the most used dunders.
'''

# __init__() and __new__()
class A:
    def __new__(cls, *args, **kwargs):
        '''
        New is called even before __init__() method. __init__() is called when an object is initiated.
        It is like the __new__() is called first and it returns an object, and after that, the __init__()
        is called with that object. Inside __init__() we then set properties and methods.

        That's why the __new__() requires to have an return value, while the __init__() doesn't have any return value.
        '''
        print("Created called")
        return super().__new__(cls)
    
    def __init__(self, val) -> None:
        '''
        __init__() is almost like an constructor. When an object is initiated, __init__() is called. 
        Inside the __init__(), we assign properties and methods to that object. Internally, __new__() is called
        before __init__()
        '''
        print(f"Init Called with {self} object and {val} value")
        self.val = val
        self.val2 = 10
        

a = A(10)
# Created called
# Init Called with <__main__.A object at 0x00000218F617BE50> object and 10 value


print(f"\n\n")
print("#"*50)
print(f"\n\n")

# __str__() vs __repr__()

'''
__str__() and __repr__() are used to format object to string. When we print an object 
we normally see something like "<__main__.A object at 0x00000218F617BE50>". This doesn't give us any useful information.
We can change this behaviour by implementing __str__() and __repr__()
'''

class B:
    def __init__(self, val, secret_val):
        self.val = val
        self.secret_val = secret_val

    def __str__(self):
        return f"Object of B calss from __str__() method with \nval: {self.val} and secret_val:{self.secret_val}"
    
    def __repr__(self) -> str:
        return f"Object of B calss from __repr__() method with \nval: {self.val} and secret_val:{self.secret_val}"

b = B(5, 10)

print(b)
print([b])
# Object of B calss from __str__() method with
# val: 5 and secret_val:10

# [Object of B calss from __repr__() method with
# val: 5 and secret_val:10]

"""
    In the output we can see when we normally print b, it calss __str__(), but when we call [b], it calls to __repr__()
    __str__() and __repr__() does almost the similar tasks. The key difference is, when we inspect an object, it calls
    __repr__() method.Inside a python session, if we just print the value without "print()" function, it calls __repr__().
    When use inside containers (like list, dict etc), __repr__() is called. Rule of thumb is use __repr__() to give
    info to developers. 


    One important note is that, if there's no __str__() method, the print() function refers to __repr__() then. 
    So it is adviced to have at least a __repr__() method.

"""

print(f"\n\n")
print("#"*50)
print(f"\n\n")

# Operator Oveloading
"""
Another popular use of dunders is for operator overloading. Let see a simple example;
"""
class ComplexNumber():
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return F"A complex Number: {self.real} + {self.imaginary}i"

    # To overload + operator
    def __add__(self, other):
         assert type(self) == type(other), "Object type didn't match" 
         # assert is used to varify a condition, then raise an error (Error message is optional, if given it will be displayed)

         real = self.real + other.real
         imaginary = self.imaginary + other.imaginary

         return ComplexNumber(real, imaginary)
    
a = ComplexNumber(1,2)
b = ComplexNumber(2,3)
res = a+b
print(a)
print(b)
print(res)

# we can do overloading of other operators the same way
# output:
    # A complex Number: 1 + 2i
    # A complex Number: 2 + 3i
    # A complex Number: 3 + 5i

c = 2
res2 = a + c
# AssertionError: Object type didn't match