"""Let's start by opening a file, writting something into it and finally closing it"""

file = open("hello.txt", "w")
file.write("Hello World!")
file.close()

"""
Everything looks fine. Everything is actually fine. So what's the deal with context manager?
Actually there's a problem wtih the above code. Imagine some exception happened while doing the 
write statement. In that case program will raise exception while it is in the write line and it will
never call the close() fucntion. As a result the file won't be closed properly. 
How can we solve the issue? Well we can use try...finally. Let's see.   
"""

file = open("hello.txt", "w")
try: 
    file.write("Hello World!")
    # raise Exception()
finally:
    print("Closing the file")
    file.close()
    print("File Closed")

# output:
    # Closing the file
    # File Closed
    # Traceback (most recent call last):
    # File "D:\personal_project\Python_OOP_Advance\ContextManager.py", line 18, in <module>
    #     raise Exception()
    # Exception

"""
We can see the file is now closed properly even when the exception occurs. So everything is fine now.
Yes, it is fine now. We can achieve the same with context manager in a more concise way. Let's see
"""
print(f"\n")
print("#"*50)
print(f"\n")

# Comment the axception above, otherswise the code won't reach here
with open("hello.txt","w") as file:
    file.write("Hello World!")

"""
Yes, that's it. Using with statement, it takes care of closing the file. When the program's scope
comes out of the with statementl, it closes the file properly. So with context manager, we don't
need to worry about the file closig.
"""

"""
We can define a context manager class for ourself and instead of using with satatement, we can
use that class for context manager.

To implement a class to work as our custom context manager. we have to implement two dunder methods 
inside the class. They are __enter__() and __exit__(). See the stackoverflow answer bellow 
to understand them clearly. It's clear and concise. 

https://stackoverflow.com/a/38685520

I am using the same example given in the mentioned stackoverflow answer. 
"""
print(f"\n")
print("#"*50)
print(f"\n")

class Log:
    def __init__(self,filename):
        self.filename=filename
        self.fp=None    
    def logging(self,text):
        self.fp.write(text+'\n')
    def __enter__(self):
        print("__enter__() called: opening file")
        self.fp=open(self.filename,"a+")
        return self    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__() called: closing the file")
        self.fp.close()
        print("__exit__(): file closed")

with Log(r"Hello_log.txt") as logfile:
    print("In Main function")
    logfile.logging("Test1")
    logfile.logging("Test2")

# output:
    # __enter__() called: opening file
    # In Main function
    # __exit__() called: closing the file
    # __exit__(): file closed

"""
We can see how it opens and closes file just like context manager. In the __exit__(), we can see
exc_type, exc_val, exc_tb. With these, we can handle exceptions.

There's another way to create a context manager. That's with contextmanager decorator fron contextlib 
library. It's built in in python. Let's see
"""

print(f"\n")
print("#"*50)
print(f"\n")


from contextlib import contextmanager

@contextmanager
def file_cntxt(filename, mode):
    file = open(filename, mode)
    yield file
    file.close()

with file_cntxt("hello.txt", "w") as file:
    file.write("Hello World!")

"""
It works perfectly as a contexr manager. And with this example, it comes to an end here. 
Happy coding!
"""