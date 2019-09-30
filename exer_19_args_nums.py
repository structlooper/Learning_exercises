def power_function(num,*args):
    # result = [i**num for i in args if (num in args) else (print("You Didn't Enter any Thing !!")) ]
    # result = []
    if args :
        return [i**num for i in args]
    else:
       return print("You Didn't Enter any Thing !!")
    
user_input = [2,2,3,4,5]
print(power_function(*user_input))