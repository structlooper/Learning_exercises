from functools import wraps
import time
def time_taken(any_function):
    @wraps(any_function)
    def warpper_function(*args,**kwags):
        t1 = time.time()
        returned_value = any_function(*args,**kwags)
        t2 = time.time()
        print(f"time taken by {any_function.__name__} function to run is {t2-t1} sec")
        return returned_value
    return warpper_function
@time_taken
def subtraction(a,b):
     return b-a
print(subtraction(2,10))

@time_taken
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

print(square_finder(1000))
