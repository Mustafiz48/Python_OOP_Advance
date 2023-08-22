# I will practice decorators for an use case of logging. It will log a function call
# what parameter the function recieves, how much time does it takes and what is the return value

import time



def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function Name: {func.__name__}, \nCalled with Parameters: {args, kwargs}")
        start_time = time.time()
        res = func(*args, *kwargs)
        print(f"Function runtime: {time.time()-start_time}")
        print(f"Return value from func: {res}\n")
        return res
    return wrapper

@logger
def sleep_func(n=10):
    for i in range(n):
        time.sleep(1)
    return n

result = sleep_func(5)
print("Result outside is: ",result)