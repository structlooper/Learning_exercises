def reverse_list_function(l):
    reverse_list = []
    for sub_num in l:
        reverse_list.append(sub_num[::-1])
    return reverse_list
        

numbers = ["abc","def","ijk"]
print(numbers)
print(f"The Output number is {reverse_list_function(numbers)} " )
