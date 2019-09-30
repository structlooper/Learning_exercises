def cube_function(numbers):
    new = {}
    for i in range(1,numbers+1):
        new[i] = i**3
    return new
        
    
    
num = 5

print(cube_function(num))