# name,letter = input("Enter your name and single letter comma seprated : ").split(",")
# print(f"the length of Entred name is {len(name)}")
# # print(f"the charactor {letter} is {name.count(letter)} times present in {name}")
# # for charactor insencitive we use this line
# #  name.lower().count(letter.lower())
# resul = name.replace(" ","").lower().count(letter.replace(" ","").lower())
# print(f"the charactor {letter} is {resul} times present in {name}")
# print()
age = int(input("Enter your age : "))
if age >= 14 :
    print(f"your age is {age} which is above 14,\nso you can procedue")
    
else:
        print("sorry! you can't procedue ")