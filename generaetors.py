"""
The concept of generator gets really usefull when dealing with a large data size. Let say we have a data frame which 
is really big. Loading the entire data frame can make the process really slow. We can use generator here.

The generator yeilds chunks of the object(data) when called. Let's see an example
"""

def generator_func():
    n = 0
    while True:
        yield n
        n+=100

gen = generator_func()
print(next(gen))
print(next(gen))
print(next(gen))

# output:
    # 0
    # 100
    # 200
"""
    Here we can see the genereator_func() actually runs an infinite loop. But using yield plays the interesting role here.
    As a result of using as a generator, it only return value when the generator is called inside next(). 
    After yielding the value at that time, it updates the value. Let see another example
"""

print(f"\n\n")
print("#"*50)
print(f"\n\n")


nums = [ i for i in range(1000000)]

def load_nums(n):
    start = 0
    end = n
    while n <= len(nums):
        yield nums[start:end]

        start = end+0
        end += n

num = load_nums(100)

print(next(num))
print(next(num))
print(next(num))
print(next(num))
# It prints number [0,1...99], [100, 101..199] and so on. Here we can see, instead of loading the entire
# nums list, we can load it in smaller chunks and perform operations on them. This way we can save both memory and load time.