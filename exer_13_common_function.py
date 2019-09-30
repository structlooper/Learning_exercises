def compare(l1,l2):
    common = []
    for i in l1:
    
        if i in l2:
            common.append(i)
        else:
            pass
    return common

number_1 = [1,2,3,4,5,6]
number_2 = [1,2,7,8,9]
print(compare(number_1,number_2))