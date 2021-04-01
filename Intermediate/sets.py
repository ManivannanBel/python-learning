# Sets: unordered, mutable, no duplicates

# initializing
mySet = {1, 2, 3}
print(mySet)
mySet = set([1, 2, 3])
print(mySet)
mySet1 = set("Hello")
print(mySet1)

# add()
mySet.add(10)
mySet.add(2)
print(mySet)

# remove(), throws error when not found
mySet.remove(3)
print(mySet)

# discord(), removes element but don't throw error when not found
mySet.discard(3)
print(mySet)

# clear() to empty the set
mySet1.clear()
print(mySet1)

# pop(), removes and returns arbitrary value
print(mySet.pop())

# iteration
for x in mySet:
    print(x)

# in statement


odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
primes = {2, 3, 5, 7, 11, 13}

# union
print(odds.union(evens))
# intersection
print(odds.intersection(evens))
print(odds.intersection(primes))
print(evens.intersection(primes))


setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
# difference(), gives set of elements present in first set that are not present in second set
print(setA.difference(setB))
print(setB.difference(setA))
# symmetric_difference(), gives all the elements from both the sets that are not present in the other set
print(setA.symmetric_difference(setB))

# update(), inplace union
setA.update(setB)
print(setA)
# intersection_update(), inplace intersection
# difference_update(), inplace difference
# symmetric_difference_update(), inplace symmetric difference

# issubset(), returns boolean
print(setB.issubset(setA))
# superset(), returns boolean
print(setA.issuperset(setB))
# isdisjoint, return boolean
print(setA.isdisjoint(setB))

# copying
newSet = setB.copy()
newSet = set(setB)

# frozenset(), immutable set
immutableSet = frozenset([1, 2, 3, 4, 5, 6])
print(immutableSet)
