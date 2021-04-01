# Dictionary: Key-Value pairs, unordered, mutable

# Note : list cannot be used as key but tuple can be

# initializing
myDict = {"Name": "Manivannan", "Age": 24, "City": "Bangalore"}
print(myDict)
# by dict()
myDict = dict(Name="Manivannan", Age=24, City="Bangalore")
print(myDict)

# accessing
print(myDict["Name"])

# add new key value pair
myDict["email"] = "manivannan@gmail.com"
print(myDict)

# delete key value pair
del myDict["email"]
print(myDict)
# using pop()
myDict.pop("Age")
print(myDict)
# popitem() removes the last item
myDict.popitem()
print(myDict)

myDict = {"Name": "Manivannan", "Age": 24,
          "City": "Bangalore", "Email": "manivannan@gmail.com"}

# contains key operation
if "Name" in myDict:
    print(myDict["Name"])
else:
    print("'Name' field is not present")

# iteration
for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)

for key, value in myDict.items():
    print(key, value)

# copying
newDict = myDict.copy()
newDict2 = dict(myDict)

# merging two dicts
myDict1 = {"Name": "Manivannan", "Age": 24, "City": "Bangalore"}
myDict2 = {"Name": "Manivannan", "City": "Bangalore",
           "Email": "manivannan@gmail.com"}

myDict1.update(myDict2)
print(myDict1)
