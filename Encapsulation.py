"""
We will see data encapsulation here. Data Encapsulation is a data hiding technique. In some other language we have 
getters and setters. In python we can do similar tasks.Let's see with example  
"""

class BaseClass():

    def __init__(self, private_val) -> None:
        self.__private_val = private_val

    @property
    def private_val(self):
        return self.__private_val
    
    @private_val.setter
    def private_val(self, val):
        self.__private_val = val

obj = BaseClass(10)
print(obj.private_val)
obj.private_val = 20
print(obj.private_val)
# 10
# 20

"""
Here we see how we can access private(actually name mangled) variable through property and setter function. Interesting 
point here is to notice the function name. Both the getter and setter has the same name. One is decorated
with @property and another is decorated with @funcname.setter decorator. With these two decorators, we can imitate
getters and setters for python. Also, we can define two different fucntion who can return or update the private 
values thorugh the function call.
"""


