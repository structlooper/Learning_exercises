def reverse_string(list0):
    new_list = [name[::-1] for name in list0]
    return new_list
# def reverse_string(l):
#     new_list = []
#     for i in l:
#         new_list.append(i[::-1])
#     return new_list
string = ['abc','def','ijk',]
print(reverse_string(string))