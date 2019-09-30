# def word_counter(string):
#     new = {}
#     for i in string:
#         new[i] = string.count(i)
#     return new
 
# string_value = input("Enter the number to count : ")
# print(word_counter(string_value))

# list_0 = [1,2,3,4,5,5,5,5,5,6,6,6,7,7,8,8,9]
# set_0 = set(list_0)
# print(set_0)
# list_1 = list(set_0)
# print(list_1)

# def filter(l):
#     return[num for num in l if num%2 == 0]
#     # odd_num =[]
    
# list_number = list(range(1,11))
# print(filter(list_number))

# nested_statement = [[i for i in range(1,4)] for j in range(3)]
# print(nested_statement)

# def square_function(l):
# square = {num:num**3 for num in range(1,11)}
#     # return square
# # print(square)
# for i in square:
#     print(f"cube of {i} : {square[i]}")

# odd_even = {i : ('even' if i%2 == 0 else 'odd') for i in range(1,11)}
# print(odd_even)

# name = ['deepak','rohit','structlooper']
# first_letter = {k[1:3:3] for k in name}
# print(first_letter)

# def total(*args):
#     total_num = 0
#     for num in args:
#         total_num += num
#     return total_num
# user_number = 1,2,3,4,5,6
# print(total(*user_number))

# even_function = lambda a: a%2 == 0
# print(even_function(4))

# func = lambda s: len(s)>5
# print(func('Deepak'))

# def func(l,target):
#     for pos , name in enumerate(l):
#         if name == target.lower():
#             return pos
#     return 'not found'
        
#         # print(f"{pos}--> {target}")
# list_item = ['abcd','efgh','deepak']
# print(func(list_item,'Deepak'))

# user_numbers = [1,2,3,4,5,6]
# print(list(map(lambda a: a**2,user_numbers)))

# average_finder = lambda *args: [ sum(pair)/len(pair) for pair in zip(*args) ]
# user_list = ([1,2,3],[4,5,6],[7,8,9])
# print(average_finder(*user_list))

# num1 = [2,3,4,6,8]
# def func(l):
#     result = [num % 2 == 0 for num in l]
#     return result
# print(func(num1))

# def add(l):
#     ''' this is doc string '''
#     return l**2
# print(zip.__doc__)

# def my_map(function,l):
#     return[function(item) for item in l]
# print(my_map(lambda a : a**3,[1,2,3,4]))

# def head_function(func):
#     def inner_function():
#         print("this is awsome")
#         func()
#     return inner_function
# def function():
#     print("function 1")
# @head_function
# def function2():
#     print("this is function 2")
# function2()

# from functools import wraps
# def print_function_data(any_funtion):
#     @wraps(any_funtion)
#     def wrapper_function(*args,**kwargs):
#         '''this is wrapper_function '''
#         print(f"You are calling {any_funtion}")
#         print(f"this function take {args} parameters")
#         return any_funtion(*args,**kwargs)
#     return wrapper_function
# @print_function_data
# def subtract(b,a):
#     '''this is subtract function'''
#     return b-a

# print(subtract.__doc__)
# print(subtract(10,2))

# from functools import wraps
# def universal_data_type(data_type):
#     def decorator_function(any_function):
#         @wraps(any_function)
#         def wrapper_function(*args, **kwargs):
#             if all([type(args) == data_type for args in args]):
#                 return any_function(*args ,**kwargs)
#             elif any([type(kwargs) == True for kwargs in kwargs]):
#                 return "KEYWORD ARGUMENT NOT ILETRABLE"
#             return "Invalid Argument"
#         return wrapper_function
#     return decorator_function
    
# @universal_data_type(str)
# def stng_add(*args):
#     temp = ""
#     for string in args:
#         temp += string
#     return temp

# print(string_add('Deepak',' Kumar'))


# def number(n):
#     for i in range(1,n+1):
#         yield(i)

# for i in number(10):
#     print(i)

# print(number(10))


