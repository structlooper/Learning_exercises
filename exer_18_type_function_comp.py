def type_finder(l):
    return [str(item) for item in l if (type(item) == int or type(item) == float)]
    # new_list = []
    # for item in l:
    #     if type(item) == int:
    #         new_list.append(str(item))
    # return new_list
    
list_items = [1,2,3,4,(1,2,3,4,),{1:3,3:5,},'rohit','mohit',1.1,2.5]
print(type_finder(list_items))
