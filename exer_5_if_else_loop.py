user_name,age = input("Enter the name and age to watch the movie : ").split()
age = int(age)
conduction = user_name[0].lower()

if conduction == 'a' and age >= 10 :
    print(f"Hello {user_name}!! \n You can watch the coco movie ")

else :
    if age < 10:
        print("Your age is smaller then limit to watch the movie ")
    else:
        print("You can't procedue, Sorry!!")
    