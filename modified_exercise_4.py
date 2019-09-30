import random
number = random.randint(1,100)
guess = 1
user_number = int(input("Enter the number : "))


while True:
   
     if user_number == number :
         print(f"YOU WIN!! you guseed in {guess} times ")
         break
         
     else:
          if user_number < number:
              print("too low !!")
              
          else:
              print("too high")
          guess += 1 
          user_number = int(input("guess again : "))        
          