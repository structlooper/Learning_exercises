def square(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
numbers = list(range(1,11))
print(square(numbers)) 