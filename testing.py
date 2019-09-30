# name = input("Enter your name : ")
# if name :
#     print(f"Hello {name} !!")

# else :
#     print("You didn\'t type anything \nwrite your name")
# total = 0
# i = 1
# while i<=10:
#     total+=i
#     i+=1
# print(total)
# name = input("Enter your name : ")
# i = 0 
# temp = ""
# while i < len(name):
#     if name[i] not in temp:
#         print(f"{name[i].lower()} : {name.lower().count(name[i].lower())}")
#         temp += name[i].lower()
    
#     i +=1
# var = int(input("Enter the value of strig for sum : "))
# total = 0
# for i in range(0,var+1):
#     total += i
# print(total)
# name = input("Enter your name : ")
# temp = ""
# for i in range(0,len(name)):
#     if name[i] not in temp:
#         print(f" {name[i]} : {name.count(name[i])}")
#         temp += name[i]
    
# number = (input("Enter a number : "))
# total = 0
# for i in number:
#         total += int(i)
# print(total)
# def last(a):
#         return a[-1]
# name = input("Enter name :")
# print(last(name))
# def greater_num(num1,num2,num3):
#         if num1 > num2 and num3:

#                return num1
#         elif num2 > num3 and num1:
#                return num2
#         else:
#                 return num3
        
        

       

# num1,num2,num3 = input("Enter the number to compare comma seprated : ").split(",")
# num1=int(num1)
# num2 = int(num2)
# num3 = int(num3)
# print(f"The Greater number between {num1},{num2} and {num3} is {greater_num(num1,num2,num3)} ")

# def is_drom(string,reverse_string):
#         return string == reverse_string
        

# string = input("Enter the is_drom name : ")
# reverse_string = string[::-1]
# print(is_drom(string,reverse_string))
# user_ifo = [input("Enter name : "), input("Enter age : ")]
# print(', '.join(user_ifo))

# numbers = [1,2,3,[4,5,6],[7,8,9]]

# def type_function(l):
#     output = []
#     for i in l:
#         if type(i) == list:
#              output.append(type(i))
#     return len(output)
       

# print(type_function(numbers))
# number = (1,2,3,4,[7,8,9,],5)
# for i in number:
#         print(type(i))
# user_info = {}
# user_info['name'] = 'Deepak'
# user_info['age'] = 23
# print(f"{user_info} ,{type(user_info)}")
# user_info = {
#     "name" : "Deepak",
#     "age" : 23,
#     'fav_movie' : ["3_idot","Harry_Pother","Iron_man_Series"],
#     'Fav_songs' : ['happier','love_mashup' ],

# }
# more_info = {
#     'name' : 'Ashok',
#     'age' : 14,
# }
# user_info.update(more_info)
# print(user_info)33