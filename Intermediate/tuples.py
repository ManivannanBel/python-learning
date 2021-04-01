#Tuple: ordered, immutable, allows duplicate elements
myTuple = ("Max", 28, "Boston")
print(myTuple)

myTuple1 = tuple(["Max", 28, "Mani"])
print(myTuple1)

#get item by index
print(myTuple1[0])

#iteration
for x in myTuple1:
    print(x)

#in keyword
if "Max" in myTuple1:
    print("'Max' is in myTuple1")
else:
    print("'Max' is not in myTuple1")

myTuple2 = ('a', 'b', 'c', 't', 'w', 't', 'k', 'q', 'i', 'i')
#length of tuple
print(len(myTuple2))
#count the specific item's occurrence
print(myTuple2.count('i'))
#get the index of the specific element
print(myTuple2.index('a'))

#create list from a tuple
myList = list(myTuple2)
#create tuple from list
newTuple = tuple(myList)

#slicing
myTuple3 = (1,6,4,8,5,79,3,5,8,3)
print(myTuple3[2:5])
#step
print(myTuple3[::2])

#unpack tuple
myTuple4 = ("Mani", 24, "CSE")
name, age, course = myTuple4
print("name:", name, " Age:", age, " Course:", course)

myTuple5 = (1,2,3,4,5,6,7,8,9,10)
l1, *l2, l3 = myTuple5
#first element
print(l1)
#middle elements list
print(l2)
#middle element
print(l3)

