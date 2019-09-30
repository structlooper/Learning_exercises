def filter_list(l):
    odd_list = []
    even_list = []
    for i in range(len(l)):
        if  i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    # print(odd_list)
    # print(even_list)
    filter_list_1 = [odd_list , even_list]
    print(filter_list_1)

numbers = list(range(1,11))
filter_list(numbers)