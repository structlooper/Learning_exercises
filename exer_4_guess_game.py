import random
num = random.randint(1,9)
user_num = int(input("Enter no. from 0 to 9 : "))
guess = 1
while True:
     if user_num == num :
         print(f"You Entered {user_num} correct number!! YOU WIN!! in {guess}")
         break
     else:
          print(f"YOU Entred {user_num} ")
    
          if user_num < num :
             print("The number is smaller then guessing number")
                       # input("guess again : ")
          else:
              print("The entred number is greater then guessing number")
          guess += 1
          user_num = int(input("guess again : "))
        

