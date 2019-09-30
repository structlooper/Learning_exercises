# num1 = input("Enter 1 numbers " )
# num2 = input("Enter 2 numbers " )
# num3 = input("Enter 3 numbers " )
# num1,num2,num3 = int(input("Enter three numbers " )).split()
# average = (num1 + num2 + num3)/3
# print("Average of values are " + str(average))
# print(f"The average of {num1},{num2} and {num3} are {average}")
num1,num2,num3 = input ("Enter three numbers comma seprated : ").split(",")
average = (int(num1) + int(num2)+ int(num3))/3
print(f"the average of entred values are {average}")