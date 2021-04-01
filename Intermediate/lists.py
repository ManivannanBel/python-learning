#Lists: ordered, mutable, allows duplicate lements
myList = ["banana", "orange", "apple", "guava"]
print(myList)

#create empty list
myList2 = list()
print(myList2)

#list of different types
myList3 = [5, True, "apple"]
print(myList3)

#print from last
print(myList[-1])

#iterate list
for l in myList:
    print(l)

#in keyword
if "banana" in myList:
    print("banana is present in myList")
else:
    print("banana is not present in myList")

#length
print(len(myList))

#append
myList.append("coconut")
print(myList)

#insert at specific position
myList.insert(1, 'strawberry')
print(myList)

#pop method, removes the last item
print(myList.pop())
print(myList)

#remove specific element
myList.remove("orange")
print(myList)

#reverse method
myList.reverse()
print(myList)

#sort method - inplace sorting
myList.sort()
print(myList)

#sorted() - returns a new sorted list
myList4 = [1,-3, -1, 6, 4, 8, 19, -2, -10]
sortedList = sorted(myList4)
print(myList4)
print(sortedList)

#create multiple times
myList5 = [0] * 5
print(myList5)

#concatenate two lists
newList1 = myList5 + sortedList
print(newList1)

#slicing
newList2 = newList1[1:5]
print(newList2)

newList2 = newList1[::2]
print(newList2)

#copying list
originalList = [1,5,3,8,6,9,0,4,3,67,43,22,7]
#modifying one will change another also
cpyList = originalList
print(cpyList)

#have seperate memeory for copying
cpyList = originalList[:]   #copy by slicing
cpyList = originalList.copy()   #copy by copy()
cpyList = list(originalList)    #copy by list()
print(cpyList)

#lambda
newList3 = [1,2,3,4,5,6,7,8,9,10]
squaredList = [x * x for x in newList3]
print(squaredList)


