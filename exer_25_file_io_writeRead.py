with open('file.txt','r') as file1:
    with open("file1.txt",'w') as sol_file:
    # string = file1.readline()
      for string in file1.readlines():
        #  print(string)
         name,salary = string.split(",")
         sol_file.write(f"{name}\'s salary is {salary}")