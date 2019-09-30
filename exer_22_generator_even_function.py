def generator_function(n):
    for i in range(2,n+1,2):
         yield(i)

for num in generator_function(10):
    print(num)

print(generator_function(10)) 