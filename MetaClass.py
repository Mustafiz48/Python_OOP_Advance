"""
A metaclass is a class whose instances are classes. 
Like an "ordinary" class defines the behavior of the instances of the class, a metaclass defines the behavior of classes and their instances.
ref: https://python-course.eu/oop/metaclasses.php

So metaclass is a class whose object is another class. 
So in __new()__, instead of returning an object, we need to return a class (uh...kind of).
Before going into metaclass, we need to understand how classes are actually created. Let's dive into code.
"""

class MyClass():
    pass
obj = MyClass()

print(obj)
print(MyClass)
print(type(MyClass))
#output:
    # <__main__.MyClass object at 0x0000023340A9ADD0>
    # <class '__main__.MyClass'>
    # <class 'type'>

# So we have an object and a class, as expected. 

MyTypeClass = type("MyTypeClass", (),{})
obj_2 = MyTypeClass()
print(obj_2)
print(MyTypeClass)
print(type(MyTypeClass))

# output:
    # <__main__.MyTypeClass object at 0x000001FE2115B4F0>
    # <class '__main__.MyTypeClass'>
    # <class 'type'>
"""
Wait a minute, the outputs are the same!! Yes, with type(), we can create function. the syntex is: 
    type(name, bases, attrs)
Where:
    name: name of the class
    bases: tuple of the parent class (for inheritance, can be empty)
    attrs: dictionary containing attributes names and values

Actually when we create a class, internally the type() function creates that class for us. That's why type() of class is 'type'.

Now to create a meta class, we need to inherit it from type. Let's create out metaclass.
"""

print(f"\n\n")
print("#"*50)
print(f"\n\n")

class MyMeta(type):
    def __new__(cls, class_name, base_classes, attrs):
        print("Class name: ", class_name)
        print("Parent classes: ", base_classes)
        print("Attributes: ", attrs)

        return type(class_name,base_classes,attrs)
    
class NormalCalss:
    pass
class MetaClass(metaclass=MyMeta):
    pass

normal_obj = NormalCalss()
meta_obj = MetaClass()
# output
    # Class name:  MetaClass
    # Parent classes:  ()
    # Attributes:  {'__module__': '__main__', '__qualname__': 'MetaClass'}

# I know we did nothing but print some lines. But it is just to show the example of metaclass. 
# Usecase of Metaclass is another topic. Let's create another class that inherits MyMeta

print(f"\n\n")
print("#"*50)
print(f"\n\n")

class BaseClass():
    pass
class MyClass(BaseClass, metaclass = MyMeta):
    def __init__(self, val1, val2):
        self.val_1 = val1
        self.val_2 = val2
    def get_val_1(self):
        return self.val_1
    
myobj = MyClass(5, 10)

# output
    # Class name:  MyClass
    # Parent classes:  (<class '__main__.BaseClass'>,)
    # Attributes:  {'__module__': '__main__', '__qualname__': 'MyClass', '__init__': <function MyClass.__init__ at 0x000001B747FDFA30>, 'get_val_1': <function MyClass.get_val_1 at 0x000001B747FDFAC0>}


# To see one of the usecase of Metaclass, look at the MetaClassExample file in this repo