# lambda arguments: expression

from functools import reduce


def add10(x): return x + 10


print(add10(5))


def mult(x, y): return x * y


print(mult(2, 8))


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# sort according to y-index
points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D)
print(points2D_sorted)


# sort according to sum of x and y
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])

print(points2D)
print(points2D_sorted)


#map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

#filter(func, seq)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

# reduce(func seq)
a = [1, 2, 3, 4, 5, 6]
product = reduce(lambda x, y: x * y, a)
print(product)
