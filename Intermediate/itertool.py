# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))
# repeat
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))


# permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
# perm length
a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))


# combinations
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
# combinations with replacement - create combination along with the same number itself
comb = combinations_with_replacement(a, 2)
print(list(comb))


# accumulate
a = [1, 2, 3, 4]
# sum by default
acc = accumulate(a)
print(a)
print(list(acc))
# multiply
acc = accumulate(a, func=operator.mul)
print(list(acc))
# max
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(list(acc))


# groupby
a = [1, 2, 3, 4]


def smaller_than_3(x):
    return x < 3


# group by the condition
group_by = groupby(a, key=smaller_than_3)
for key, value in group_by:
    print(key, list(value))


persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
# group by ages
group_by = groupby(persons, key=lambda x: x['age'])
for key, value in group_by:
    print(key, list(value))
