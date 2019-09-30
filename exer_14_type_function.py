numbers = [1,2,3,[4,5,6],[7,8,9]]

def type_function(l):
    output = []
    for i in l:
        if type(i) == list:
             output.append(type(i))
    return len(output)
       

print(type_function(numbers))