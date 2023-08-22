"""
    Here we will work with python's abc module, which is Abstract base class. It's like declaring Interface 
    in other language. We will use abc with two following condition:
    • instantiating the base class is impossible; and
    • forgetting to implement interface methods in one of the subclasses raises an error as early as possible.

    Now let's go
"""

from abc import ABCMeta, abstractmethod

class IBaseClass(metaclass = ABCMeta): # I for Interface, you can skip it
    @abstractmethod
    def method_A(self):
        pass

    @abstractmethod
    def method_B(self):
        pass

class ChildClass(IBaseClass):

    def method_A(self):
        print(f"method_A() implemented in child class")

    def method_B(self):
        print(f"method_B() implemented in child class")



obj = ChildClass()
#output
    # TypeError: Can't instantiate abstract class ChildClass with abstract method method_B

"""
    Here first comment the implementation of method_B() in child class. It will immediately raise an error saying 
    it can't instantiate. If we remove the comment from method_B() implementation, then it will run normally.
    Let's also try to create an object of BaseClass.
"""

print(f"Instantiating Base Class...\n")
base_obj = IBaseClass()
# output:
    # TypeError: Can't instantiate abstract class IBaseClass with abstract methods method_A, method_B

"""
    Here we can see, we can't instantiate the base class. 
"""