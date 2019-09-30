reverse_list = []
def reverse_number(numbers):
    
    for i in range(1,len(numbers)+1):
        num = numbers.pop()
        reverse_list.append(num)
    print(reverse_list)



numbers = list(range(1,21))

print(numbers)
reverse_number(numbers)
