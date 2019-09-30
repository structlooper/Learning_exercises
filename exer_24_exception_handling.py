def div(a,b):
    try:
        return a/b
    except ValueError:
            print('Please Enter only number')
    except ZeroDivisionError:
            print('Zero is not exeptable')
    except:
            print("Undefined error !!")
    
    
num1 = input('Enter the number of a : ')
num2 = input('Enter the number of b : ')
num1 = int(num1)
num2 = int(num2)


print(div(num1,num2))
