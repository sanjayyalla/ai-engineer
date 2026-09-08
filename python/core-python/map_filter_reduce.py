# map , filter , reduce

numbers = [1, 2, 3, 4, 5]

def double(x):
    return x * 2

# or 

# double = lambda a:a*2

res = map(double, numbers)

print(list(res))

#Filter


num = [1,2,3,4,5]

even = lambda n : n % 2 == 0

result = filter(even,num)

print(list(result))


# Reduce
from functools import reduce

people = [
    ("Boys",2000),
    ("Girls",2000),
    ("Men",2000)
]

sum = reduce(lambda a, b : a+b[1], people,0) 

print(sum)
